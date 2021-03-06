from django.db import models

class Presenter(models.Model):
	first_name = models.CharField(max_length=200,default="")
	last_name = models.CharField(max_length=200,default="")
	nickname = models.CharField(max_length=200, default="")
	major = models.CharField(max_length=200,default="")
	grad_year = models.IntegerField(default=0)
	project_title = models.CharField(max_length=200, blank=True, null=True)
	profile_image = models.ImageField(upload_to="profile_images", blank=True, null=True)
	formal_abstract = models.TextField(blank=True, null=True)
	informal_abstract = models.TextField(blank=True, null=True)
	video = models.CharField(max_length=200, blank=True, null=True)
	project_image = models.ImageField(upload_to="project_images", blank=True, null=True)
	project_docs = models.ImageField(upload_to="project_docs", blank=True, null=True)

	def url_name(self):
		return "%s_%s" % (self.first_name.lower().strip(), self.last_name.lower().strip())

	def __unicode__(self):
		return "%s %s" % (self.first_name, self.last_name)

	def save(self, *args, **kwargs):
		if self.nickname == "":
			self.nickname = self.url_name()
		super(Presenter, self).save(*args, **kwargs)
