# Generated by Django 3.0.8 on 2020-08-01 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(choices=[('First Year', 'First Year'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Mechanical Sandwitch Engineering', 'Mechanical Sandwitch Engineering'), ('Electronics And Telecommunication Engineering', 'Electronics And Telecommunication Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Computer Engineering', 'Computer Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Instrumentation Engineering', 'Instrumentation Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Information Technology Engineering', 'Information Technology Engineering')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Universitie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('universitie', models.CharField(choices=[('Savitribai Phule Pune Universities', 'Savitribai Phule Pune Universities'), ('Gate', 'Gate'), ('Indian Engineering Services', 'Indian Engineering Services')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Fourth Year', 'Fourth Year')], max_length=100)),
                ('patterns', models.CharField(choices=[('2015', '2015'), ('2019', '2019')], max_length=50)),
                ('Sem', models.CharField(choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2'), ('Semester 3', 'Semester 3'), ('Semester 4', 'Semester 4'), ('Semester 5', 'Semester 5'), ('Semester 6', 'Semester 6'), ('Semester 7', 'Semester 7'), ('Semester 8', 'Semester 8')], max_length=50)),
                ('Subjects', models.CharField(max_length=100)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyMaterial.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Pre_Q_Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('Winter', 'Winter'), ('Summer', 'Summer')], max_length=50)),
                ('papers', models.FileField(upload_to='Previous/')),
                ('Subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyMaterial.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Indian_Engineering_Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Years', models.CharField(choices=[('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019')], max_length=50)),
                ('Subjects', models.CharField(max_length=30)),
                ('papers', models.FileField(upload_to='Indian_Engineering_Services/')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyMaterial.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Years', models.CharField(choices=[('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019')], max_length=50)),
                ('Subjects', models.CharField(max_length=30)),
                ('papers', models.FileField(upload_to='Competative/')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyMaterial.Department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='universities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studyMaterial.Universitie'),
        ),
    ]
