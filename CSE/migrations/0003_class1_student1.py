# Generated by Django 4.2.7 on 2023-11-25 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0002_rename_sudent_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='ram', max_length=30)),
                ('last_name', models.CharField(default='kumar', max_length=30)),
                ('email', models.EmailField(default='ram@gmail.com', max_length=254, unique=True)),
                ('date_of_birth', models.DateField()),
                ('usn', models.CharField(max_length=20, unique=True)),
                ('department', models.CharField(max_length=50)),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('total_marks', models.IntegerField()),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='CSE.class1')),
            ],
        ),
    ]
