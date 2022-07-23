# Generated by Django 4.0.5 on 2022-07-23 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_custom_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='age',
            field=models.PositiveIntegerField(blank=True, verbose_name='Yoshi'),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'Male (Erkak)'), (2, 'Female (Ayol)')], verbose_name='Jinsi'),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ismi'),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='surname',
            field=models.CharField(blank=True, max_length=100, verbose_name='Familyasi'),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='token',
            field=models.CharField(default='f35da33a0cdf822150c5d444e909efac', max_length=500),
        ),
    ]
