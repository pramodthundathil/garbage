# Generated by Django 5.0.6 on 2024-12-29 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_alter_garbagecollectionrequests_garbage_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='garbagecollectionrequests',
            name='collection_status',
            field=models.BooleanField(default=False),
        ),
    ]
