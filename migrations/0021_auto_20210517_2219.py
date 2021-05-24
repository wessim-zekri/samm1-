# Generated by Django 3.1.7 on 2021-05-17 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20210517_1355'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.AlterField(
            model_name='commande',
            name='date_livraison',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='demande',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.demande'),
        ),
    ]
