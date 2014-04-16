# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Presenter'
        db.create_table(u'archives_presenter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('major', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('grad_year', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('profile_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('formal_abstract', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('informal_abstract', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('video', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('project_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('project_docs', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'archives', ['Presenter'])


    def backwards(self, orm):
        # Deleting model 'Presenter'
        db.delete_table(u'archives_presenter')


    models = {
        u'archives.presenter': {
            'Meta': {'object_name': 'Presenter'},
            'formal_abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'grad_year': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informal_abstract': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'profile_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project_docs': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['archives']