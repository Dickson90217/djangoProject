# Generated by Django 4.0.3 on 2022-03-29 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_helpreal_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptreal',
            name='picture',
            field=models.ImageField(upload_to='static/picture'),
        ),
    ]
