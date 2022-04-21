# Generated by Django 4.0.3 on 2022-03-30 04:20

from django.db import migrations
import easy_thumbnails.fields
from unique_upload import unique_upload


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_historicaluser_new_email_user_new_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to=unique_upload),
        ),
    ]