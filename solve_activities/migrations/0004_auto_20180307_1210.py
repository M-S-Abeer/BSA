# Generated by Django 2.0.2 on 2018-03-07 06:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problems', '0008_auto_20180306_2339'),
        ('solve_activities', '0003_solve_creation_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solve',
            old_name='creation_date',
            new_name='solved_at',
        ),
        migrations.AlterUniqueTogether(
            name='solve',
            unique_together={('solver', 'problem')},
        ),
    ]
