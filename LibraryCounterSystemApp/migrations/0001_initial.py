# Generated by Django 3.2.6 on 2021-08-25 11:21

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StudentBatch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Unknown',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('entry', models.DateTimeField(auto_now_add=True)),
                ('exit', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default=False, max_length=50)),
                ('lname', models.CharField(default=False, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter', models.DateTimeField(auto_now_add=True)),
                ('exit', models.DateTimeField(auto_now_add=True)),
                ('std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryCounterSystemApp.student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentSemester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryCounterSystemApp.semester')),
                ('std', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryCounterSystemApp.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='bid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryCounterSystemApp.studentbatch'),
        ),
    ]
