from django.db import models
import ipaddress

class IPBlock(models.Model):
	ip_address = models.GenericIPAddressField(null=True,blank=True)
	ip_range = models.CharField(max_length=100,null=True,blank=True)
	def save(self, *args, **kwargs):
		if self.ip_range:
			# Normalize the CIDR notation to ensure it is valid
			cidr_ip = ipaddress.ip_network(self.ip_range, strict=False)
			self.ip_range = str(cidr_ip)
		super(IPBlock, self).save(*args, **kwargs)
# from django.utils.translation import ugettext_lazy as _


# class UserManager(BaseUserManager):
#     """Define a model manager for User model with no username field."""

#     def _create_user(self, email, password=None, **extra_fields):
#         """Create and save a User with the given email and password."""
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)

#     def create_superuser(self, email, password=None, **extra_fields):
#         """Create and save a SuperUser with the given email and password."""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self._create_user(email, password, **extra_fields)


# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name','last_name']
#     @property
#     def full_name(self):
#         return self.first_name + " " + self.last_name
#     def __str__(self):
#         if not self.last_name:
#             return self.first_name	
#         return self.first_name + " " + self.last_name

#     objects = UserManager()
