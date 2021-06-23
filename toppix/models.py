from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Category(models.Model):
	name = models.CharField(max_length=50)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class SubCategory(models.Model):
	category  = models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL)
	name  = models.CharField(max_length=100)
	active = models.BooleanField(default=True)


	def __str__(self):
		return self.name

class Tags(models.Model):
	name = models.CharField(max_length=20)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Tag"
	

TOPPIX_IMAGE_CHOICE = [

					('image','image'),
					('video','video'),
					('pdf','pdf'),
					('gif','gif')
]


class Toppix(models.Model):
	title = models.CharField(max_length=200)
	user =  models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
	category = models.ForeignKey(Category,null=True,blank=True,on_delete=models.SET_NULL)
	sub_category = models.ForeignKey(SubCategory,null=True,blank=True,on_delete=models.SET_NULL)
	tag = models.ManyToManyField(Tags)
	min_price = models.PositiveIntegerField(default=0)
	max_price = models.PositiveIntegerField(default=0)
	discount_percentage = models.IntegerField(default=0)
	like = models.PositiveIntegerField(default=0)
	toppix_type = models.CharField(max_length = 20,choices = TOPPIX_IMAGE_CHOICE,default = 'image')
	shares = models.PositiveIntegerField(default=0)
	views = models.PositiveIntegerField(default=0)
	downloads = models.PositiveIntegerField(default=0)
	file = models.FileField(upload_to='uploads/%Y/%m/%d/',null=True,blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(null=True,blank=True)


	def __str__(self):
		return self.title


	