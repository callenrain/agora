# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Presenter.nickname'
        db.add_column(u'archives_presenter', 'nickname',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Presenter.nickname'
        db.delete_column(u'archives_presenter', 'nickname')


    models = {
        u'archives.presenter': {
            'Meta': {'object_name': 'Presenter'},
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'formal_abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'grad_year': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informal_abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'major': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'profile_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project_docs': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project_title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['archives']