import jdatetime
from django.db import models
from django.db.models import Avg
from uuid import uuid4

from accounts.models import CustomUser


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    uuid = models.UUIDField(default=uuid4, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='vendor',
                                unique=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='vendors')
    is_active = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='vendors/logo')
    profile_image = models.ImageField(upload_to='vendors/profile')
    is_new = models.BooleanField(default=True)
    delivery = models.PositiveIntegerField(default=0, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class VendorAddress(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='addresses')
    address_line1 = models.CharField(max_length=70)
    address_line2 = models.CharField(max_length=50, null=True, blank=True)
    post_code = models.CharField(max_length=10, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address_line1


class WorkTime(models.Model):
    SATURDAY = 5
    SUNDAY = 6
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    WEEK_DAYS = (
        (SATURDAY, 'شنبه' ),
        (SUNDAY, 'یکشنبه'),
        (MONDAY, 'دوشنبه'),
        (TUESDAY, 'سه شنبه'),
        (WEDNESDAY, ' چهارشنبه'),
        (THURSDAY, 'پنجشنبه'),
        (FRIDAY, 'جمعه')
    )
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='open_times')
    day = models.PositiveSmallIntegerField(choices=WEEK_DAYS)
    open_morning = models.CharField(max_length=8)
    close_morning = models.CharField(max_length=8)
    open_afternoon = models.CharField(max_length=8)
    close_afternoon = models.CharField(max_length=8)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('vendor', 'day')

    def __str__(self):
        return f'{self.vendor.name} - {self.day} - {self.open_morning} - {self.close_morning} '

    def check_open(self):
        time = jdatetime.datetime.now().strftime("%H:%M")
        time_str = time.replace(':', '')
        open_morning = self.open_morning.replace(':', '')
        close_morning = self.close_morning.replace(':', '')
        open_afternoon = self.open_afternoon.replace(':', '')
        close_afternoon = self.close_afternoon.replace(':', '')
        if 0 < int(time_str) <= 1530:
            return int(open_morning) <= int(time_str) <= int(close_morning)
        elif 1530 <= int(time_str) <= 2359:
            return int(open_afternoon) <= int(time_str) <= int(close_afternoon)

    def hour_opening(self):
        time = jdatetime.datetime.now().strftime("%H:%M")
        time_str = time.replace(':', '')
        open_morning = self.open_morning.replace(':', '')
        open_afternoon = self.close_afternoon.replace(':', '')
        close_afternoon = self.close_afternoon.replace(':', '')
        if int(time_str) < int(open_morning):
            return self.open_morning
        elif int(time_str) < int(open_afternoon):
            return self.open_afternoon
        elif int(time_str) > int(close_afternoon):
            return False


class City(models.Model):
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Rating(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='rating')
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rating')
    rate = models.FloatField(default=0)

    @classmethod
    def rate_average(cls, vendor):
        vendors_rating = cls.objects.filter(vendor_id=vendor).aggregate(Avg('rate'))
        return vendors_rating


