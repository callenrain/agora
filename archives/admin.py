from django.contrib import admin
from archives.models import Presenter

class PresenterAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'major', 'grad_year', 'project_title')
	list_filter = ['grad_year', 'major']
	fieldsets = [
        ('Personal',               {'fields': ['first_name', 'last_name', 'major', 'grad_year']}),
        ('Project Information', {'fields': ['project_title', 'informal_abstract', 'formal_abstract']}),
        ('External Data', {'fields': ['project_docs', 'project_image', 'video', 'profile_image']}),
    ]

admin.site.register(Presenter, PresenterAdmin)