# Generated by Django 4.2.9 on 2024-01-12 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_app', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='test3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testing3', models.CharField(max_length=100)),
            ],
        ),
    ]
