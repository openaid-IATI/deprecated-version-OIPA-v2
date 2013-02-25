# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Solid_waste_disposal_by_shelter_deprivation'
        db.delete_table('data_solid_waste_disposal_by_shelter_deprivation')

        # Adding model 'SolidWastDisposalShelterDeprivation'
        db.create_table('data_solidwastdisposalshelterdeprivation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unhabitat_indicator_country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.UnHabitatIndicatorCountry'])),
            ('kind_of_soil_waste_disposal', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('urban', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('non_slum_household', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slum_household', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('one_shelter_deprivation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('two_shelter_deprivations', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('data', ['SolidWastDisposalShelterDeprivation'])


    def backwards(self, orm):
        # Adding model 'Solid_waste_disposal_by_shelter_deprivation'
        db.create_table('data_solid_waste_disposal_by_shelter_deprivation', (
            ('kind_of_soil_waste_disposal', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('one_shelter_deprivation', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('unhabitat_indicator_country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.UnHabitatIndicatorCountry'])),
            ('non_slum_household', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('two_shelter_deprivations', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('slum_household', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('urban', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('data', ['Solid_waste_disposal_by_shelter_deprivation'])

        # Deleting model 'SolidWastDisposalShelterDeprivation'
        db.delete_table('data_solidwastdisposalshelterdeprivation')


    models = {
        'data.activitystatistics': {
            'Meta': {'object_name': 'ActivityStatistics'},
            'iati_identifier': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['data.IATIActivity']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_budget': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '20', 'decimal_places': '2', 'blank': 'True'})
        },
        'data.activitystatustype': {
            'Meta': {'object_name': 'ActivityStatusType'},
            'code': ('django.db.models.fields.IntegerField', [], {'max_length': '8', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Country']", 'null': 'True', 'blank': 'True'})
        },
        'data.aidtype': {
            'Meta': {'object_name': 'AidType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'primary_key': 'True'})
        },
        'data.budget': {
            'Meta': {'object_name': 'Budget'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.CurrencyType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period_end': ('django.db.models.fields.DateField', [], {}),
            'period_start': ('django.db.models.fields.DateField', [], {}),
            'type': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'})
        },
        'data.city': {
            'Meta': {'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'data.collaborationtype': {
            'Meta': {'object_name': 'CollaborationType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '55', 'primary_key': 'True'})
        },
        'data.country': {
            'Meta': {'object_name': 'Country'},
            'country_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dac_country_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dac_region_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dac_region_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '2', 'primary_key': 'True'}),
            'iso2': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'iso3': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'data.countrystatistics': {
            'Meta': {'object_name': 'CountryStatistics'},
            'country': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['data.Country']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'total_activities': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'data.currencytype': {
            'Meta': {'object_name': 'CurrencyType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Country']", 'null': 'True', 'blank': 'True'})
        },
        'data.distributioncookingfuelbyshelterdepr': {
            'Meta': {'object_name': 'DistributionCookingFuelByShelterDepr'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'non_slum_household': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'one_shelter_deprivation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slum_household': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'two_shelter_deprivations': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'type_of_cooking_fuel': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'unhabitat_indicator_country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.UnHabitatIndicatorCountry']"}),
            'urban': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'data.financetype': {
            'Meta': {'object_name': 'FinanceType'},
            'code': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'primary_key': 'True'})
        },
        'data.flowtype': {
            'Meta': {'object_name': 'FlowType'},
            'code': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'primary_key': 'True'})
        },
        'data.iatiactivity': {
            'Meta': {'object_name': 'IATIActivity'},
            'activity_status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.ActivityStatusType']", 'null': 'True', 'blank': 'True'}),
            'collaboration_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.CollaborationType']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'default_aid_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.AidType']", 'null': 'True', 'blank': 'True'}),
            'default_finance_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.FinanceType']", 'null': 'True', 'blank': 'True'}),
            'default_flow_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.FlowType']", 'null': 'True', 'blank': 'True'}),
            'default_tied_status_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.TiedAidStatusType']", 'null': 'True', 'blank': 'True'}),
            'end_actual': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_planned': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'iati_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'reporting_organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Organisation']"}),
            'start_actual': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'start_planned': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'data.iatiactivitybudget': {
            'Meta': {'object_name': 'IATIActivityBudget', '_ormbases': ['data.Budget']},
            'budget_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['data.Budget']", 'unique': 'True', 'primary_key': 'True'}),
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"})
        },
        'data.iatiactivitycontact': {
            'Meta': {'object_name': 'IATIActivityContact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mailing_address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'organisation': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'data.iatiactivitycountry': {
            'Meta': {'object_name': 'IATIActivityCountry'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Country']"}),
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'data.iatiactivitydescription': {
            'Meta': {'object_name': 'IATIActivityDescription'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Language']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
        'data.iatiactivitydocument': {
            'Meta': {'object_name': 'IATIActivityDocument'},
            'format': ('django.db.models.fields.CharField', [], {'max_length': '55', 'null': 'True', 'blank': 'True'}),
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Language']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'data.iatiactivitypolicymarker': {
            'Meta': {'object_name': 'IATIActivityPolicyMarker'},
            'code': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'significance_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.SignificanceType']", 'null': 'True', 'blank': 'True'}),
            'vocabulary_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.VocabularyType']", 'null': 'True', 'blank': 'True'})
        },
        'data.iatiactivityregion': {
            'Meta': {'object_name': 'IATIActivityRegion'},
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Region']"})
        },
        'data.iatiactivitysector': {
            'Meta': {'object_name': 'IATIActivitySector'},
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sectors'", 'to': "orm['data.IATIActivity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Sector']"})
        },
        'data.iatiactivitytitle': {
            'Meta': {'object_name': 'IATIActivityTitle'},
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Language']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'data.iatiactivitywebsite': {
            'Meta': {'object_name': 'IATIActivityWebsite'},
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'data.iatitransaction': {
            'Meta': {'object_name': 'IATITransaction', '_ormbases': ['data.Transaction']},
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"}),
            'transaction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['data.Transaction']", 'unique': 'True', 'primary_key': 'True'})
        },
        'data.language': {
            'Meta': {'object_name': 'Language'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'data.organisation': {
            'Meta': {'object_name': 'Organisation'},
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'org_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'org_name_lang': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '25', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'data.organisationstatistics': {
            'Meta': {'object_name': 'OrganisationStatistics'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organisation': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['data.Organisation']", 'unique': 'True'}),
            'total_activities': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'data.otheridentifier': {
            'Meta': {'object_name': 'OtherIdentifier'},
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner_ref': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'data.participatingorganisation': {
            'Meta': {'object_name': 'ParticipatingOrganisation'},
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'org_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'org_name_lang': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'data.planneddisbursement': {
            'Meta': {'object_name': 'PlannedDisbursement'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.CurrencyType']"}),
            'iati_activity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.IATIActivity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period_end': ('django.db.models.fields.DateField', [], {}),
            'period_start': ('django.db.models.fields.DateField', [], {})
        },
        'data.region': {
            'Meta': {'object_name': 'Region'},
            'code': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'primary_key': 'True'})
        },
        'data.sector': {
            'Meta': {'object_name': 'Sector'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '55', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'vocabulary_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.VocabularyType']", 'null': 'True', 'blank': 'True'})
        },
        'data.significancetype': {
            'Meta': {'object_name': 'SignificanceType'},
            'code': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'primary_key': 'True'})
        },
        'data.solidwastdisposalshelterdeprivation': {
            'Meta': {'object_name': 'SolidWastDisposalShelterDeprivation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind_of_soil_waste_disposal': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'non_slum_household': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'one_shelter_deprivation': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slum_household': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'two_shelter_deprivations': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'unhabitat_indicator_country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.UnHabitatIndicatorCountry']"}),
            'urban': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'data.tiedaidstatustype': {
            'Meta': {'object_name': 'TiedAidStatusType'},
            'code': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'primary_key': 'True'})
        },
        'data.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'aid_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.AidType']", 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.CurrencyType']", 'null': 'True', 'blank': 'True'}),
            'disbursement_channel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'finance_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.FinanceType']", 'null': 'True', 'blank': 'True'}),
            'flow_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.FlowType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider_org': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'provider_org'", 'to': "orm['data.Organisation']"}),
            'receiver_org': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'receiver_org'", 'null': 'True', 'to': "orm['data.Organisation']"}),
            'tied_aid_status_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_type': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'value_date': ('django.db.models.fields.DateField', [], {})
        },
        'data.unhabitatindicatorcity': {
            'Meta': {'object_name': 'UnHabitatIndicatorCity'},
            'avg_annual_rate_change_urban_agglomerations': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bottle_water': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.City']"}),
            'composting_toilet': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'connection_to_electricity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'has_telephone': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'improved_floor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'improved_flush_toilet': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'improved_pit_latrine': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'improved_spring_surface_water': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'improved_toilet': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'improved_water': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'piped_water': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pit_latrine_with_slab_or_covered_latrine': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pit_latrine_without_slab': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop_urban_agglomerations': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'protected_well': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'public_tap_pump_borehole': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pump_borehole': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rainwater': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slum_proportion_living_urban': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sufficient_living': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'under_five_mortality_rate': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'urban_slum_population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {}),
            'year_plus_range': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'data.unhabitatindicatorcountry': {
            'Meta': {'object_name': 'UnHabitatIndicatorCountry'},
            'avg_annual_rate_change_percentage_urban': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'avg_annual_rate_change_total_population': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bottle_water': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'composting_toilet': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'connection_to_electricity': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Country']"}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'has_telephone': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'improved_floor': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'improved_flush_toilet': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'improved_pit_latrine': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'improved_spring_surface_water': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'improved_toilet': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'improved_water': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'piped_water': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pit_latrine_with_slab_or_covered_latrine': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pit_latrine_without_slab': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop_rural_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop_urban_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pop_urban_percentage': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'protected_well': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'public_tap_pump_borehole': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pump_borehole': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rainwater': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slum_proportion_living_urban': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sufficient_living': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'under_five_mortality_rate': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'urban_slum_population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {}),
            'year_plus_range': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'data.vocabularytype': {
            'Meta': {'object_name': 'VocabularyType'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'primary_key': 'True'})
        }
    }

    complete_apps = ['data']