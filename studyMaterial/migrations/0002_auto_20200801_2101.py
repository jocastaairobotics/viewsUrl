# Generated by Django 3.0.8 on 2020-08-01 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyMaterial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pre_q_paper',
            name='Subjects',
            field=models.CharField(max_length=100),
        ),
    ]
