# Generated by Django 3.2.4 on 2021-06-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Image',
            field=models.ImageField(default=True, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='Email_id',
            field=models.EmailField(max_length=254),
        ),
    ]
