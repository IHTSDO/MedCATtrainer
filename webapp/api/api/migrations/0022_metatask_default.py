# Generated by Django 2.2.9 on 2020-01-24 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20200124_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='metatask',
            name='default',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='task_default', to='api.MetaTaskValue'),
        ),
    ]
