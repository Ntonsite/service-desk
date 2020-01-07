from django.db import models


# Create your models here.
class Service(models.Model):
	service_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.service_name

class Request(models.Model):
	service_name = models.ForeignKey(Service, on_delete=models.CASCADE)
	request_name = models.CharField(max_length=200)
	data         = models.FileField(default='To be Added',upload_to='documents/')

	def __str__(self):
	    return self.request_name
	    filename = self.data.url