from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        # Attempt to get the associated profile
        profile = instance.profile
    except Profile.DoesNotExist:
        # If the profile doesn't exist, create a new one
        profile = Profile(user=instance)

    # Save the profile
    profile.save()
