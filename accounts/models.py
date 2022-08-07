from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from PIL import Image
from django.conf import settings
from .import utils
from .managers import CustomUserManager

# Create your models here.

###############
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

from .managers import CustomUserManager

from . import utils

# Create your models here.

class CustomUser(AbstractUser):
    username = None 
    email = models.EmailField(unique=True)
    
    slug = models.SlugField(blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    class Meta:
        ordering = ["email"]
        verbose_name = "User"

    def __str__(self):
        return self.email 

    # Creating a default slug/username for users if blank.
    def gen_random_slug(self):
        random_slug = slugify(self.first_name + self.last_name + utils.generate_random_id())
        while CustomUser.objects.filter(slug=random_slug).exists():
            random_slug = slugify(self.first_name + self.last_name + utils.generate_random_id())
        return random_slug
        
    def save(self, *args, **kwargs):
        # Check for a slug        
        if not self.slug:
            # Create default slug
            self.slug = self.gen_random_slug()
        # Finally save.
        super().save(*args, **kwargs)

##############

class Profile(models.Model):
	user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	profile_img=models.ImageField(default="profile-images/avater.png")
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	department = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	bio=models.CharField(max_length=600)
	date_joined=models.DateTimeField(auto_now_add=True, blank=True,null=True)

	def __str__(self):
		return f"{self.user}"


