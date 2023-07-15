from django.db import models
from django.contrib.auth.models import User
# imports neeeded for signals to work
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

# add user profile model to attach info for users profile
# user can only use one profile
class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    # taken user models that are needed for profiles and add default before each
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    # return username string
    def __str__(self):
        return self.user.username
# receiver to save user profiles details to file
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()