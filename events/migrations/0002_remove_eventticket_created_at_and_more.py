# Generated by Django 5.1.6 on 2025-02-16 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventticket',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='eventticket',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='tickettype',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tickettype',
            name='updated_at',
        ),
    ]
