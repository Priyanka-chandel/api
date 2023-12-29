# Generated by Django 4.2.8 on 2023-12-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='type',
            field=models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobile phones', 'Mobile phones'), ('Business company', 'Business company')], max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Software Developer', 'Software Developer'), ('Project Leader', 'Project Leader')], max_length=100),
        ),
    ]
