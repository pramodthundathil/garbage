# Generated by Django 5.0.6 on 2024-12-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garbagecollectionrequests',
            name='garbage_status',
            field=models.CharField(choices=[('collected', 'Collected'), ('recycled', 'Recycled'), ('disposed', 'disposed'), ('pending', 'Pending'), ('in_progress', 'In Progress'), ('not_collected', 'Not Collected'), ('driver assigned', 'Driver assigned')], default='pending', max_length=255),
        ),
    ]
