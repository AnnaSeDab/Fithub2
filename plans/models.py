from django.db import models
from datetime import datetime, date

from merchandise.models import Product


class DayPlan(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    video_url = models.URLField(max_length=1024, null=True, blank=True)
    is_rest = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    available_from = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class PlanCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Plan Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class FitnessPlan(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=80)
    plan_category = models.ForeignKey('PlanCategory', null=True, blank=True, on_delete=models.SET_NULL)
    start_day = models.DateField(auto_now_add=True, auto_now=False, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    day_one = models.ForeignKey('DayPlan', related_name='dayone', null=True, blank=True, on_delete=models.SET_NULL)
    day_two = models.ForeignKey('DayPlan', related_name='daytwo', null=True, blank=True, on_delete=models.SET_NULL)
    day_three = models.ForeignKey('DayPlan', related_name='daythree', null=True, blank=True, on_delete=models.SET_NULL)
    day_four = models.ForeignKey('DayPlan', related_name='dayfour', null=True, blank=True, on_delete=models.SET_NULL)
    day_five = models.ForeignKey('DayPlan', related_name='dayfive', null=True, blank=True, on_delete=models.SET_NULL)
    day_six = models.ForeignKey('DayPlan', related_name='daysix', null=True, blank=True, on_delete=models.SET_NULL)
    day_seven = models.ForeignKey('DayPlan', related_name='dayseven', null=True, blank=True, on_delete=models.SET_NULL)
    day_eight = models.ForeignKey('DayPlan', related_name='dayeight', null=True, blank=True, on_delete=models.SET_NULL)
    day_nine = models.ForeignKey('DayPlan', related_name='daynine', null=True, blank=True, on_delete=models.SET_NULL)
    day_ten = models.ForeignKey('DayPlan', related_name='dayten', null=True, blank=True, on_delete=models.SET_NULL)
    day_eleven = models.ForeignKey('DayPlan', related_name='dayeleven', null=True, blank=True, on_delete=models.SET_NULL)
    day_twelve = models.ForeignKey('DayPlan', related_name='daytwelve', null=True, blank=True, on_delete=models.SET_NULL)
    day_thirteen = models.ForeignKey('DayPlan', related_name='daythirteen', null=True, blank=True, on_delete=models.SET_NULL)
    day_fourteen = models.ForeignKey('DayPlan', related_name='dayfourteen', null=True, blank=True, on_delete=models.SET_NULL)
    day_fifteen = models.ForeignKey('DayPlan', related_name='dayfifteen', null=True, blank=True, on_delete=models.SET_NULL)
    day_sixteen = models.ForeignKey('DayPlan', related_name='daysixteen', null=True, blank=True, on_delete=models.SET_NULL)
    day_seventeen = models.ForeignKey('DayPlan', related_name='dayseventeen', null=True, blank=True, on_delete=models.SET_NULL)
    day_eighteen = models.ForeignKey('DayPlan', related_name='dayeighteen', null=True, blank=True, on_delete=models.SET_NULL)
    day_nineteen = models.ForeignKey('DayPlan', related_name='daynineteen', null=True, blank=True, on_delete=models.SET_NULL)
    day_twenty = models.ForeignKey('DayPlan', related_name='daytwenty', null=True, blank=True, on_delete=models.SET_NULL)
    day_twentyone = models.ForeignKey('DayPlan', related_name='daytwentyone', null=True, blank=True, on_delete=models.SET_NULL)
    day_twentytwo = models.ForeignKey('DayPlan', related_name='daytwentytwo', null=True, blank=True, on_delete=models.SET_NULL)
    day_twentythree = models.ForeignKey('DayPlan', related_name='daytwentythree', null=True, blank=True, on_delete=models.SET_NULL)
    day_twentyfour = models.ForeignKey('DayPlan', related_name='daytwentyfour', null=True, blank=True, on_delete=models.SET_NULL)
    day_twentyfive = models.ForeignKey('DayPlan', related_name='daytwentyfive', null=True, blank=True, on_delete=models.SET_NULL)
    day_twentysix = models.ForeignKey('DayPlan', related_name='daytwentysix', null=True, blank=True, on_delete=models.SET_NULL)
    day_twentyseven = models.ForeignKey('DayPlan', related_name='daytwentyseven', null=True, blank=True, on_delete=models.SET_NULL)
    day_twentyeight = models.ForeignKey('DayPlan', related_name='daytwentyeight', null=True, blank=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name