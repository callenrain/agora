from django.db import models

class Presenter(models.Model):
	name = models.CharField(max_length=200)
	major = models.CharField(max_length=200)
	grad_year = models.IntegerField(default=0)
	#project = models.ForeignKey(Project, blank=True, null=True)
	profile_image = models.ImageField(upload_to="profile_images", blank=True, null=True)
	formal_abstract = models.TextField(blank=True, null=True)
	informal_abstract = models.TextField(blank=True, null=True)
	video = models.URLField(blank=True, null=True)
	project_image = models.ImageField(upload_to="project_images", blank=True, null=True)
	project_docs = models.ImageField(upload_to="project_docs", blank=True, null=True)

