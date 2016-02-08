# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-02-06 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Yoins', '0005_auto_20160205_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=32)),
                ('admin_email', models.CharField(max_length=96)),
                ('email_password', models.CharField(max_length=255)),
                ('admin_pass', models.CharField(max_length=40)),
                ('admin_group', models.CharField(max_length=32)),
                ('access', models.CharField(max_length=10000)),
                ('modi_time', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customers_id', models.AutoField(primary_key=True, serialize=False)),
                ('customers_gender', models.CharField(max_length=1)),
                ('customers_nickname', models.CharField(max_length=255)),
                ('customers_firstname', models.CharField(max_length=32)),
                ('customers_lastname', models.CharField(max_length=32)),
                ('customers_points', models.IntegerField()),
                ('customers_affiliate_points', models.IntegerField()),
                ('affiliate_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customers_avatars', models.CharField(max_length=255)),
                ('customers_credit', models.IntegerField()),
                ('customers_dob', models.DateTimeField()),
                ('customers_email_address', models.CharField(max_length=96)),
                ('customers_default_address_id', models.IntegerField(blank=True, null=True)),
                ('customers_telephone', models.CharField(max_length=32)),
                ('customers_fax', models.CharField(blank=True, max_length=32, null=True)),
                ('customers_password', models.CharField(max_length=40)),
                ('customers_newsletter', models.CharField(blank=True, max_length=1, null=True)),
                ('customers_paypal_payerid', models.CharField(blank=True, max_length=20, null=True)),
                ('customers_paypal_ec', models.IntegerField()),
                ('customers_ip_address', models.CharField(blank=True, max_length=50, null=True)),
                ('customers_locked', models.IntegerField()),
                ('customers_paypal_payerids', models.CharField(blank=True, max_length=255, null=True)),
                ('customers_is_registerd', models.IntegerField()),
                ('customers_to_affiliate_status', models.IntegerField()),
                ('affiliate_code', models.CharField(max_length=20)),
                ('customers_affiliate_level', models.IntegerField()),
                ('super_affiliate_rate', models.IntegerField()),
                ('customers_confirm_email', models.IntegerField()),
                ('affiliate_email', models.CharField(blank=True, max_length=96, null=True)),
                ('send_affiliate_group_mail', models.IntegerField()),
                ('affiliate_site', models.CharField(blank=True, max_length=255, null=True)),
                ('affiliate_blog', models.CharField(blank=True, max_length=255, null=True)),
                ('affiliate_referral_place', models.CharField(blank=True, max_length=255, null=True)),
                ('affiliate_remarks', models.TextField(blank=True, null=True)),
                ('apply_affiliater_date', models.DateTimeField()),
                ('apply_affiliater_success_date', models.DateTimeField()),
                ('is_dropship', models.IntegerField()),
                ('dropshipper_level', models.IntegerField()),
                ('is_wholesale', models.IntegerField()),
                ('wholesale_level', models.IntegerField()),
                ('auto_register', models.IntegerField()),
                ('assign_admin_id', models.IntegerField()),
                ('fb_id', models.BigIntegerField()),
                ('twitter_id', models.BigIntegerField()),
                ('countries', models.CharField(blank=True, max_length=10, null=True)),
                ('pp_billing_agreement_id', models.CharField(max_length=255)),
                ('privileged', models.IntegerField()),
                ('google_id', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
                'db_table': 'customers',
            },
        ),
        migrations.AlterModelOptions(
            name='categories',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='ecategoryfilter',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'managed': False},
        ),
    ]