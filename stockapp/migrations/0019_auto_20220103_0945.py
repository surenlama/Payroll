# Generated by Django 3.2 on 2022-01-03 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0018_auto_20220103_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='added_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='added_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='update_on',
            field=models.DateTimeField(null=True),
        ),
    ]