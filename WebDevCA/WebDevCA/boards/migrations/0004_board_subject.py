# Generated by Django 2.0.1 on 2018-02-15 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_topic_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='subject',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
