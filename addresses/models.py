from django.db import models

from billing.models import BillingProfile

ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping','Shipping'),
)
# Create your models here.

class Address(models.Model):
    billing_profile    = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_type       = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_line_1     = models.CharField(max_length=120)
    address_line_2     = models.CharField(max_length=120, null=True, blank=True)
    country            = models.CharField(max_length=120, default='VietNam')
    city               = models.CharField(max_length=120)
    district           = models.CharField(max_length=120)
    postal_code        = models.CharField(max_length=120)

    """docstring for ClassName"""
    def __str__(self):
        return str(self.billing_profile)
        