# Generated by Django 3.2.21 on 2023-09-26 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merchandise', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField()),
                ('video_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('is_rest', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
                ('available_from', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Plan Categories',
            },
        ),
        migrations.CreateModel(
            name='FitnessPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('difficulty', models.CharField(max_length=80)),
                ('start_day', models.DateField(auto_now_add=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('day_eight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dayeight', to='plans.dayplan')),
                ('day_eighteen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dayeighteen', to='plans.dayplan')),
                ('day_eleven', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dayeleven', to='plans.dayplan')),
                ('day_fifteen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dayfifteen', to='plans.dayplan')),
                ('day_five', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dayfive', to='plans.dayplan')),
                ('day_four', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dayfour', to='plans.dayplan')),
                ('day_fourteen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dayfourteen', to='plans.dayplan')),
                ('day_nine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daynine', to='plans.dayplan')),
                ('day_nineteen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daynineteen', to='plans.dayplan')),
                ('day_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dayone', to='plans.dayplan')),
                ('day_seven', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dayseven', to='plans.dayplan')),
                ('day_seventeen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dayseventeen', to='plans.dayplan')),
                ('day_six', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daysix', to='plans.dayplan')),
                ('day_sixteen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daysixteen', to='plans.dayplan')),
                ('day_ten', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dayten', to='plans.dayplan')),
                ('day_thirteen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daythirteen', to='plans.dayplan')),
                ('day_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daythree', to='plans.dayplan')),
                ('day_twelve', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daytwelve', to='plans.dayplan')),
                ('day_twenty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daytwenty', to='plans.dayplan')),
                ('day_twentyeight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daytwentyeight', to='plans.dayplan')),
                ('day_twentyfive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daytwentyfive', to='plans.dayplan')),
                ('day_twentyfour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daytwentyfour', to='plans.dayplan')),
                ('day_twentyone', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daytwentyone', to='plans.dayplan')),
                ('day_twentyseven', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daytwentyseven', to='plans.dayplan')),
                ('day_twentysix', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daytwentysix', to='plans.dayplan')),
                ('day_twentythree', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daytwentythree', to='plans.dayplan')),
                ('day_twentytwo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daytwentytwo', to='plans.dayplan')),
                ('day_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='daytwo', to='plans.dayplan')),
                ('plan_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='plans.plancategory')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchandise.product')),
            ],
        ),
    ]