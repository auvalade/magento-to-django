# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 00:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingTablerate',
            fields=[
                ('st_pk', models.IntegerField(primary_key=True, serialize=False)),
                ('website_id', models.IntegerField()),
                ('dest_country_id', models.CharField(max_length=4)),
                ('dest_region_id', models.IntegerField()),
                ('dest_zip', models.CharField(max_length=10)),
                ('condition_name', models.CharField(max_length=20)),
                ('condition_value', models.DecimalField(decimal_places=4, max_digits=12)),
                ('price', models.DecimalField(decimal_places=4, max_digits=12)),
                ('cost', models.DecimalField(decimal_places=4, max_digits=12)),
            ],
            options={
                'db_table': 'shipping_tablerate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sitemap',
            fields=[
                ('sitemap_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sitemap_type', models.CharField(blank=True, max_length=32, null=True)),
                ('sitemap_filename', models.CharField(blank=True, max_length=32, null=True)),
                ('sitemap_path', models.CharField(blank=True, max_length=255, null=True)),
                ('sitemap_time', models.DateTimeField(blank=True, null=True)),
                ('store_id', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'sitemap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.SmallIntegerField()),
                ('first_customer_id', models.IntegerField(blank=True, null=True)),
                ('first_store_id', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TagProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_id', models.IntegerField()),
                ('store_id', models.SmallIntegerField()),
                ('base_popularity', models.IntegerField()),
            ],
            options={
                'db_table': 'tag_properties',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TagRelation',
            fields=[
                ('tag_relation_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tag_id', models.IntegerField()),
                ('customer_id', models.IntegerField(blank=True, null=True)),
                ('product_id', models.IntegerField()),
                ('store_id', models.SmallIntegerField()),
                ('active', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tag_relation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TagSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_id', models.IntegerField()),
                ('store_id', models.SmallIntegerField()),
                ('customers', models.IntegerField()),
                ('products', models.IntegerField()),
                ('uses', models.IntegerField()),
                ('historical_uses', models.IntegerField()),
                ('popularity', models.IntegerField()),
                ('base_popularity', models.IntegerField()),
            ],
            options={
                'db_table': 'tag_summary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaxCalculation',
            fields=[
                ('tax_calculation_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tax_calculation_rate_id', models.IntegerField()),
                ('tax_calculation_rule_id', models.IntegerField()),
                ('customer_tax_class_id', models.SmallIntegerField()),
                ('product_tax_class_id', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'tax_calculation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaxCalculationRate',
            fields=[
                ('tax_calculation_rate_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tax_country_id', models.CharField(max_length=2)),
                ('tax_region_id', models.IntegerField()),
                ('tax_postcode', models.CharField(blank=True, max_length=21, null=True)),
                ('code', models.CharField(max_length=255)),
                ('rate', models.DecimalField(decimal_places=4, max_digits=12)),
                ('zip_is_range', models.SmallIntegerField(blank=True, null=True)),
                ('zip_from', models.IntegerField(blank=True, null=True)),
                ('zip_to', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tax_calculation_rate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaxCalculationRateTitle',
            fields=[
                ('tax_calculation_rate_title_id', models.IntegerField(primary_key=True, serialize=False)),
                ('tax_calculation_rate_id', models.IntegerField()),
                ('store_id', models.SmallIntegerField()),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tax_calculation_rate_title',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaxCalculationRule',
            fields=[
                ('tax_calculation_rule_id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=255)),
                ('priority', models.IntegerField()),
                ('position', models.IntegerField()),
                ('calculate_subtotal', models.IntegerField()),
            ],
            options={
                'db_table': 'tax_calculation_rule',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaxClass',
            fields=[
                ('class_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=255)),
                ('class_type', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'tax_class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaxOrderAggregatedCreated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(blank=True, null=True)),
                ('store_id', models.SmallIntegerField(blank=True, null=True)),
                ('code', models.CharField(max_length=255)),
                ('order_status', models.CharField(max_length=50)),
                ('percent', models.FloatField(blank=True, null=True)),
                ('orders_count', models.IntegerField()),
                ('tax_base_amount_sum', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tax_order_aggregated_created',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TaxOrderAggregatedUpdated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(blank=True, null=True)),
                ('store_id', models.SmallIntegerField(blank=True, null=True)),
                ('code', models.CharField(max_length=255)),
                ('order_status', models.CharField(max_length=50)),
                ('percent', models.FloatField(blank=True, null=True)),
                ('orders_count', models.IntegerField()),
                ('tax_base_amount_sum', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tax_order_aggregated_updated',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeeeDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_id', models.IntegerField()),
                ('website_id', models.SmallIntegerField()),
                ('customer_group_id', models.SmallIntegerField()),
                ('value', models.DecimalField(decimal_places=4, max_digits=12)),
            ],
            options={
                'db_table': 'weee_discount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WeeeTax',
            fields=[
                ('value_id', models.IntegerField(primary_key=True, serialize=False)),
                ('website_id', models.SmallIntegerField()),
                ('entity_id', models.IntegerField()),
                ('country', models.CharField(blank=True, max_length=2, null=True)),
                ('value', models.DecimalField(decimal_places=4, max_digits=12)),
                ('state', models.CharField(max_length=255)),
                ('attribute_id', models.SmallIntegerField()),
                ('entity_type_id', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'weee_tax',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('widget_id', models.IntegerField(primary_key=True, serialize=False)),
                ('widget_code', models.CharField(blank=True, max_length=255, null=True)),
                ('widget_type', models.CharField(blank=True, max_length=255, null=True)),
                ('parameters', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'widget',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WidgetInstance',
            fields=[
                ('instance_id', models.IntegerField(primary_key=True, serialize=False)),
                ('instance_type', models.CharField(blank=True, max_length=255, null=True)),
                ('package_theme', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('store_ids', models.CharField(max_length=255)),
                ('widget_parameters', models.TextField(blank=True, null=True)),
                ('sort_order', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'widget_instance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WidgetInstancePage',
            fields=[
                ('page_id', models.IntegerField(primary_key=True, serialize=False)),
                ('instance_id', models.IntegerField()),
                ('page_group', models.CharField(blank=True, max_length=25, null=True)),
                ('layout_handle', models.CharField(blank=True, max_length=255, null=True)),
                ('block_reference', models.CharField(blank=True, max_length=255, null=True)),
                ('page_for', models.CharField(blank=True, max_length=25, null=True)),
                ('entities', models.TextField(blank=True, null=True)),
                ('page_template', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'widget_instance_page',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WidgetInstancePageLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_id', models.IntegerField()),
                ('layout_update_id', models.IntegerField()),
            ],
            options={
                'db_table': 'widget_instance_page_layout',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('wishlist_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField(unique=True)),
                ('shared', models.SmallIntegerField()),
                ('sharing_code', models.CharField(blank=True, max_length=32, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wishlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('wishlist_item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('wishlist_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('store_id', models.SmallIntegerField(blank=True, null=True)),
                ('added_at', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('qty', models.DecimalField(decimal_places=4, max_digits=12)),
            ],
            options={
                'db_table': 'wishlist_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WishlistItemOption',
            fields=[
                ('option_id', models.IntegerField(primary_key=True, serialize=False)),
                ('wishlist_item_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('code', models.CharField(max_length=255)),
                ('value', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wishlist_item_option',
                'managed': False,
            },
        ),
    ]
