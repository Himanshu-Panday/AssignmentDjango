import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal receiver function
@receiver(post_save, sender=User)
def slow_signal_receiver(sender, instance, **kwargs):
    print("Signal received. Starting a slow task...")
    time.sleep(5)  # Simulating a long-running task
    print("Signal processing completed.")

# Simulate saving a user instance
print("Saving user...")
user = User(username="test_user")
user.save()
print("User save method completed.")
