# Generated by Django 3.0.2 on 2020-03-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200324_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finedata',
            name='d',
        ),
        migrations.AddField(
            model_name='finedata',
            name='image',
            field=models.ImageField(default=2131, upload_to='numberplates_images'),
            preserve_default=False,
        ),
    ]
