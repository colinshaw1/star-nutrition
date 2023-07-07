from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem

# exectues the update_on_save method
@receiver(post_save, sender=OrderLineItem)
# fucniton to handle signals from post save event
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

# exectues the update_on_save method
@receiver(post_delete, sender=OrderLineItem)
# fucniton to handle signals from post save event
def update_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()