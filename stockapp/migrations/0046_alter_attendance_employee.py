# Generated by Django 4.0.6 on 2022-09-03 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0045_remove_employee_no_of_absent_days_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attende', to='stockapp.employee'),
        ),
    ]