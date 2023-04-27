from django.db import models

# Create your models here.

class activity_report(models.Model):
	reporter_name = models.CharField(max_length=100,null=True,blank=True)
	reporter_email = models.EmailField(null=True,blank=True)
	reporter_phone = models.CharField(max_length=100,null=True,blank=True)
	reporter_address = models.CharField(max_length=100,null=True,blank=True)
	
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	date = models.DateField()
	time = models.TimeField()
	
	image = models.ImageField(upload_to="images",blank=True)
	video = models.FileField(upload_to="videos",blank=True)
	
	save_date_time = models.DateTimeField(auto_now_add=True)

	false_alarm = models.BooleanField(default=False)

	invistigated = models.BooleanField(default=False)
	
	def save(self,*args,**kwargs):
		super(activity_report,self).save(*args,**kwargs)

	def __str__(self):
		return self.name

class person_report(models.Model):
	reporter_name = models.CharField(max_length=100,null=True,blank=True)
	reporter_email = models.EmailField(null=True,blank=True)
	reporter_phone = models.CharField(max_length=100,null=True,blank=True)
	reporter_address = models.CharField(max_length=100,null=True,blank=True)
	
	name = models.CharField(max_length=100,null=True,blank=True)
	description = models.CharField(max_length=10000)
	location = models.CharField(max_length=100,null=True,blank=True)
	date = models.DateField()
	time = models.TimeField()
	
	image = models.ImageField(upload_to="images",blank=True)
	video = models.FileField(upload_to="videos",blank=True)
	
	save_date_time = models.DateTimeField(auto_now_add=True)

	false_alarm = models.BooleanField(default=False)

	invistigated = models.BooleanField(default=False)

	def save(self,*args,**kwargs):
		super(person_report,self).save(*args,**kwargs)

	def __str__(self):
		return str(self.pk)

class wanted_list(models.Model):
	name = models.CharField(max_length=100)
	
	reported_by_name = models.CharField(max_length=100,null=True,blank=True)
	reported_by_phone = models.CharField(max_length=100,null=True,blank=True)
	reported_by_address = models.CharField(max_length=100,null=True,blank=True)
	hair_description = models.CharField(max_length=100,null=True,blank=True)
	height_description = models.CharField(max_length=100,null=True,blank=True)
	cloth_description = models.CharField(max_length=100,null=True,blank=True)
	caught_crime = models.CharField(max_length=100,null=True,blank=True)
	caught_location = models.CharField(max_length=100,null=True,blank=True)
	caught_date = models.DateField(null=True,blank=True)
	caught_time = models.TimeField(null=True,blank=True)
	save_date_time = models.DateTimeField(auto_now_add=True)

	def save(self,*args,**kwargs):
		super(wanted_list,self).save(*args,**kwargs)

	def __str__(self):
		return f'{self.name}'
