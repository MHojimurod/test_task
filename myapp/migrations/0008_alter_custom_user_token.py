# Generated by Django 4.0.6 on 2022-07-24 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_custom_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='token',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
