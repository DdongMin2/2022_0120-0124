# Generated by Django 2.2.5 on 2022-01-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirdapp', '0002_auto_20220118_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('age', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'animal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.AutoField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=14, null=True)),
                ('loc', models.CharField(max_length=13, null=True)),
            ],
            options={
                'db_table': 'dept',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=10, null=True)),
                ('job', models.CharField(max_length=9, null=True)),
                ('mgr', models.IntegerField(null=True)),
                ('hiredate', models.DateTimeField(null=True)),
                ('sal', models.IntegerField(null=True)),
                ('comm', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'emp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'owner',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('tel', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'playground',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_nm', models.CharField(max_length=50, null=True)),
                ('period', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'warranty',
                'managed': False,
            },
        ),
    ]
