# Generated by Django 2.0.2 on 2018-03-15 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0008_auto_20180306_2339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='problem',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
