# Generated by Django 3.1.1 on 2021-04-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20210409_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
