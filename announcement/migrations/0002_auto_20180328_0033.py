# Generated by Django 2.0.3 on 2018-03-27 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='sheets',
            field=models.CharField(blank=True, default='0', max_length=1000, null=True),
        ),
    ]
