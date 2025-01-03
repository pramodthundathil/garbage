# Generated by Django 5.0.6 on 2024-12-28 16:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GarbageCollectionRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('collected_time', models.DateTimeField(blank=True, null=True)),
                ('garbage_status', models.CharField(choices=[('collected', 'Collected'), ('recycled', 'Recycled'), ('disposed', 'disposed'), ('pending', 'Pending'), ('in_progress', 'In Progress'), ('not_collected', 'Not Collected'), ('driver assigned', 'Driver assigned')], max_length=255)),
                ('collection_date_time', models.DateTimeField(blank=True, null=True)),
                ('visibility', models.BooleanField(default=True)),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collected', to=settings.AUTH_USER_MODEL)),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested', to=settings.AUTH_USER_MODEL)),
                ('updated_staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='handled', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Garbages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('garbage_item', models.CharField(choices=[('plastic', 'Plastic'), ('organic', 'Organic'), ('metal', 'Metal'), ('glass', 'Glass'), ('paper', 'Paper'), ('electronic', 'Electronic'), ('other', 'Other')], max_length=50, verbose_name='Type of Garbage')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Weight of Garbage (kg)')),
                ('description', models.TextField(blank=True, help_text='Add any additional details about the garbage.', null=True, verbose_name='Description (optional)')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='garbage_request', to='work.garbagecollectionrequests')),
            ],
            options={
                'verbose_name': 'Garbage',
                'verbose_name_plural': 'Garbages',
            },
        ),
    ]
