# Generated by Django 4.0.5 on 2022-08-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MM', '0007_remove_account_gr_remove_account_invoice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='name',
            field=models.CharField(default='GD00', max_length=4),
            preserve_default=False,
        ),
    ]