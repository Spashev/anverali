# Generated by Django 4.2.11 on 2024-04-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NamesMan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Man',
                'verbose_name_plural': 'Men',
            },
        ),
        migrations.CreateModel(
            name='NamesWoman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Woman',
                'verbose_name_plural': 'Women',
            },
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
