# Generated by Django 2.2.6 on 2019-10-15 01:48

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20191015_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='article/images'),
        ),
    ]
