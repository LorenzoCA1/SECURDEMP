from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Role(models.Model):
	name = models.CharField(max_length=15, blank=True)
	browse_search = models.BooleanField()
	borrow = models.BooleanField()
	review = models.BooleanField()
	add = models.BooleanField()
	edit = models.BooleanField()
	delete = models.BooleanField()
	add_instance = models.BooleanField()
	edit_instance = models.BooleanField()
	delete_instance = models.BooleanField()
	create_manager = models.BooleanField()
	view_logs = models.BooleanField()
	any_create = models.BooleanField()

	def __str__(self):
		"""String for representing the Model object."""
		return self.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default ='default.jpg',upload_to='profile_pics')
	IDnum = models.CharField(max_length=8, blank=True)
	Role = models.ForeignKey('Role' , on_delete=models.SET_NULL, null=True)
	SecurityQuestion = models.CharField(max_length=50, blank=True)
	SecurityAnswer = models.CharField(max_length=30, blank=True)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

class Activity(models.Model):
    action_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=256)
    content = models.CharField(max_length=256)