# Generated by Django 2.0.5 on 2018-07-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0005_auto_20180725_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_schools',
            name='school_badge',
            field=models.FileField(default=True, help_text='upload a jpg, ping file', upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='reg_schools',
            name='short_video',
            field=models.FileField(default=True, help_text='upload a video file, mp4, ', upload_to='media/video'),
        ),
    ]
