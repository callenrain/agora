# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'archives_project')

        # Adding field 'Presenter.formal_abstract'
        db.add_column(u'archives_presenter', 'formal_abstract',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Presenter.informal_abstract'
        db.add_column(u'archives_presenter', 'informal_abstract',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Presenter.video'
        db.add_column(u'archives_presenter', 'video',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Presenter.project_image'
        db.add_column(u'archives_presenter', 'project_image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Presenter.project_docs'
        db.add_column(u'archives_presenter', 'project_docs',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'archives_project', (
            ('project_docs', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('video', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('informal_abstract', self.gf('django.db.models.fields.TextField')()),
            ('formal_abstract', self.gf('django.db.models.fields.TextField')()),
            ('project_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'archives', ['Project'])

        # Deleting field 'Presenter.formal_abstract'
        db.delete_column(u'archives_presenter', 'formal_abstract')

        # Deleting field 'Presenter.informal_abstract'
        db.delete_column(u'archives_presenter', 'informal_abstract')

        # Deleting field 'Presenter.video'
        db.delete_column(u'archives_presenter', 'video')

        # Deleting field 'Presenter.project_image'
        db.delete_column(u'archives_presenter', 'project_image')

        # Deleting field 'Presenter.project_docs'
        db.delete_column(u'archives_presenter', 'project_docs')


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