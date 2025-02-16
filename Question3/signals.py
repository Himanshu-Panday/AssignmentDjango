from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal receiver function
@receiver(post_save, sender=User)
def signal_receiver(sender, instance, **kwargs):
    print("Signal received! Checking if data is in DB...")
    
    # Check if user exists in the database
    user_exists = User.objects.filter(username=instance.username).exists()
    
    if user_exists:
        print("User exists in DB at the time of signal execution.")
    else:
        print("User does NOT exist in DB at the time of signal execution!")

# Function to test transaction rollback
def test_transaction():
    try:
        with transaction.atomic():  # Start a transaction block
            user = User.objects.create(username="test_user")
            print("User created in transaction.")
            raise Exception("Forcing rollback")  # Force a rollback
    except Exception as e:
        print(f"Transaction rolled back: {e}")

# Run the test
test_transaction()
