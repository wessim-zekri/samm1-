# Generated by Django 3.1.7 on 2021-05-02 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210502_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demande',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]