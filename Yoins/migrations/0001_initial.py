# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-02-05 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categories_id', models.AutoField(primary_key=True, serialize=False)),
                ('categories_image', models.CharField(blank=True, max_length=64, null=True)),
                ('parent_id', models.IntegerField()),
                ('sellercube_categories_id', models.IntegerField()),
                ('sellercube_parent_id', models.IntegerField()),
                ('sort_order', models.IntegerField(blank=True, null=True)),
                ('batch_price_disable', models.IntegerField()),
                ('categories_featured', models.IntegerField(blank=True, null=True)),
                ('categories_status', models.IntegerField(blank=True, null=True)),
                ('categories_disable_ups', models.IntegerField(blank=True, null=True)),
                ('categories_disable_usps', models.IntegerField(blank=True, null=True)),
                ('categories_free_shipping', models.CharField(blank=True, max_length=1, null=True)),
                ('categories_featured_until', models.DateField(blank=True, null=True)),
                ('categories_no_products_show', models.CharField(max_length=1)),
                ('categories_is_nofollow', models.CharField(max_length=1)),
                ('date_added', models.DateTimeField(blank=True, null=True)),
                ('products_list_grid_image_width', models.SmallIntegerField(blank=True, null=True)),
                ('products_list_grid_image_height', models.SmallIntegerField(blank=True, null=True)),
                ('products_grid_image_width', models.SmallIntegerField(blank=True, null=True)),
                ('products_grid_image_height', models.SmallIntegerField(blank=True, null=True)),
                ('products_gallery_image_width', models.SmallIntegerField(blank=True, null=True)),
                ('products_gallery_image_height', models.SmallIntegerField(blank=True, null=True)),
                ('products_view_image_width', models.SmallIntegerField(blank=True, null=True)),
                ('products_view_image_height', models.SmallIntegerField(blank=True, null=True)),
                ('products_items_image_width', models.SmallIntegerField(blank=True, null=True)),
                ('products_items_image_height', models.SmallIntegerField(blank=True, null=True)),
                ('last_modified', models.DateTimeField(blank=True, null=True)),
                ('admin_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ECategoryFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_id', models.IntegerField()),
                ('parent_filter_id', models.IntegerField()),
                ('categories_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('sort_order', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'e_category_filter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('products_id', models.AutoField(primary_key=True, serialize=False)),
                ('products_quantity', models.IntegerField()),
                ('products_model', models.CharField(blank=True, max_length=255, null=True)),
                ('products_image', models.CharField(blank=True, max_length=100, null=True)),
                ('products_image_2', models.CharField(blank=True, max_length=100, null=True)),
                ('products_image_3', models.CharField(blank=True, max_length=100, null=True)),
                ('new_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_usa_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_uk_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_de_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_au_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_cost_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_usa_low_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_uk_low_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('group_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_batch', models.IntegerField()),
                ('products_date_added', models.DateTimeField()),
                ('products_last_modified', models.DateTimeField(blank=True, null=True)),
                ('products_date_available', models.DateTimeField(blank=True, null=True)),
                ('products_featured_until', models.DateField(blank=True, null=True)),
                ('products_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('products_status', models.IntegerField()),
                ('clear_stock', models.IntegerField()),
                ('isfactorystock', models.IntegerField(db_column='IsFactoryStock')),
                ('isshowsubtitle', models.IntegerField(db_column='IsShowSubTitle')),
                ('products_featured', models.IntegerField(blank=True, null=True)),
                ('products_tax_class_id', models.IntegerField()),
                ('manufacturers_id', models.IntegerField(blank=True, null=True)),
                ('products_ordered', models.IntegerField()),
                ('products_qty_blocks', models.IntegerField()),
                ('products_price1', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_price2', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_price3', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_price4', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_price5', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_price6', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_price7', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_price8', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_price1_qty', models.IntegerField()),
                ('products_price2_qty', models.IntegerField()),
                ('products_price3_qty', models.IntegerField()),
                ('products_price4_qty', models.IntegerField()),
                ('products_price5_qty', models.IntegerField()),
                ('products_price6_qty', models.IntegerField()),
                ('products_price7_qty', models.IntegerField()),
                ('products_price8_qty', models.IntegerField()),
                ('products_sale_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_purchase_price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('products_image_4', models.CharField(blank=True, max_length=100, null=True)),
                ('products_image_5', models.CharField(blank=True, max_length=100, null=True)),
                ('products_image_6', models.CharField(blank=True, max_length=100, null=True)),
                ('products_image_7', models.CharField(blank=True, max_length=100, null=True)),
                ('products_image_8', models.CharField(blank=True, max_length=100, null=True)),
                ('products_length', models.DecimalField(decimal_places=2, max_digits=6)),
                ('products_width', models.DecimalField(decimal_places=2, max_digits=6)),
                ('products_height', models.DecimalField(decimal_places=2, max_digits=6)),
                ('products_ready_to_ship', models.IntegerField()),
                ('products_disable_ups', models.IntegerField(blank=True, null=True)),
                ('products_enable_usps', models.IntegerField(blank=True, null=True)),
                ('products_free_shipping', models.CharField(blank=True, max_length=1, null=True)),
                ('admin_id', models.IntegerField(blank=True, null=True)),
                ('products_image_9', models.CharField(blank=True, max_length=100, null=True)),
                ('products_image_10', models.CharField(blank=True, max_length=100, null=True)),
                ('products_image_11', models.CharField(blank=True, max_length=100, null=True)),
                ('products_image_12', models.CharField(blank=True, max_length=100, null=True)),
                ('products_video', models.CharField(blank=True, max_length=255, null=True)),
                ('products_ga_keywords', models.TextField(blank=True, null=True)),
                ('products_bulk', models.CharField(max_length=10)),
                ('px_id', models.IntegerField()),
                ('supply_type', models.IntegerField(blank=True, null=True)),
                ('oa_px_id', models.IntegerField()),
                ('sj_id', models.IntegerField()),
                ('oa_sj_id', models.IntegerField()),
                ('deliver_type', models.IntegerField()),
                ('booking_time', models.DateTimeField()),
                ('book_end_time', models.DateTimeField()),
                ('is_snamup', models.IntegerField()),
                ('show_size', models.IntegerField()),
                ('show_new_arrival', models.IntegerField()),
                ('oa_kf_id', models.IntegerField()),
                ('oa_ms_id', models.IntegerField()),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
    ]
