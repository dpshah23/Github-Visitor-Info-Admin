# Generated by Django 4.2.7 on 2024-08-02 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users_main',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('password', models.CharField(max_length=120)),
                ('unique_link', models.CharField(max_length=255, unique=True)),
                ('github_username', models.CharField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
            ],
            options={
                'db_table': 'Users_main',
            },
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unique_link', models.CharField(max_length=200)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Visits',
            },
        ),
    ]
