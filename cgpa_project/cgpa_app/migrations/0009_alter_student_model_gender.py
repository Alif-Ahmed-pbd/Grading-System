# Generated by Django 5.0.1 on 2024-02-04 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cgpa_app', '0008_alter_student_model_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_model',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], max_length=30, null=True),
        ),
    ]
