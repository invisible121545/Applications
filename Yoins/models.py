# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=32)
    admin_email = models.CharField(max_length=96)
    email_password = models.CharField(max_length=255,null=True)
    admin_pass = models.CharField(max_length=40)
    admin_group = models.CharField(max_length=32,null=True)
    access = models.CharField(max_length=10000,null=True)
    modi_time = models.IntegerField(null=True)

    class Meta:
        managed = True
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categories(models.Model):
    categories_id = models.AutoField(primary_key=True)
    categories_image = models.CharField(max_length=64, blank=True, null=True)
    parent_id = models.IntegerField()
    sellercube_categories_id = models.IntegerField()
    sellercube_parent_id = models.IntegerField()
    sort_order = models.IntegerField(blank=True, null=True)
    batch_price_disable = models.IntegerField()
    categories_featured = models.IntegerField(blank=True, null=True)
    categories_status = models.IntegerField(blank=True, null=True)
    categories_disable_ups = models.IntegerField(blank=True, null=True)
    categories_disable_usps = models.IntegerField(blank=True, null=True)
    categories_free_shipping = models.CharField(max_length=1, blank=True, null=True)
    categories_featured_until = models.DateField(blank=True, null=True)
    categories_no_products_show = models.CharField(max_length=1)
    categories_is_nofollow = models.CharField(max_length=1)
    date_added = models.DateTimeField(blank=True, null=True)
    products_list_grid_image_width = models.SmallIntegerField(blank=True, null=True)
    products_list_grid_image_height = models.SmallIntegerField(blank=True, null=True)
    products_grid_image_width = models.SmallIntegerField(blank=True, null=True)
    products_grid_image_height = models.SmallIntegerField(blank=True, null=True)
    products_gallery_image_width = models.SmallIntegerField(blank=True, null=True)
    products_gallery_image_height = models.SmallIntegerField(blank=True, null=True)
    products_view_image_width = models.SmallIntegerField(blank=True, null=True)
    products_view_image_height = models.SmallIntegerField(blank=True, null=True)
    products_items_image_width = models.SmallIntegerField(blank=True, null=True)
    products_items_image_height = models.SmallIntegerField(blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Customers(models.Model):
    customers_id = models.AutoField(primary_key=True)
    customers_gender = models.CharField(max_length=1)
    customers_nickname = models.CharField(max_length=255)
    customers_firstname = models.CharField(max_length=32)
    customers_lastname = models.CharField(max_length=32)
    customers_points = models.IntegerField()
    customers_affiliate_points = models.IntegerField()
    affiliate_amount = models.DecimalField(max_digits=10, decimal_places=2)
    customers_avatars = models.CharField(max_length=255)
    customers_credit = models.IntegerField()
    customers_dob = models.DateTimeField()
    customers_email_address = models.CharField(max_length=96)
    customers_default_address_id = models.IntegerField(blank=True, null=True)
    customers_telephone = models.CharField(max_length=32)
    customers_fax = models.CharField(max_length=32, blank=True, null=True)
    customers_password = models.CharField(max_length=40)
    customers_newsletter = models.CharField(max_length=1, blank=True, null=True)
    customers_paypal_payerid = models.CharField(max_length=20, blank=True, null=True)
    customers_paypal_ec = models.IntegerField()
    customers_ip_address = models.CharField(max_length=50, blank=True, null=True)
    customers_locked = models.IntegerField()
    customers_paypal_payerids = models.CharField(max_length=255, blank=True, null=True)
    customers_is_registerd = models.IntegerField()
    customers_to_affiliate_status = models.IntegerField()
    affiliate_code = models.CharField(max_length=20)
    customers_affiliate_level = models.IntegerField()
    super_affiliate_rate = models.IntegerField()
    customers_confirm_email = models.IntegerField()
    affiliate_email = models.CharField(max_length=96, blank=True, null=True)
    send_affiliate_group_mail = models.IntegerField()
    affiliate_site = models.CharField(max_length=255, blank=True, null=True)
    affiliate_blog = models.CharField(max_length=255, blank=True, null=True)
    affiliate_referral_place = models.CharField(max_length=255, blank=True, null=True)
    affiliate_remarks = models.TextField(blank=True, null=True)
    apply_affiliater_date = models.DateTimeField()
    apply_affiliater_success_date = models.DateTimeField()
    is_dropship = models.IntegerField()
    dropshipper_level = models.IntegerField()
    is_wholesale = models.IntegerField()
    wholesale_level = models.IntegerField()
    auto_register = models.IntegerField()
    assign_admin_id = models.IntegerField()
    fb_id = models.BigIntegerField()
    twitter_id = models.BigIntegerField()
    countries = models.CharField(max_length=10, blank=True, null=True)
    pp_billing_agreement_id = models.CharField(max_length=255)
    privileged = models.IntegerField()
    google_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'customers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ECategoryFilter(models.Model):
    filter_id = models.IntegerField()
    parent_filter_id = models.IntegerField()
    categories_id = models.IntegerField()
    name = models.CharField(max_length=50)
    sort_order = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'e_category_filter'


class Products(models.Model):
    products_id = models.AutoField(primary_key=True)
    products_quantity = models.IntegerField()
    products_model = models.CharField(max_length=255, blank=True, null=True)
    products_image = models.CharField(max_length=100, blank=True, null=True)
    new_price = models.DecimalField(max_digits=15, decimal_places=4)
    products_price = models.DecimalField(max_digits=15, decimal_places=4)
    group_price = models.DecimalField(max_digits=15, decimal_places=4)
    products_batch = models.IntegerField()
    products_date_added = models.DateTimeField()
    products_last_modified = models.DateTimeField(blank=True, null=True)
    products_date_available = models.DateTimeField(blank=True, null=True)
    products_featured_until = models.DateField(blank=True, null=True)
    products_weight = models.DecimalField(max_digits=10, decimal_places=2)
    products_status = models.IntegerField()
    clear_stock = models.IntegerField()
    isfactorystock = models.IntegerField(db_column='IsFactoryStock')  # Field name made lowercase.
    isshowsubtitle = models.IntegerField(db_column='IsShowSubTitle')  # Field name made lowercase.
    products_featured = models.IntegerField(blank=True, null=True)
    products_tax_class_id = models.IntegerField()
    manufacturers_id = models.IntegerField(blank=True, null=True)
    products_ordered = models.IntegerField()
    products_sale_price = models.DecimalField(max_digits=15, decimal_places=4)
    products_purchase_price = models.DecimalField(max_digits=15, decimal_places=4)
    products_length = models.DecimalField(max_digits=6, decimal_places=2)
    products_width = models.DecimalField(max_digits=6, decimal_places=2)
    products_height = models.DecimalField(max_digits=6, decimal_places=2)
    products_ready_to_ship = models.IntegerField()
    products_disable_ups = models.IntegerField(blank=True, null=True)
    products_enable_usps = models.IntegerField(blank=True, null=True)
    products_free_shipping = models.CharField(max_length=1, blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)
    products_video = models.CharField(max_length=255, blank=True, null=True)
    products_ga_keywords = models.TextField(blank=True, null=True)
    products_bulk = models.CharField(max_length=10)
    px_id = models.IntegerField()
    supply_type = models.IntegerField(blank=True, null=True)
    oa_px_id = models.IntegerField()
    sj_id = models.IntegerField()
    oa_sj_id = models.IntegerField()
    deliver_type = models.IntegerField()
    booking_time = models.DateTimeField()
    book_end_time = models.DateTimeField()
    is_snamup = models.IntegerField()
    show_size = models.IntegerField()
    show_new_arrival = models.IntegerField()
    oa_kf_id = models.IntegerField()
    oa_ms_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'products'
