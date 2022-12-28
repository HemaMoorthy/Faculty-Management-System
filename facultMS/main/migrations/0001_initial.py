# Generated by Django 4.0.3 on 2022-06-09 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptId', models.IntegerField()),
                ('name', models.CharField(max_length=10)),
                ('fname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subId', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.dept')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facId', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('experience', models.IntegerField(max_length=100)),
                ('salary', models.FloatField()),
                ('dept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.dept')),
                ('subjects', models.ManyToManyField(to='main.subject')),
            ],
        ),
    ]
