# Generated by Django 4.0.5 on 2022-08-18 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MM', '0014_alter_vendor_companycode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='meterial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MM.materialitem'),
        ),
        migrations.AlterField(
            model_name='requisitionitem',
            name='meterial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MM.materialitem'),
        ),
    ]
