# Generated by Django 2.1.3 on 2018-11-17 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cuzcobot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priceDate', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=16)),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickerSymbol', models.CharField(max_length=6, verbose_name='Security Ticker Symbol')),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cuzcobot.Security'),
        ),
    ]