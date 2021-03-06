# Generated by Django 2.1.3 on 2018-11-17 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cuzcobot', '0004_auto_20181116_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('submissionDate', models.DateTimeField(auto_now_add=True)),
                ('expirationDate', models.DateTimeField(blank=True, null=True)),
                ('cancelationDate', models.DateTimeField(blank=True, null=True)),
                ('failedDate', models.DateTimeField(blank=True, null=True)),
                ('exchange', models.CharField(max_length=15)),
                ('assetClass', models.CharField(choices=[('equity', 'E'), ('option', 'O'), ('future', 'F'), ('commodity', 'C')], max_length=1)),
                ('shares', models.IntegerField()),
                ('filledShares', models.IntegerField()),
                ('orderType', models.CharField(choices=[('Market Order', 'MKT'), ('Limit Order', 'LMT'), ('Stop Order', 'STP'), ('Stop Limit Order', 'SLT')], max_length=3)),
                ('orderDirection', models.CharField(choices=[('Buy', 'B'), ('Sell', 'S')], max_length=1)),
                ('timeInForce', models.CharField(choices=[('Day', 'D'), ('Good Till Canceled', 'G'), ('At Market Open', 'O'), ('Immediate or Cancel Partial', 'I'), ('Immediate or Cancel Full', 'F')], max_length=1)),
                ('limitPrice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('stopPrice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('filledAvgPrice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('orderStatus', models.CharField(choices=[('New', 'NEW'), ('Partial Fill', 'PAR'), ('Filled', 'FIL'), ('Done For Day', 'DFD'), ('Canceled', 'CAN'), ('Expired', 'EXP'), ('Accepted', 'ACP'), ('Pending At Exchange', 'PAE'), ('Pending Cancelation', 'PC'), ('Stopped', 'STP'), ('Rejected', 'RCT'), ('Suspended', 'SUS'), ('Calculated', 'CAL')], max_length=3)),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cuzcobot.Security')),
            ],
        ),
    ]
