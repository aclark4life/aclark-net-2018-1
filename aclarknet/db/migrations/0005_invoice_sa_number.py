# Generated by Django 2.0.1 on 2018-02-06 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_invoice_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='sa_number',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Subcontractor Agreement Number'),
        ),
    ]
