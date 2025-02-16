import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal receiver function
@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")

# Function to simulate saving a user
def save_user():
    print(f"Saving user in thread: {threading.current_thread().name}")
    user = User(username="test_user")
    user.save()

# Run the function
save_user()
