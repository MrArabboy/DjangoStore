# Generated by Django 3.1.3 on 2020-12-09 09:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=25)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=5)),
                ('total_in_shop', models.DecimalField(decimal_places=2, default=1, max_digits=5)),
                ('product_added_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('select_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('items', models.ManyToManyField(blank=True, to='products.Item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product'),
        ),
    ]
