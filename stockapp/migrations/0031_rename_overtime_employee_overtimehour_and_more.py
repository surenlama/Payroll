# Generated by Django 4.0.5 on 2022-07-16 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0030_alter_employee_salary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='overtime',
            new_name='overtimehour',
        ),
        migrations.RemoveField(
            model_name='totalsalary',
            name='leaverate',
        ),
        migrations.RemoveField(
            model_name='totalsalary',
            name='overtimerate',
        ),
    ]