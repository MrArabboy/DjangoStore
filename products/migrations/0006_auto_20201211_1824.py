# Generated by Django 3.1.3 on 2020-12-11 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201211_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='store_name',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.store'),
        ),
    ]
