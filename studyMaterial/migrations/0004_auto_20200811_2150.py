# Generated by Django 3.0.8 on 2020-08-11 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studyMaterial', '0003_auto_20200801_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pre_q_paper',
            name='Subjects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='studyMaterial.Subject'),
        ),
    ]
