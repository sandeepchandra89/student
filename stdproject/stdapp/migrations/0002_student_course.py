# Generated by Django 5.0.4 on 2024-04-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stdapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
