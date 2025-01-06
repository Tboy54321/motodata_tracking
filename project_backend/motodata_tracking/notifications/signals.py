from django.db.models.signals import post_save
from django.dispatch import receiver
from vehicles.models import Vehicle, Tasks
from .models import Notification

@receiver(post_save, sender=Vehicle)
def create_job_update_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            customer=instance.owner,
            vehicle=instance,
            title=f"Vehicle Created: {instance.make} {instance.model}",
            message=f"""
            Dear {instance.owner},

            We’re excited to inform you that a new job has been created for your vehicle. Here are the details:

            Job ID: [Unique Job ID, e.g., JOB12345]
            Vehicle: {instance.make} {instance.model},
            Service Type: [e.g., Engine Diagnosis & Repair]
            Service Advisor: [Advisor Name]
            Start Date: {instance.created_at}
            Estimated Completion Date: [e.g., January 10, 2025]
            We’ll keep you updated as the job progresses and notify you once the service is complete.

            If you have any questions, please don’t hesitate to reach out:

            Service Advisor Contact: [Phone Number or Email]
            Thank you for trusting us with your vehicle!

            Best regards.
            """,
            notification_type="General Information",
        )
    elif 'status' in instance.__dict__:
        Notification.objects.create(
            customer=instance.owner,
            vehicle=instance,
            title=f"Update on your Vehicle - Repair in Progress",
            message=f"""
            Dear {instance.owner},
            
            We are writing to update you on the status of your vehicle, [{instance.make}] {instance.model}].
            
            Current Status: {instance.status}
            
            Our technician, is currently working on your vehicle. We'll notify you as soon as there are further updates or when the service is completed.
            
            If you have any question, please feel free to contact:

            Service Adviser:
            Phone Number:
            Email:

            Best Regards
            """,
            notification_type="Job Update",
        )
    print('Notification created')
