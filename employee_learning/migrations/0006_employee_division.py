# Generated by Django 5.1.3 on 2024-11-14 10:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_learning', '0005_employee_reg_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='division',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee_learning.division'),
            preserve_default=False,
        ),
    ]
