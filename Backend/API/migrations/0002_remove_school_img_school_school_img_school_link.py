# Generated by Django 4.0.4 on 2022-09-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='img_school',
        ),
        migrations.AddField(
            model_name='school',
            name='img_school_link',
            field=models.CharField(default='hey', max_length=1000),
            preserve_default=False,
        ),
    ]
