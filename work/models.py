from django.db import models
from django.contrib.auth.models import User

class GarbageCollectionRequests(models.Model):
    request_date = models.DateField(auto_now_add=True)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requested")
    updated_staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name="handled", null=True, blank=True)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="collected", null=True, blank=True)
    updated_date = models.DateField(auto_now=True)
    collected_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    collection_status = models.BooleanField(default=False)
    garbage_status = models.CharField(max_length=255,default="pending",choices=(('collected', 'Collected'),('recycled', 'Recycled'),('disposed', 'disposed'),('pending', 'Pending'),('in_progress', 'In Progress'),('not_collected', 'Not Collected'), ("driver assigned","Driver assigned")))
    collection_date_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return f"Request from {self.requested_by.first_name} on {self.request_date}"
    


class Garbages(models.Model):
    GARBAGE_CHOICES = [
        ('plastic', 'Plastic'),
        ('organic', 'Organic'),
        ('metal', 'Metal'),
        ('glass', 'Glass'),
        ('paper', 'Paper'),
        ('electronic', 'Electronic'),
        ('other', 'Other'),
    ]

    request = models.ForeignKey(
        'GarbageCollectionRequests',
        on_delete=models.CASCADE,
        related_name="garbage_request"
    )
    garbage_item = models.CharField(
        max_length=50,
        choices=GARBAGE_CHOICES,
        verbose_name="Type of Garbage"
    )
    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Weight of Garbage (kg)"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description (optional)",
        help_text="Add any additional details about the garbage."
    )


    def __str__(self):
        return f"{self.garbage_item} - {self.weight} kg"

    class Meta:
        verbose_name = "Garbage"
        verbose_name_plural = "Garbages"



class GarbageVault(models.Model):
    vault_name = models.CharField(max_length=200)
    garbage_category = models.CharField(max_length=255)
    total_weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Weight of Garbage (kg)",
        default=0
    )

