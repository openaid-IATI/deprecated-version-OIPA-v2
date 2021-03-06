# Django specific
import json
from django.db import connection
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from django.views.generic import FormView
from data.models.common import IndicatorData
from data.models.constants import countryData, REGION_CHOICES, REGION_CHOICES_DICT
from utils.forms import UploadForm
from django.core.urlresolvers import reverse

import pdb

class JSONResponse(HttpResponse):
    def __init__(self, data):
        output = simplejson.dumps(data)
        super(JSONResponse, self).__init__(output, mimetype="text/javascript")

def render_to(template):
    """
    Decorator for Django views that sends returned dict to render_to_response function
    with given template and RequestContext as context instance.

    If view doesn't return dict then decorator simply returns output.
    Additionally view can return two-tuple, which must contain dict as first
    element and string with template name as second. This string will
    override template name, given as parameter

    Parameters:

     - template: template name to use
    """
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if isinstance(output, (list, tuple)):
                return render_to_response(output[1], output[0], RequestContext(request))
            elif isinstance(output, dict):
                return render_to_response(template, output, RequestContext(request))
            return output
        return wrapper
    return renderer


def render_json(func):
    def wrapper(request, *args, **kw):
        data = func(request, *args, **kw)
        if isinstance(data, HttpResponse):
            return data
        return JSONResponse(data)
    return wrapper
class UploadUnHabitatIndicatorCountryCSV(FormView):
    template_name = "upload_csv.html"
    form_class = UploadForm

    def get_success_url(self):
        return reverse('upload_data')

    def get_context_data(self, **kwargs):
        data = super(UploadUnHabitatIndicatorCountryCSV, self).get_context_data(**kwargs)
        return data

    def form_valid(self, form):
        form.save()
        return super(UploadUnHabitatIndicatorCountryCSV, self).form_valid(form=form)
def make_where_query(values, name):
    query = ''
    if values:
        if not values[0]:
            return None

        for v in values:
            query += '  ' + name + ' = "' + v +'" OR'
        query = query[:-2]
    return query

def test_json_response(request):

    country_filters = request.GET.get('countries', None)
    if country_filters:
        country_q = make_where_query(values=country_filters.split(','), name='iso')
        country_q += ') AND ('
    else:
        country_q = ''

    region_filters = request.GET.get('regions', None)
    if region_filters:
        region_q = make_where_query(values=region_filters.split(','), name='dac_region_code')
        region_q += ') AND ('
    else:
        region_q = ''

    indicator_filters = request.GET.get('indicator', None)
    if indicator_filters:
        indicator_q = make_where_query(values=indicator_filters.split(','), name='indicator_id')
        indicator_q += ') AND ('
    else:
        indicator_q = ''

    if not indicator_q:
        indicator_q = ' indicator_id = "population"'

    filter_string = '  (' + country_q + region_q + indicator_q + ')'

    if 'AND ()' in filter_string:
        filter_string = filter_string[:-6]

    cursor = connection.cursor()

    cursor.execute('SELECT indicator_id, da.friendly_label, da.type_data, id.country_id, country_name, dac_region_code, dac_region_name, value, year, latitude, longitude, C.iso '
                   'FROM data_indicatordata id LEFT OUTER JOIN data_country C ON id.country_id=C.iso, data_indicator da '
                   'WHERE da.name = indicator_id AND %s' % (filter_string))
    #LEFT OUTER JOIN data_city City ON C.iso = City.country_id
    cursor_max = connection.cursor()

    if indicator_filters:
        indicator_q = make_where_query(values=indicator_filters.split(','), name='indicator_id')
#        indicator_q += ' AND '
    else:
        indicator_q = ''

    if not indicator_q:
        indicator_q = ' indicator_id = "population"'

    cursor_max.execute('SELECT max(value) as max_value FROM data_indicatordata WHERE %s' % indicator_q)
    result_max = cursor_max.fetchone()
    desc = cursor.description
    results = [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]
    new_results = []
    country = {}
    regions = {}
    countries = {}
    cities = {}
    for r in results:
        years = {}

        year = {}

        #        year[r['year']] = r['value']
#        years.append(year)
#        try:
        #check if it has a result
        if r['value']:
            try:
                years = country[r['country_id']]['years']
            except:
                country[r['country_id']] = {'name' : r['country_name'], 'indicator_friendly' : r['friendly_label'], 'type_data' : r['type_data'] , 'indicator' : r['indicator_id'], 'longitude' : r['longitude'], 'latitude' : r['latitude'], 'max_value' : result_max[0], 'years' : {}}



            years = country[r['country_id']]['years']
            year['y' + str(r['year'])] = r['value']


            country[r['country_id']]['years'].update(year)

            region = {}
            if r['dac_region_code']:
                region[r['dac_region_code']] = r['dac_region_name']
                regions.update(region)

            cntry = {}
            if r['country_id']:
                cntry[r['country_id']] = r['country_name']
                countries.update(cntry)


    country['regions'] = regions
    country['countries'] = countries

#        cit = {}
#        if r['name']:
#            cit[r['name']] = r['name']
#            cities.update(cit)
    #getting all the cpi indicators
    cursor = connection.cursor()
    cursor.execute('SELECT DISTINCT indicator_id, friendly_label'
                   ' FROM data_indicatordata did, data_indicator di WHERE did.indicator_id = di.name ')

    desc = cursor.description
    results = [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]
    indicators = {}
    for r in results:
        indicator = {}
        indicator[r['indicator_id']] = r['friendly_label']
        indicators.update(indicator)

    country['indicators'] = indicators


    return HttpResponse(json.dumps(country), mimetype='application/json')


def test_json_city_response(request):
    city_filters = request.GET.get('city', None)
    if city_filters:
        city_q = make_where_query(values=city_filters.split(','), name='name')
        city_q += ') AND ('
    else:
        city_q = ''

    country_filters = request.GET.get('countries', None)
    if country_filters:
        country_q = make_where_query(values=country_filters.split(','), name='iso')
        country_q += ') AND ('
    else:
        country_q = ''

    region_filters = request.GET.get('regions', None)
    if region_filters:
        region_q = make_where_query(values=region_filters.split(','), name='dac_region_code')
        region_q += ') AND ('
    else:
        region_q = ''

    indicator_filters = request.GET.get('indicator', None)
    if indicator_filters:
        indicator_q = make_where_query(values=indicator_filters.split(','), name='indicator_id')
        indicator_q += ') AND ('
    else:
        indicator_q = ''

    if not indicator_q:
        indicator_q = ' indicator_id = "cpi_5_dimensions"'
    filter_string = ' AND (' + city_q + country_q + region_q + indicator_q + ')'
    if 'AND ()' in filter_string:
        filter_string = filter_string[:-6]
    cursor = connection.cursor()
    cursor.execute('SELECT indicator_id, city_id, name, country_name, iso, value, year, Ci.longitude, Ci.latitude, dac_region_code, dac_region_name '
                   'FROM data_indicatorcitydata icd LEFT OUTER JOIN data_city Ci ON icd.city_id=Ci.id, data_country dc where dc.iso = Ci.country_id and year=2012 %s' % (filter_string))

    desc = cursor.description
    results = [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]

    cursor_max = connection.cursor()

    if indicator_filters:
        indicator_q = make_where_query(values=indicator_filters.split(','), name='indicator_id')
    #        indicator_q += ' AND '
    else:
        indicator_q = ''

    if not indicator_q:
        indicator_q = ' indicator_id = "cpi_5_dimensions"'

    cursor_max.execute('SELECT max(value) as max_value FROM data_indicatorcitydata WHERE %s' % indicator_q)
    result_max = cursor_max.fetchone()

    country = {}
    regions = {}
    countries = {}
    cities = {}
    for r in results:
        year = {}
        try:
            country[r['city_id']]['years']
        except:
            country[r['city_id']] = {'name' : r['name'], 'indicator' : r['indicator_id'], 'longitude' : r['longitude'], 'latitude' : r['latitude'], 'max_value' : result_max[0], 'years' : {}}

#        years = country[r['city_id']]['years']
        year['y' + str(r['year'])] = r['value']

        country[r['city_id']]['years'].update(year)

        region = {}
        if r['dac_region_code']:
            region[r['dac_region_code']] = r['dac_region_name']
            regions.update(region)

        cntry = {}
        if r['iso']:
            cntry[r['iso']] = r['country_name']
            countries.update(cntry)

        cit = {}
        if r['name']:
            cit[r['name']] = r['name']
            cities.update(cit)



    country['regions'] = regions
    country['countries'] = countries
    country['cities'] = cities

    #getting all the cpi indicators
    cursor = connection.cursor()
    cursor.execute('SELECT DISTINCT indicator_id, friendly_label'
                   ' FROM data_indicatorcitydata cd, data_indicator i WHERE cd.indicator_id = i.name ')

    desc = cursor.description
    results = [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]
    indicators = {}
    for r in results:
        indicator = {}
        indicator[r['indicator_id']] = r['friendly_label']
        indicators.update(indicator)

    country['indicators'] = indicators
    return HttpResponse(json.dumps(country), mimetype='application/json')

def get_fields(cursor):
    desc = cursor.description
    results = [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]
    return results
#    SELECT sd.name, reporting_organisation_id, a.iati_identifier, s.sector_id, r.region_id
#FROM
#data_iatiactivity a LEFT JOIN data_iatiactivityregion r ON a.iati_identifier = r.iati_activity_id
#LEFT JOIN
#data_iatiactivitycountry ic ON a.iati_identifier = ic.iati_activity_id
#LEFT JOIN
#data_iatiactivitysector s ON a.iati_identifier = s.iati_activity_id,
#data_sector sd
#WHERE
#s.sector_id = sd.code
#and reporting_organisation_id = 'NL-1'
def json_filter_projects(request):
    cursor = connection.cursor()
    q_organisations = {'reporting_organisation_id' : request.GET.get('organisations', None)}

    filters = []

    filters.append(q_organisations)
    query_string = get_filter_query(filters=filters)
    query = 'SELECT sd.name, ic.country_id, a.iati_identifier, s.sector_id, r.region_id, c.country_name, c.dac_region_name '\
                   'FROM data_iatiactivity a '\
                   'LEFT JOIN data_iatiactivityregion r ON a.iati_identifier = r.iati_activity_id '\
                   'LEFT JOIN data_iatiactivitycountry ic ON a.iati_identifier = ic.iati_activity_id '\
                   'LEFT JOIN data_country c ON ic.country_id = c.iso '\
                   'LEFT JOIN data_iatiactivitysector s ON a.iati_identifier = s.iati_activity_id,'\
                   'data_sector sd '\
                   'WHERE '\
                   's.sector_id = sd.code %s' % query_string
    cursor.execute(query)
    results = get_fields(cursor=cursor)
    countries = {}
    countries['countries'] = {}
    countries['regions'] = {}
    countries['sectors'] = {}
    for r in results:
        country = {}
#        country[r['country_id']] = r['country_name']
#        countries['countries'].update(country)
        if r['country_name']:
            countries['countries'][r['country_id']] = r['country_name']
        if r['name']:
            countries['sectors'][r['sector_id']] = r['name']
        if r['region_id']:
            countries['regions'][r['region_id']] = REGION_CHOICES_DICT.get(r['region_id'], None)

    return HttpResponse(json.dumps(countries), mimetype='application/json')


def find_coordinates(iso2):
    coordinates = None
    for k in countryData['features']:
        try:
            if k['properties']['iso2'] == iso2:
                coordinates =  k['geometry']['coordinates']
        except KeyError:
            pass
    if coordinates:
        return coordinates
    else:
        return []

def find_type_polygon(iso2):
    polygon = None
    for k in countryData['features']:
        try:
            if k['properties']['iso2'] == iso2:
                polygon = k['geometry']['type']
        except KeyError:
            pass
    if polygon:
        return polygon
    else:
        return 'Polygon'

def get_filter_query(filters):
    q= ''

    for f in filters:
        if f[f.keys()[0]]:
            values = f[f.keys()[0]].split(',')
        else:
            values = None
        q += make_where_query(values=values, name=f.keys()[0]) + ') and ('

    q = q.replace(' and ()', '')
    q = q[:-5]
    q = " AND (" + q
    try:
        q[8]
        return q
    except IndexError:
        return ''


def json_activities_response(request):
    q_countries = { 'country_id' :request.GET.get('countries', None)}
    q_sectors = {'sector_id' : request.GET.get('sectors', None)}
    q_regions = {'dac_region_code' :request.GET.get('regions', None)}
    q_budget = {'total_budget' : request.GET.get('budget', None)}
    q_organisations = {'reporting_organisation_id' : request.GET.get('organisations', None)}

    filters = []

    filters.append(q_organisations)
    filters.append(q_countries)
#    filters.append(q_sectors)
    filters.append(q_regions)

    filter_region = []
    filter_region.append(q_regions)
    filter_sector = []
    filter_sector.append(q_sectors)

    if request.GET.get('sectors', None):
        where_sector =  ' Where ' + str(get_filter_query(filters=filter_sector)[4:])
        where_sector = ' and a.iati_identifier in (select iati_activity_id from data_iatiactivitysector s %s)  ' % where_sector
    else:
        where_sector = ''

    if q_budget['total_budget']:
        query_having = 'having total_budget ' + q_budget['total_budget'].split(',')[0]
    else:
        query_having = ''

    query_string = get_filter_query(filters=filters)
    query_string = query_string.replace('AND () and' , ' (')
    if query_string:
        query_string = ' WHERE ' + query_string[5:]

    if not 'WHERE (' in query_string:
        query_string = query_string[6:]
        query_string = ' WHERE ( ' + query_string

    # if '" ) ' in query_string:
    #     query_string = query_string[:-3]

    cursor = connection.cursor()

    query = 'SELECT c.country_id, a.iati_identifier as iati_activity, count(a.iati_identifier) as total_projects, cd.country_name, sum(bd.value) as total_budget, cd.dac_region_code '\
            ' FROM data_iatiactivity a '\
            'LEFT JOIN data_iatiactivitybudget b ON a.iati_identifier = b.iati_activity_id '\
            'LEFT JOIN data_budget bd ON b.budget_ptr_id = bd.id '\
            'LEFT JOIN data_iatiactivitycountry c ON a.iati_identifier = c.iati_activity_id '\
            'LEFT JOIN data_country cd ON c.country_id = cd.iso '\
            ' %s %s '\
            'Group by c.country_id %s' % (query_string, where_sector,query_having)
    print query
    cursor.execute(query)

    activity_result = {}
    activity_result = {'type' : 'FeatureCollection', 'features' : []}

    activities = []

#        if properties['iso2'] == 'TZ':
#            print 'hahahah'
    results = get_fields(cursor=cursor)
    for r in results:
        country = {}
        country['type'] = 'Feature'
        country['id'] = r['country_id']
        country['properties'] = {'name' : r['country_name'], 'project_amount' : r['total_projects'], 'total_budget' : str(r['total_budget'])}
        country['geometry'] = {'type' : find_type_polygon(iso2=r['country_id']), 'coordinates' : find_coordinates(iso2=r['country_id'])}

        activities.append(country)

    result = {}

    activity_result['features'] = activities
    return HttpResponse(json.dumps(activity_result), mimetype='application/json')

def json_cpi_filter_response(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM data_country')
    results = get_fields(cursor=cursor)
    result = {}
    regions = {}
    for r in results:
        region = {}
        if r['dac_region_code']:
            region[r['dac_region_code']] = r['dac_region_name']
            regions.update(region)

    result['regions'] = regions

    return HttpResponse(json.dumps(result), mimetype='application/json')


