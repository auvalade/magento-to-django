# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AdminAssert(models.Model):
    assert_id = models.IntegerField(primary_key=True)
    assert_type = models.CharField(max_length=20, blank=True, null=True)
    assert_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_assert'


class AdminRole(models.Model):
    role_id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    tree_level = models.SmallIntegerField()
    sort_order = models.SmallIntegerField()
    role_type = models.CharField(max_length=1)
    user_id = models.IntegerField()
    role_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_role'


class AdminRule(models.Model):
    rule_id = models.IntegerField(primary_key=True)
    role = models.ForeignKey(AdminRole, models.DO_NOTHING)
    resource_id = models.CharField(max_length=255, blank=True, null=True)
    privileges = models.CharField(max_length=20, blank=True, null=True)
    assert_id = models.IntegerField()
    role_type = models.CharField(max_length=1, blank=True, null=True)
    permission = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_rule'


class AdminUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(unique=True, max_length=40, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    logdate = models.DateTimeField(blank=True, null=True)
    lognum = models.SmallIntegerField()
    reload_acl_flag = models.SmallIntegerField()
    is_active = models.SmallIntegerField()
    extra = models.TextField(blank=True, null=True)
    rp_token = models.TextField(blank=True, null=True)
    rp_token_created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin_user'


class AdminnotificationInbox(models.Model):
    notification_id = models.IntegerField(primary_key=True)
    severity = models.SmallIntegerField()
    date_added = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    is_read = models.SmallIntegerField()
    is_remove = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'adminnotification_inbox'


class Api2AclAttribute(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    user_type = models.CharField(max_length=20)
    resource_id = models.CharField(max_length=255)
    operation = models.CharField(max_length=20)
    allowed_attributes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api2_acl_attribute'
        unique_together = (('user_type', 'resource_id', 'operation'),)


class Api2AclRole(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    role_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'api2_acl_role'


class Api2AclRule(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    role = models.ForeignKey(Api2AclRole, models.DO_NOTHING)
    resource_id = models.CharField(max_length=255)
    privilege = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api2_acl_rule'
        unique_together = (('role', 'resource_id', 'privilege'),)


class Api2AclUser(models.Model):
    admin = models.ForeignKey(AdminUser, models.DO_NOTHING, unique=True)
    role = models.ForeignKey(Api2AclRole, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'api2_acl_user'


class ApiAssert(models.Model):
    assert_id = models.IntegerField(primary_key=True)
    assert_type = models.CharField(max_length=20, blank=True, null=True)
    assert_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_assert'


class ApiRole(models.Model):
    role_id = models.IntegerField(primary_key=True)
    parent_id = models.IntegerField()
    tree_level = models.SmallIntegerField()
    sort_order = models.SmallIntegerField()
    role_type = models.CharField(max_length=1)
    user_id = models.IntegerField()
    role_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_role'


class ApiRule(models.Model):
    rule_id = models.IntegerField(primary_key=True)
    role = models.ForeignKey(ApiRole, models.DO_NOTHING)
    resource_id = models.CharField(max_length=255, blank=True, null=True)
    api_privileges = models.CharField(max_length=20, blank=True, null=True)
    assert_id = models.IntegerField()
    role_type = models.CharField(max_length=1, blank=True, null=True)
    api_permission = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_rule'


class ApiSession(models.Model):
    user = models.ForeignKey('ApiUser', models.DO_NOTHING)
    logdate = models.DateTimeField()
    sessid = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api_session'


class ApiUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True, null=True)
    api_key = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    lognum = models.SmallIntegerField()
    reload_acl_flag = models.SmallIntegerField()
    is_active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_user'


class CaptchaLog(models.Model):
    type = models.CharField(max_length=32)
    value = models.CharField(max_length=32)
    count = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'captcha_log'
        unique_together = (('type', 'value'),)


class CatalogCategoryAncCategsIndexIdx(models.Model):
    category_id = models.IntegerField()
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_anc_categs_index_idx'


class CatalogCategoryAncCategsIndexTmp(models.Model):
    category_id = models.IntegerField()
    path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_anc_categs_index_tmp'


class CatalogCategoryAncProductsIndexIdx(models.Model):
    category_id = models.IntegerField()
    product_id = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_anc_products_index_idx'


class CatalogCategoryAncProductsIndexTmp(models.Model):
    category_id = models.IntegerField()
    product_id = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_anc_products_index_tmp'


class CatalogCategoryEntity(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute_set_id = models.SmallIntegerField()
    parent_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=255)
    position = models.IntegerField()
    level = models.IntegerField()
    children_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_entity'


class CatalogCategoryEntityDatetime(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    entity = models.ForeignKey(CatalogCategoryEntity, models.DO_NOTHING)
    value = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_entity_datetime'
        unique_together = (('entity_type_id', 'entity', 'attribute', 'store'),)


class CatalogCategoryEntityDecimal(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    entity = models.ForeignKey(CatalogCategoryEntity, models.DO_NOTHING)
    value = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_entity_decimal'
        unique_together = (('entity_type_id', 'entity', 'attribute', 'store'),)


class CatalogCategoryEntityInt(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    entity = models.ForeignKey(CatalogCategoryEntity, models.DO_NOTHING)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_entity_int'
        unique_together = (('entity_type_id', 'entity', 'attribute', 'store'),)


class CatalogCategoryEntityText(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    entity = models.ForeignKey(CatalogCategoryEntity, models.DO_NOTHING)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_entity_text'
        unique_together = (('entity_type_id', 'entity', 'attribute', 'store'),)


class CatalogCategoryEntityVarchar(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    entity = models.ForeignKey(CatalogCategoryEntity, models.DO_NOTHING)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_entity_varchar'
        unique_together = (('entity_type_id', 'entity', 'attribute', 'store'),)


class CatalogCategoryFlatStore1(models.Model):
    entity = models.ForeignKey(CatalogCategoryEntity, models.DO_NOTHING, primary_key=True)
    parent_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=255)
    position = models.IntegerField()
    level = models.IntegerField()
    children_count = models.IntegerField()
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    all_children = models.TextField(blank=True, null=True)
    available_sort_by = models.TextField(blank=True, null=True)
    children = models.TextField(blank=True, null=True)
    custom_apply_to_products = models.IntegerField(blank=True, null=True)
    custom_design = models.CharField(max_length=255, blank=True, null=True)
    custom_design_from = models.DateTimeField(blank=True, null=True)
    custom_design_to = models.DateTimeField(blank=True, null=True)
    custom_layout_update = models.TextField(blank=True, null=True)
    custom_use_parent_settings = models.IntegerField(blank=True, null=True)
    default_sort_by = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    display_mode = models.CharField(max_length=255, blank=True, null=True)
    filter_price_range = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    include_in_menu = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    is_anchor = models.IntegerField(blank=True, null=True)
    landing_page = models.IntegerField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    page_layout = models.CharField(max_length=255, blank=True, null=True)
    path_in_store = models.TextField(blank=True, null=True)
    url_key = models.CharField(max_length=255, blank=True, null=True)
    url_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_category_flat_store_1'


class CatalogCategoryProduct(models.Model):
    category = models.ForeignKey(CatalogCategoryEntity, models.DO_NOTHING)
    product = models.ForeignKey('CatalogProductEntity', models.DO_NOTHING)
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_product'
        unique_together = (('category', 'product'),)


class CatalogCategoryProductIndex(models.Model):
    category = models.ForeignKey(CatalogCategoryEntity, models.DO_NOTHING)
    product = models.ForeignKey('CatalogProductEntity', models.DO_NOTHING)
    position = models.IntegerField(blank=True, null=True)
    is_parent = models.SmallIntegerField()
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    visibility = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_product_index'
        unique_together = (('category', 'product', 'store'),)


class CatalogCategoryProductIndexEnblIdx(models.Model):
    product_id = models.IntegerField()
    visibility = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_product_index_enbl_idx'


class CatalogCategoryProductIndexEnblTmp(models.Model):
    product_id = models.IntegerField()
    visibility = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_product_index_enbl_tmp'


class CatalogCategoryProductIndexIdx(models.Model):
    category_id = models.IntegerField()
    product_id = models.IntegerField()
    position = models.IntegerField()
    is_parent = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    visibility = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_product_index_idx'


class CatalogCategoryProductIndexTmp(models.Model):
    category_id = models.IntegerField()
    product_id = models.IntegerField()
    position = models.IntegerField()
    is_parent = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    visibility = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_category_product_index_tmp'


class CatalogCompareItem(models.Model):
    catalog_compare_item_id = models.IntegerField(primary_key=True)
    visitor_id = models.IntegerField()
    customer = models.ForeignKey('CustomerEntity', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('CatalogProductEntity', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_compare_item'


class CatalogEavAttribute(models.Model):
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING, primary_key=True)
    frontend_input_renderer = models.CharField(max_length=255, blank=True, null=True)
    is_global = models.SmallIntegerField()
    is_visible = models.SmallIntegerField()
    is_searchable = models.SmallIntegerField()
    is_filterable = models.SmallIntegerField()
    is_comparable = models.SmallIntegerField()
    is_visible_on_front = models.SmallIntegerField()
    is_html_allowed_on_front = models.SmallIntegerField()
    is_used_for_price_rules = models.SmallIntegerField()
    is_filterable_in_search = models.SmallIntegerField()
    used_in_product_listing = models.SmallIntegerField()
    used_for_sort_by = models.SmallIntegerField()
    is_configurable = models.SmallIntegerField()
    apply_to = models.CharField(max_length=255, blank=True, null=True)
    is_visible_in_advanced_search = models.SmallIntegerField()
    position = models.IntegerField()
    is_wysiwyg_enabled = models.SmallIntegerField()
    is_used_for_promo_rules = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_eav_attribute'


class CatalogProductBundleOption(models.Model):
    option_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey('CatalogProductEntity', models.DO_NOTHING)
    required = models.SmallIntegerField()
    position = models.IntegerField()
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_bundle_option'


class CatalogProductBundleOptionValue(models.Model):
    value_id = models.IntegerField(primary_key=True)
    option = models.ForeignKey(CatalogProductBundleOption, models.DO_NOTHING)
    store_id = models.SmallIntegerField()
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_bundle_option_value'
        unique_together = (('option', 'store_id'),)


class CatalogProductBundlePriceIndex(models.Model):
    entity = models.ForeignKey('CatalogProductEntity', models.DO_NOTHING)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)
    customer_group = models.ForeignKey('CustomerGroup', models.DO_NOTHING)
    min_price = models.DecimalField(max_digits=12, decimal_places=4)
    max_price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_bundle_price_index'
        unique_together = (('entity', 'website', 'customer_group'),)


class CatalogProductBundleSelection(models.Model):
    selection_id = models.IntegerField(primary_key=True)
    option = models.ForeignKey(CatalogProductBundleOption, models.DO_NOTHING)
    parent_product_id = models.IntegerField()
    product = models.ForeignKey('CatalogProductEntity', models.DO_NOTHING)
    position = models.IntegerField()
    is_default = models.SmallIntegerField()
    selection_price_type = models.SmallIntegerField()
    selection_price_value = models.DecimalField(max_digits=12, decimal_places=4)
    selection_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    selection_can_change_qty = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_bundle_selection'


class CatalogProductBundleSelectionPrice(models.Model):
    selection = models.ForeignKey(CatalogProductBundleSelection, models.DO_NOTHING)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)
    selection_price_type = models.SmallIntegerField()
    selection_price_value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_bundle_selection_price'
        unique_together = (('selection', 'website'),)


class CatalogProductBundleStockIndex(models.Model):
    entity_id = models.IntegerField()
    website_id = models.SmallIntegerField()
    stock_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    stock_status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_bundle_stock_index'
        unique_together = (('entity_id', 'website_id', 'stock_id', 'option_id'),)


class CatalogProductEnabledIndex(models.Model):
    product = models.ForeignKey('CatalogProductEntity', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    visibility = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_enabled_index'
        unique_together = (('product', 'store'),)


class CatalogProductEntity(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute_set = models.ForeignKey('EavAttributeSet', models.DO_NOTHING)
    type_id = models.CharField(max_length=32)
    sku = models.CharField(max_length=64, blank=True, null=True)
    has_options = models.SmallIntegerField()
    required_options = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity'


class CatalogProductEntityDatetime(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    value = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_datetime'
        unique_together = (('entity', 'attribute', 'store'),)


class CatalogProductEntityDecimal(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    value = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_decimal'
        unique_together = (('entity', 'attribute', 'store'),)


class CatalogProductEntityGallery(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    position = models.IntegerField()
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_gallery'
        unique_together = (('entity_type_id', 'entity', 'attribute', 'store'),)


class CatalogProductEntityGroupPrice(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    all_groups = models.SmallIntegerField()
    customer_group = models.ForeignKey('CustomerGroup', models.DO_NOTHING)
    value = models.DecimalField(max_digits=12, decimal_places=4)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_group_price'
        unique_together = (('entity', 'all_groups', 'customer_group', 'website'),)


class CatalogProductEntityInt(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type_id = models.IntegerField()
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    value = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_int'
        unique_together = (('entity', 'attribute', 'store'),)


class CatalogProductEntityMediaGallery(models.Model):
    value_id = models.IntegerField(primary_key=True)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_media_gallery'


class CatalogProductEntityMediaGalleryValue(models.Model):
    value = models.ForeignKey(CatalogProductEntityMediaGallery, models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    label = models.CharField(max_length=255, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    disabled = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_media_gallery_value'
        unique_together = (('value', 'store'),)


class CatalogProductEntityText(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type_id = models.IntegerField()
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_text'
        unique_together = (('entity', 'attribute', 'store'),)


class CatalogProductEntityTierPrice(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    all_groups = models.SmallIntegerField()
    customer_group = models.ForeignKey('CustomerGroup', models.DO_NOTHING)
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    value = models.DecimalField(max_digits=12, decimal_places=4)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_tier_price'
        unique_together = (('entity', 'all_groups', 'customer_group', 'qty', 'website'),)


class CatalogProductEntityVarchar(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type_id = models.IntegerField()
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_entity_varchar'
        unique_together = (('entity', 'attribute', 'store'),)


class CatalogProductFlat1(models.Model):
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING, primary_key=True)
    attribute_set_id = models.SmallIntegerField()
    type_id = models.CharField(max_length=32)
    cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    gift_message_available = models.SmallIntegerField(blank=True, null=True)
    has_options = models.SmallIntegerField()
    image_label = models.CharField(max_length=255, blank=True, null=True)
    is_recurring = models.SmallIntegerField(blank=True, null=True)
    links_exist = models.IntegerField(blank=True, null=True)
    links_purchased_separately = models.IntegerField(blank=True, null=True)
    links_title = models.CharField(max_length=255, blank=True, null=True)
    msrp = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    msrp_display_actual_price_type = models.CharField(max_length=255, blank=True, null=True)
    msrp_enabled = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    news_from_date = models.DateTimeField(blank=True, null=True)
    news_to_date = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price_type = models.IntegerField(blank=True, null=True)
    price_view = models.IntegerField(blank=True, null=True)
    recurring_profile = models.TextField(blank=True, null=True)
    required_options = models.SmallIntegerField()
    shipment_type = models.IntegerField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=64, blank=True, null=True)
    sku_type = models.IntegerField(blank=True, null=True)
    small_image = models.CharField(max_length=255, blank=True, null=True)
    small_image_label = models.CharField(max_length=255, blank=True, null=True)
    special_from_date = models.DateTimeField(blank=True, null=True)
    special_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    special_to_date = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    tax_class_id = models.IntegerField(blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    thumbnail_label = models.CharField(max_length=255, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    url_key = models.CharField(max_length=255, blank=True, null=True)
    url_path = models.CharField(max_length=255, blank=True, null=True)
    visibility = models.SmallIntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weight_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_flat_1'


class CatalogProductIndexEav(models.Model):
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_index_eav'
        unique_together = (('entity', 'attribute', 'store', 'value'),)


class CatalogProductIndexEavDecimal(models.Model):
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_eav_decimal'
        unique_together = (('entity', 'attribute', 'store'),)


class CatalogProductIndexEavDecimalIdx(models.Model):
    entity_id = models.IntegerField()
    attribute_id = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_eav_decimal_idx'
        unique_together = (('entity_id', 'attribute_id', 'store_id', 'value'),)


class CatalogProductIndexEavDecimalTmp(models.Model):
    entity_id = models.IntegerField()
    attribute_id = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_eav_decimal_tmp'
        unique_together = (('entity_id', 'attribute_id', 'store_id'),)


class CatalogProductIndexEavIdx(models.Model):
    entity_id = models.IntegerField()
    attribute_id = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_index_eav_idx'
        unique_together = (('entity_id', 'attribute_id', 'store_id', 'value'),)


class CatalogProductIndexEavTmp(models.Model):
    entity_id = models.IntegerField()
    attribute_id = models.SmallIntegerField()
    store_id = models.SmallIntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_index_eav_tmp'
        unique_together = (('entity_id', 'attribute_id', 'store_id', 'value'),)


class CatalogProductIndexGroupPrice(models.Model):
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    customer_group = models.ForeignKey('CustomerGroup', models.DO_NOTHING)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_group_price'
        unique_together = (('entity', 'customer_group', 'website'),)


class CatalogProductIndexPrice(models.Model):
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    customer_group = models.ForeignKey('CustomerGroup', models.DO_NOTHING)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    final_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price'
        unique_together = (('entity', 'customer_group', 'website'),)


class CatalogProductIndexPriceBundleIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    price_type = models.SmallIntegerField()
    special_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    orig_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tier = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_bundle_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceBundleOptIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    alt_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    alt_tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    alt_group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_bundle_opt_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id', 'option_id'),)


class CatalogProductIndexPriceBundleOptTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    alt_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    alt_tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    alt_group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_bundle_opt_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id', 'option_id'),)


class CatalogProductIndexPriceBundleSelIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    selection_id = models.IntegerField()
    group_type = models.SmallIntegerField(blank=True, null=True)
    is_required = models.SmallIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_bundle_sel_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id', 'option_id', 'selection_id'),)


class CatalogProductIndexPriceBundleSelTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    selection_id = models.IntegerField()
    group_type = models.SmallIntegerField(blank=True, null=True)
    is_required = models.SmallIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_bundle_sel_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id', 'option_id', 'selection_id'),)


class CatalogProductIndexPriceBundleTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    price_type = models.SmallIntegerField()
    special_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    orig_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tier = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_bundle_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceCfgOptAgrIdx(models.Model):
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_cfg_opt_agr_idx'
        unique_together = (('parent_id', 'child_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceCfgOptAgrTmp(models.Model):
    parent_id = models.IntegerField()
    child_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_cfg_opt_agr_tmp'
        unique_together = (('parent_id', 'child_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceCfgOptIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_cfg_opt_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceCfgOptTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_cfg_opt_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceDownlodIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4)
    max_price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_downlod_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceDownlodTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4)
    max_price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_downlod_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceFinalIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    orig_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tier = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_final_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceFinalTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    orig_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tier = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_final_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    final_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceOptAgrIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_opt_agr_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id', 'option_id'),)


class CatalogProductIndexPriceOptAgrTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    option_id = models.IntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_opt_agr_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id', 'option_id'),)


class CatalogProductIndexPriceOptIdx(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_opt_idx'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceOptTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_opt_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexPriceTmp(models.Model):
    entity_id = models.IntegerField()
    customer_group_id = models.SmallIntegerField()
    website_id = models.SmallIntegerField()
    tax_class_id = models.SmallIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    final_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    max_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tier_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    group_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_price_tmp'
        unique_together = (('entity_id', 'customer_group_id', 'website_id'),)


class CatalogProductIndexTierPrice(models.Model):
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    customer_group = models.ForeignKey('CustomerGroup', models.DO_NOTHING)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)
    min_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_tier_price'
        unique_together = (('entity', 'customer_group', 'website'),)


class CatalogProductIndexWebsite(models.Model):
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING, primary_key=True)
    website_date = models.DateField(blank=True, null=True)
    rate = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_index_website'


class CatalogProductLink(models.Model):
    link_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    linked_product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    link_type = models.ForeignKey('CatalogProductLinkType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalog_product_link'
        unique_together = (('link_type', 'product', 'linked_product'),)


class CatalogProductLinkAttribute(models.Model):
    product_link_attribute_id = models.SmallIntegerField(primary_key=True)
    link_type = models.ForeignKey('CatalogProductLinkType', models.DO_NOTHING)
    product_link_attribute_code = models.CharField(max_length=32, blank=True, null=True)
    data_type = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_link_attribute'


class CatalogProductLinkAttributeDecimal(models.Model):
    value_id = models.IntegerField(primary_key=True)
    product_link_attribute = models.ForeignKey(CatalogProductLinkAttribute, models.DO_NOTHING, blank=True, null=True)
    link = models.ForeignKey(CatalogProductLink, models.DO_NOTHING)
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalog_product_link_attribute_decimal'
        unique_together = (('product_link_attribute', 'link'),)


class CatalogProductLinkAttributeInt(models.Model):
    value_id = models.IntegerField(primary_key=True)
    product_link_attribute = models.ForeignKey(CatalogProductLinkAttribute, models.DO_NOTHING, blank=True, null=True)
    link = models.ForeignKey(CatalogProductLink, models.DO_NOTHING)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_link_attribute_int'
        unique_together = (('product_link_attribute', 'link'),)


class CatalogProductLinkAttributeVarchar(models.Model):
    value_id = models.IntegerField(primary_key=True)
    product_link_attribute = models.ForeignKey(CatalogProductLinkAttribute, models.DO_NOTHING)
    link = models.ForeignKey(CatalogProductLink, models.DO_NOTHING)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_link_attribute_varchar'
        unique_together = (('product_link_attribute', 'link'),)


class CatalogProductLinkType(models.Model):
    link_type_id = models.SmallIntegerField(primary_key=True)
    code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_link_type'


class CatalogProductOption(models.Model):
    option_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    type = models.CharField(max_length=50, blank=True, null=True)
    is_require = models.SmallIntegerField()
    sku = models.CharField(max_length=64, blank=True, null=True)
    max_characters = models.IntegerField(blank=True, null=True)
    file_extension = models.CharField(max_length=50, blank=True, null=True)
    image_size_x = models.SmallIntegerField(blank=True, null=True)
    image_size_y = models.SmallIntegerField(blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_option'


class CatalogProductOptionPrice(models.Model):
    option_price_id = models.IntegerField(primary_key=True)
    option = models.ForeignKey(CatalogProductOption, models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    price_type = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'catalog_product_option_price'
        unique_together = (('option', 'store'),)


class CatalogProductOptionTitle(models.Model):
    option_title_id = models.IntegerField(primary_key=True)
    option = models.ForeignKey(CatalogProductOption, models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_option_title'
        unique_together = (('option', 'store'),)


class CatalogProductOptionTypePrice(models.Model):
    option_type_price_id = models.IntegerField(primary_key=True)
    option_type = models.ForeignKey('CatalogProductOptionTypeValue', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    price_type = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'catalog_product_option_type_price'
        unique_together = (('option_type', 'store'),)


class CatalogProductOptionTypeTitle(models.Model):
    option_type_title_id = models.IntegerField(primary_key=True)
    option_type = models.ForeignKey('CatalogProductOptionTypeValue', models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_option_type_title'
        unique_together = (('option_type', 'store'),)


class CatalogProductOptionTypeValue(models.Model):
    option_type_id = models.IntegerField(primary_key=True)
    option = models.ForeignKey(CatalogProductOption, models.DO_NOTHING)
    sku = models.CharField(max_length=64, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_option_type_value'


class CatalogProductRelation(models.Model):
    parent = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    child = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalog_product_relation'
        unique_together = (('parent', 'child'),)


class CatalogProductSuperAttribute(models.Model):
    product_super_attribute_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    attribute_id = models.SmallIntegerField()
    position = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catalog_product_super_attribute'
        unique_together = (('product', 'attribute_id'),)


class CatalogProductSuperAttributeLabel(models.Model):
    value_id = models.IntegerField(primary_key=True)
    product_super_attribute = models.ForeignKey(CatalogProductSuperAttribute, models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    use_default = models.SmallIntegerField(blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product_super_attribute_label'
        unique_together = (('product_super_attribute', 'store'),)


class CatalogProductSuperAttributePricing(models.Model):
    value_id = models.IntegerField(primary_key=True)
    product_super_attribute = models.ForeignKey(CatalogProductSuperAttribute, models.DO_NOTHING)
    value_index = models.CharField(max_length=255, blank=True, null=True)
    is_percent = models.SmallIntegerField(blank=True, null=True)
    pricing_value = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalog_product_super_attribute_pricing'
        unique_together = (('product_super_attribute', 'value_index', 'website'),)


class CatalogProductSuperLink(models.Model):
    link_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    parent = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalog_product_super_link'
        unique_together = (('product', 'parent'),)


class CatalogProductWebsite(models.Model):
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalog_product_website'
        unique_together = (('product', 'website'),)


class CataloginventoryStock(models.Model):
    stock_id = models.SmallIntegerField(primary_key=True)
    stock_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cataloginventory_stock'


class CataloginventoryStockItem(models.Model):
    item_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    stock = models.ForeignKey(CataloginventoryStock, models.DO_NOTHING)
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    min_qty = models.DecimalField(max_digits=12, decimal_places=4)
    use_config_min_qty = models.SmallIntegerField()
    is_qty_decimal = models.SmallIntegerField()
    backorders = models.SmallIntegerField()
    use_config_backorders = models.SmallIntegerField()
    min_sale_qty = models.DecimalField(max_digits=12, decimal_places=4)
    use_config_min_sale_qty = models.SmallIntegerField()
    max_sale_qty = models.DecimalField(max_digits=12, decimal_places=4)
    use_config_max_sale_qty = models.SmallIntegerField()
    is_in_stock = models.SmallIntegerField()
    low_stock_date = models.DateTimeField(blank=True, null=True)
    notify_stock_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    use_config_notify_stock_qty = models.SmallIntegerField()
    manage_stock = models.SmallIntegerField()
    use_config_manage_stock = models.SmallIntegerField()
    stock_status_changed_auto = models.SmallIntegerField()
    use_config_qty_increments = models.SmallIntegerField()
    qty_increments = models.DecimalField(max_digits=12, decimal_places=4)
    use_config_enable_qty_inc = models.SmallIntegerField()
    enable_qty_increments = models.SmallIntegerField()
    is_decimal_divided = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cataloginventory_stock_item'
        unique_together = (('product', 'stock'),)


class CataloginventoryStockStatus(models.Model):
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)
    stock = models.ForeignKey(CataloginventoryStock, models.DO_NOTHING)
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    stock_status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cataloginventory_stock_status'
        unique_together = (('product', 'website', 'stock'),)


class CataloginventoryStockStatusIdx(models.Model):
    product_id = models.IntegerField()
    website_id = models.SmallIntegerField()
    stock_id = models.SmallIntegerField()
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    stock_status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cataloginventory_stock_status_idx'
        unique_together = (('product_id', 'website_id', 'stock_id'),)


class CataloginventoryStockStatusTmp(models.Model):
    product_id = models.IntegerField()
    website_id = models.SmallIntegerField()
    stock_id = models.SmallIntegerField()
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    stock_status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cataloginventory_stock_status_tmp'
        unique_together = (('product_id', 'website_id', 'stock_id'),)


class Catalogrule(models.Model):
    rule_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    is_active = models.SmallIntegerField()
    conditions_serialized = models.TextField(blank=True, null=True)
    actions_serialized = models.TextField(blank=True, null=True)
    stop_rules_processing = models.SmallIntegerField()
    sort_order = models.IntegerField()
    simple_action = models.CharField(max_length=32, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    sub_is_enable = models.SmallIntegerField()
    sub_simple_action = models.CharField(max_length=32, blank=True, null=True)
    sub_discount_amount = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalogrule'


class CatalogruleAffectedProduct(models.Model):
    product_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'catalogrule_affected_product'


class CatalogruleCustomerGroup(models.Model):
    rule = models.ForeignKey(Catalogrule, models.DO_NOTHING)
    customer_group = models.ForeignKey('CustomerGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogrule_customer_group'
        unique_together = (('rule', 'customer_group'),)


class CatalogruleGroupWebsite(models.Model):
    rule = models.ForeignKey(Catalogrule, models.DO_NOTHING)
    customer_group = models.ForeignKey('CustomerGroup', models.DO_NOTHING)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogrule_group_website'
        unique_together = (('rule', 'customer_group', 'website'),)


class CatalogruleProduct(models.Model):
    rule_product_id = models.IntegerField(primary_key=True)
    rule = models.ForeignKey(Catalogrule, models.DO_NOTHING)
    from_time = models.IntegerField()
    to_time = models.IntegerField()
    customer_group = models.ForeignKey('CustomerGroup', models.DO_NOTHING)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    action_operator = models.CharField(max_length=10, blank=True, null=True)
    action_amount = models.DecimalField(max_digits=12, decimal_places=4)
    action_stop = models.SmallIntegerField()
    sort_order = models.IntegerField()
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)
    sub_simple_action = models.CharField(max_length=32, blank=True, null=True)
    sub_discount_amount = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalogrule_product'
        unique_together = (('rule', 'from_time', 'to_time', 'website', 'customer_group', 'product', 'sort_order'),)


class CatalogruleProductPrice(models.Model):
    rule_product_price_id = models.IntegerField(primary_key=True)
    rule_date = models.DateField()
    customer_group = models.ForeignKey('CustomerGroup', models.DO_NOTHING)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    rule_price = models.DecimalField(max_digits=12, decimal_places=4)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)
    latest_start_date = models.DateField(blank=True, null=True)
    earliest_end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogrule_product_price'
        unique_together = (('rule_date', 'website', 'customer_group', 'product'),)


class CatalogruleWebsite(models.Model):
    rule = models.ForeignKey(Catalogrule, models.DO_NOTHING)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'catalogrule_website'
        unique_together = (('rule', 'website'),)


class CatalogsearchFulltext(models.Model):
    fulltext_id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    store_id = models.SmallIntegerField()
    data_index = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogsearch_fulltext'
        unique_together = (('product_id', 'store_id'),)


class CatalogsearchQuery(models.Model):
    query_id = models.IntegerField(primary_key=True)
    query_text = models.CharField(max_length=255, blank=True, null=True)
    num_results = models.IntegerField()
    popularity = models.IntegerField()
    redirect = models.CharField(max_length=255, blank=True, null=True)
    synonym_for = models.CharField(max_length=255, blank=True, null=True)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    display_in_terms = models.SmallIntegerField()
    is_active = models.SmallIntegerField(blank=True, null=True)
    is_processed = models.SmallIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'catalogsearch_query'


class CatalogsearchResult(models.Model):
    query = models.ForeignKey(CatalogsearchQuery, models.DO_NOTHING)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    relevance = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'catalogsearch_result'
        unique_together = (('query', 'product'),)


class CheckoutAgreement(models.Model):
    agreement_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    content_height = models.CharField(max_length=25, blank=True, null=True)
    checkbox_text = models.TextField(blank=True, null=True)
    is_active = models.SmallIntegerField()
    is_html = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'checkout_agreement'


class CheckoutAgreementStore(models.Model):
    agreement = models.ForeignKey(CheckoutAgreement, models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'checkout_agreement_store'
        unique_together = (('agreement', 'store'),)


class CmsBlock(models.Model):
    block_id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cms_block'


class CmsBlockStore(models.Model):
    block = models.ForeignKey(CmsBlock, models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_block_store'
        unique_together = (('block', 'store'),)


class CmsPage(models.Model):
    page_id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    root_template = models.CharField(max_length=255, blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    identifier = models.CharField(max_length=100, blank=True, null=True)
    content_heading = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_active = models.SmallIntegerField()
    sort_order = models.SmallIntegerField()
    layout_update_xml = models.TextField(blank=True, null=True)
    custom_theme = models.CharField(max_length=100, blank=True, null=True)
    custom_root_template = models.CharField(max_length=255, blank=True, null=True)
    custom_layout_update_xml = models.TextField(blank=True, null=True)
    custom_theme_from = models.DateField(blank=True, null=True)
    custom_theme_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_page'


class CmsPageStore(models.Model):
    page = models.ForeignKey(CmsPage, models.DO_NOTHING)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_page_store'
        unique_together = (('page', 'store'),)


class CoreCache(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    data = models.TextField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    expire_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_cache'


class CoreCacheOption(models.Model):
    code = models.CharField(primary_key=True, max_length=32)
    value = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_cache_option'


class CoreCacheTag(models.Model):
    tag = models.CharField(max_length=100)
    cache_id = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'core_cache_tag'
        unique_together = (('tag', 'cache_id'),)


class CoreConfigData(models.Model):
    config_id = models.IntegerField(primary_key=True)
    scope = models.CharField(max_length=8)
    scope_id = models.IntegerField()
    path = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_config_data'
        unique_together = (('scope', 'scope_id', 'path'),)


class CoreEmailQueue(models.Model):
    message_id = models.IntegerField(primary_key=True)
    entity_id = models.IntegerField(blank=True, null=True)
    entity_type = models.CharField(max_length=128, blank=True, null=True)
    event_type = models.CharField(max_length=128, blank=True, null=True)
    message_body_hash = models.CharField(max_length=64)
    message_body = models.TextField()
    message_parameters = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    processed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_email_queue'


class CoreEmailQueueRecipients(models.Model):
    recipient_id = models.IntegerField(primary_key=True)
    message = models.ForeignKey(CoreEmailQueue, models.DO_NOTHING)
    recipient_email = models.CharField(max_length=128)
    recipient_name = models.CharField(max_length=255)
    email_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'core_email_queue_recipients'
        unique_together = (('message', 'recipient_email', 'email_type'),)


class CoreEmailTemplate(models.Model):
    template_id = models.IntegerField(primary_key=True)
    template_code = models.CharField(unique=True, max_length=150)
    template_text = models.TextField()
    template_styles = models.TextField(blank=True, null=True)
    template_type = models.IntegerField(blank=True, null=True)
    template_subject = models.CharField(max_length=200)
    template_sender_name = models.CharField(max_length=200, blank=True, null=True)
    template_sender_email = models.CharField(max_length=200, blank=True, null=True)
    added_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    orig_template_code = models.CharField(max_length=200, blank=True, null=True)
    orig_template_variables = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_email_template'


class CoreFlag(models.Model):
    flag_id = models.IntegerField(primary_key=True)
    flag_code = models.CharField(max_length=255)
    state = models.SmallIntegerField()
    flag_data = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'core_flag'


class CoreLayoutLink(models.Model):
    layout_link_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey('CoreStore', models.DO_NOTHING)
    area = models.CharField(max_length=64, blank=True, null=True)
    package = models.CharField(max_length=64, blank=True, null=True)
    theme = models.CharField(max_length=64, blank=True, null=True)
    layout_update = models.ForeignKey('CoreLayoutUpdate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'core_layout_link'
        unique_together = (('store', 'package', 'theme', 'layout_update'),)


class CoreLayoutUpdate(models.Model):
    layout_update_id = models.IntegerField(primary_key=True)
    handle = models.CharField(max_length=255, blank=True, null=True)
    xml = models.TextField(blank=True, null=True)
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'core_layout_update'


class CoreResource(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    version = models.CharField(max_length=50, blank=True, null=True)
    data_version = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_resource'


class CoreSession(models.Model):
    session_id = models.CharField(primary_key=True, max_length=255)
    session_expires = models.IntegerField()
    session_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'core_session'


class CoreStore(models.Model):
    store_id = models.SmallIntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=32, blank=True, null=True)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)
    group = models.ForeignKey('CoreStoreGroup', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    sort_order = models.SmallIntegerField()
    is_active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'core_store'


class CoreStoreGroup(models.Model):
    group_id = models.SmallIntegerField(primary_key=True)
    website = models.ForeignKey('CoreWebsite', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    root_category_id = models.IntegerField()
    default_store_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'core_store_group'


class CoreTranslate(models.Model):
    key_id = models.IntegerField(primary_key=True)
    string = models.CharField(max_length=255)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    translate = models.CharField(max_length=255, blank=True, null=True)
    locale = models.CharField(max_length=20)
    crc_string = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'core_translate'
        unique_together = (('store', 'locale', 'crc_string', 'string'),)


class CoreUrlRewrite(models.Model):
    url_rewrite_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    id_path = models.CharField(max_length=255, blank=True, null=True)
    request_path = models.CharField(max_length=255, blank=True, null=True)
    target_path = models.CharField(max_length=255, blank=True, null=True)
    is_system = models.SmallIntegerField(blank=True, null=True)
    options = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(CatalogCategoryEntity, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_url_rewrite'
        unique_together = (('request_path', 'store'), ('id_path', 'is_system', 'store'),)


class CoreVariable(models.Model):
    variable_id = models.IntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_variable'


class CoreVariableValue(models.Model):
    value_id = models.IntegerField(primary_key=True)
    variable = models.ForeignKey(CoreVariable, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    plain_value = models.TextField(blank=True, null=True)
    html_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_variable_value'
        unique_together = (('variable', 'store'),)


class CoreWebsite(models.Model):
    website_id = models.SmallIntegerField(primary_key=True)
    code = models.CharField(unique=True, max_length=32, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    sort_order = models.SmallIntegerField()
    default_group_id = models.SmallIntegerField()
    is_default = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_website'


class CouponAggregated(models.Model):
    period = models.DateField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    coupon_uses = models.IntegerField()
    subtotal_amount = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_amount = models.DecimalField(max_digits=12, decimal_places=4)
    subtotal_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    total_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    rule_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon_aggregated'
        unique_together = (('period', 'store', 'order_status', 'coupon_code'),)


class CouponAggregatedOrder(models.Model):
    period = models.DateField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    coupon_uses = models.IntegerField()
    subtotal_amount = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_amount = models.DecimalField(max_digits=12, decimal_places=4)
    rule_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon_aggregated_order'
        unique_together = (('period', 'store', 'order_status', 'coupon_code'),)


class CouponAggregatedUpdated(models.Model):
    period = models.DateField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    coupon_uses = models.IntegerField()
    subtotal_amount = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_amount = models.DecimalField(max_digits=12, decimal_places=4)
    subtotal_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    total_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    rule_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon_aggregated_updated'
        unique_together = (('period', 'store', 'order_status', 'coupon_code'),)


class CronSchedule(models.Model):
    schedule_id = models.IntegerField(primary_key=True)
    job_code = models.CharField(max_length=255)
    status = models.CharField(max_length=7)
    messages = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    scheduled_at = models.DateTimeField(blank=True, null=True)
    executed_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cron_schedule'


class CustomerAddressEntity(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute_set_id = models.SmallIntegerField()
    increment_id = models.CharField(max_length=50, blank=True, null=True)
    parent = models.ForeignKey('CustomerEntity', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'customer_address_entity'


class CustomerAddressEntityDatetime(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    entity = models.ForeignKey(CustomerAddressEntity, models.DO_NOTHING)
    value = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_address_entity_datetime'
        unique_together = (('entity', 'attribute'),)


class CustomerAddressEntityDecimal(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    entity = models.ForeignKey(CustomerAddressEntity, models.DO_NOTHING)
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'customer_address_entity_decimal'
        unique_together = (('entity', 'attribute'),)


class CustomerAddressEntityInt(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    entity = models.ForeignKey(CustomerAddressEntity, models.DO_NOTHING)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_address_entity_int'
        unique_together = (('entity', 'attribute'),)


class CustomerAddressEntityText(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    entity = models.ForeignKey(CustomerAddressEntity, models.DO_NOTHING)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'customer_address_entity_text'
        unique_together = (('entity', 'attribute'),)


class CustomerAddressEntityVarchar(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    entity = models.ForeignKey(CustomerAddressEntity, models.DO_NOTHING)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_address_entity_varchar'
        unique_together = (('entity', 'attribute'),)


class CustomerEavAttribute(models.Model):
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING, primary_key=True)
    is_visible = models.SmallIntegerField()
    input_filter = models.CharField(max_length=255, blank=True, null=True)
    multiline_count = models.SmallIntegerField()
    validate_rules = models.TextField(blank=True, null=True)
    is_system = models.SmallIntegerField()
    sort_order = models.IntegerField()
    data_model = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_eav_attribute'


class CustomerEavAttributeWebsite(models.Model):
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    website = models.ForeignKey(CoreWebsite, models.DO_NOTHING)
    is_visible = models.SmallIntegerField(blank=True, null=True)
    is_required = models.SmallIntegerField(blank=True, null=True)
    default_value = models.TextField(blank=True, null=True)
    multiline_count = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_eav_attribute_website'
        unique_together = (('attribute', 'website'),)


class CustomerEntity(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute_set_id = models.SmallIntegerField()
    website = models.ForeignKey(CoreWebsite, models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    group_id = models.SmallIntegerField()
    increment_id = models.CharField(max_length=50, blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.SmallIntegerField()
    disable_auto_group_change = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'customer_entity'
        unique_together = (('email', 'website'),)


class CustomerEntityDatetime(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    entity = models.ForeignKey(CustomerEntity, models.DO_NOTHING)
    value = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer_entity_datetime'
        unique_together = (('entity', 'attribute'),)


class CustomerEntityDecimal(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    entity = models.ForeignKey(CustomerEntity, models.DO_NOTHING)
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'customer_entity_decimal'
        unique_together = (('entity', 'attribute'),)


class CustomerEntityInt(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    entity = models.ForeignKey(CustomerEntity, models.DO_NOTHING)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_entity_int'
        unique_together = (('entity', 'attribute'),)


class CustomerEntityText(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    entity = models.ForeignKey(CustomerEntity, models.DO_NOTHING)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'customer_entity_text'
        unique_together = (('entity', 'attribute'),)


class CustomerEntityVarchar(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)
    entity = models.ForeignKey(CustomerEntity, models.DO_NOTHING)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_entity_varchar'
        unique_together = (('entity', 'attribute'),)


class CustomerFormAttribute(models.Model):
    form_code = models.CharField(max_length=32)
    attribute = models.ForeignKey('EavAttribute', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'customer_form_attribute'
        unique_together = (('form_code', 'attribute'),)


class CustomerGroup(models.Model):
    customer_group_id = models.SmallIntegerField(primary_key=True)
    customer_group_code = models.CharField(max_length=32)
    tax_class_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer_group'


class DataflowBatch(models.Model):
    batch_id = models.IntegerField(primary_key=True)
    profile = models.ForeignKey('DataflowProfile', models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    adapter = models.CharField(max_length=128, blank=True, null=True)
    params = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataflow_batch'


class DataflowBatchExport(models.Model):
    batch_export_id = models.BigIntegerField(primary_key=True)
    batch = models.ForeignKey(DataflowBatch, models.DO_NOTHING)
    batch_data = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'dataflow_batch_export'


class DataflowBatchImport(models.Model):
    batch_import_id = models.BigIntegerField(primary_key=True)
    batch = models.ForeignKey(DataflowBatch, models.DO_NOTHING)
    batch_data = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'dataflow_batch_import'


class DataflowImportData(models.Model):
    import_id = models.IntegerField(primary_key=True)
    session = models.ForeignKey('DataflowSession', models.DO_NOTHING, blank=True, null=True)
    serial_number = models.IntegerField()
    value = models.TextField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dataflow_import_data'


class DataflowProfile(models.Model):
    profile_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    actions_xml = models.TextField(blank=True, null=True)
    gui_data = models.TextField(blank=True, null=True)
    direction = models.CharField(max_length=6, blank=True, null=True)
    entity_type = models.CharField(max_length=64, blank=True, null=True)
    store_id = models.SmallIntegerField()
    data_transfer = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataflow_profile'


class DataflowProfileHistory(models.Model):
    history_id = models.IntegerField(primary_key=True)
    profile = models.ForeignKey(DataflowProfile, models.DO_NOTHING)
    action_code = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.IntegerField()
    performed_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataflow_profile_history'


class DataflowSession(models.Model):
    session_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    file = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    direction = models.CharField(max_length=32, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dataflow_session'


class DesignChange(models.Model):
    design_change_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    design = models.CharField(max_length=255, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design_change'


class DirectoryCountry(models.Model):
    country_id = models.CharField(primary_key=True, max_length=2)
    iso2_code = models.CharField(max_length=2, blank=True, null=True)
    iso3_code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directory_country'


class DirectoryCountryFormat(models.Model):
    country_format_id = models.IntegerField(primary_key=True)
    country_id = models.CharField(max_length=2, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    format = models.TextField()

    class Meta:
        managed = False
        db_table = 'directory_country_format'
        unique_together = (('country_id', 'type'),)


class DirectoryCountryRegion(models.Model):
    region_id = models.IntegerField(primary_key=True)
    country_id = models.CharField(max_length=4)
    code = models.CharField(max_length=32, blank=True, null=True)
    default_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directory_country_region'


class DirectoryCountryRegionName(models.Model):
    locale = models.CharField(max_length=8)
    region = models.ForeignKey(DirectoryCountryRegion, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directory_country_region_name'
        unique_together = (('locale', 'region'),)


class DirectoryCurrencyRate(models.Model):
    currency_from = models.CharField(max_length=3)
    currency_to = models.CharField(max_length=3)
    rate = models.DecimalField(max_digits=24, decimal_places=12)

    class Meta:
        managed = False
        db_table = 'directory_currency_rate'
        unique_together = (('currency_from', 'currency_to'),)


class DownloadableLink(models.Model):
    link_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    sort_order = models.IntegerField()
    number_of_downloads = models.IntegerField(blank=True, null=True)
    is_shareable = models.SmallIntegerField()
    link_url = models.CharField(max_length=255, blank=True, null=True)
    link_file = models.CharField(max_length=255, blank=True, null=True)
    link_type = models.CharField(max_length=20, blank=True, null=True)
    sample_url = models.CharField(max_length=255, blank=True, null=True)
    sample_file = models.CharField(max_length=255, blank=True, null=True)
    sample_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'downloadable_link'


class DownloadableLinkPrice(models.Model):
    price_id = models.IntegerField(primary_key=True)
    link = models.ForeignKey(DownloadableLink, models.DO_NOTHING)
    website = models.ForeignKey(CoreWebsite, models.DO_NOTHING)
    price = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'downloadable_link_price'


class DownloadableLinkPurchased(models.Model):
    purchased_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey('SalesFlatOrder', models.DO_NOTHING, blank=True, null=True)
    order_increment_id = models.CharField(max_length=50, blank=True, null=True)
    order_item_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_sku = models.CharField(max_length=255, blank=True, null=True)
    link_section_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'downloadable_link_purchased'


class DownloadableLinkPurchasedItem(models.Model):
    item_id = models.IntegerField(primary_key=True)
    purchased = models.ForeignKey(DownloadableLinkPurchased, models.DO_NOTHING)
    order_item = models.ForeignKey('SalesFlatOrderItem', models.DO_NOTHING, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    link_hash = models.CharField(max_length=255, blank=True, null=True)
    number_of_downloads_bought = models.IntegerField()
    number_of_downloads_used = models.IntegerField()
    link_id = models.IntegerField()
    link_title = models.CharField(max_length=255, blank=True, null=True)
    is_shareable = models.SmallIntegerField()
    link_url = models.CharField(max_length=255, blank=True, null=True)
    link_file = models.CharField(max_length=255, blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'downloadable_link_purchased_item'


class DownloadableLinkTitle(models.Model):
    title_id = models.IntegerField(primary_key=True)
    link = models.ForeignKey(DownloadableLink, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'downloadable_link_title'
        unique_together = (('link', 'store'),)


class DownloadableSample(models.Model):
    sample_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    sample_url = models.CharField(max_length=255, blank=True, null=True)
    sample_file = models.CharField(max_length=255, blank=True, null=True)
    sample_type = models.CharField(max_length=20, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'downloadable_sample'


class DownloadableSampleTitle(models.Model):
    title_id = models.IntegerField(primary_key=True)
    sample = models.ForeignKey(DownloadableSample, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'downloadable_sample_title'
        unique_together = (('sample', 'store'),)


class EavAttribute(models.Model):
    attribute_id = models.SmallIntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute_code = models.CharField(max_length=255, blank=True, null=True)
    attribute_model = models.CharField(max_length=255, blank=True, null=True)
    backend_model = models.CharField(max_length=255, blank=True, null=True)
    backend_type = models.CharField(max_length=8)
    backend_table = models.CharField(max_length=255, blank=True, null=True)
    frontend_model = models.CharField(max_length=255, blank=True, null=True)
    frontend_input = models.CharField(max_length=50, blank=True, null=True)
    frontend_label = models.CharField(max_length=255, blank=True, null=True)
    frontend_class = models.CharField(max_length=255, blank=True, null=True)
    source_model = models.CharField(max_length=255, blank=True, null=True)
    is_required = models.SmallIntegerField()
    is_user_defined = models.SmallIntegerField()
    default_value = models.TextField(blank=True, null=True)
    is_unique = models.SmallIntegerField()
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_attribute'
        unique_together = (('entity_type', 'attribute_code'),)


class EavAttributeGroup(models.Model):
    attribute_group_id = models.SmallIntegerField(primary_key=True)
    attribute_set = models.ForeignKey('EavAttributeSet', models.DO_NOTHING)
    attribute_group_name = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.SmallIntegerField()
    default_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_attribute_group'
        unique_together = (('attribute_set', 'attribute_group_name'),)


class EavAttributeLabel(models.Model):
    attribute_label_id = models.IntegerField(primary_key=True)
    attribute = models.ForeignKey(EavAttribute, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_attribute_label'


class EavAttributeOption(models.Model):
    option_id = models.IntegerField(primary_key=True)
    attribute = models.ForeignKey(EavAttribute, models.DO_NOTHING)
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'eav_attribute_option'


class EavAttributeOptionValue(models.Model):
    value_id = models.IntegerField(primary_key=True)
    option = models.ForeignKey(EavAttributeOption, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_attribute_option_value'


class EavAttributeSet(models.Model):
    attribute_set_id = models.SmallIntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute_set_name = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'eav_attribute_set'
        unique_together = (('entity_type', 'attribute_set_name'),)


class EavEntity(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute_set_id = models.SmallIntegerField()
    increment_id = models.CharField(max_length=50, blank=True, null=True)
    parent_id = models.IntegerField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    is_active = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'eav_entity'


class EavEntityAttribute(models.Model):
    entity_attribute_id = models.IntegerField(primary_key=True)
    entity_type_id = models.SmallIntegerField()
    attribute_set_id = models.SmallIntegerField()
    attribute_group = models.ForeignKey(EavAttributeGroup, models.DO_NOTHING)
    attribute = models.ForeignKey(EavAttribute, models.DO_NOTHING)
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'eav_entity_attribute'
        unique_together = (('attribute_set_id', 'attribute'), ('attribute_group', 'attribute'),)


class EavEntityDatetime(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute_id = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    entity = models.ForeignKey(EavEntity, models.DO_NOTHING)
    value = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eav_entity_datetime'
        unique_together = (('entity', 'attribute_id', 'store'),)


class EavEntityDecimal(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute_id = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    entity = models.ForeignKey(EavEntity, models.DO_NOTHING)
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'eav_entity_decimal'
        unique_together = (('entity', 'attribute_id', 'store'),)


class EavEntityInt(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute_id = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    entity = models.ForeignKey(EavEntity, models.DO_NOTHING)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eav_entity_int'
        unique_together = (('entity', 'attribute_id', 'store'),)


class EavEntityStore(models.Model):
    entity_store_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    increment_prefix = models.CharField(max_length=20, blank=True, null=True)
    increment_last_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_entity_store'


class EavEntityText(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey('EavEntityType', models.DO_NOTHING)
    attribute_id = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    entity = models.ForeignKey(EavEntity, models.DO_NOTHING)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'eav_entity_text'
        unique_together = (('entity', 'attribute_id', 'store'),)


class EavEntityType(models.Model):
    entity_type_id = models.SmallIntegerField(primary_key=True)
    entity_type_code = models.CharField(max_length=50)
    entity_model = models.CharField(max_length=255)
    attribute_model = models.CharField(max_length=255, blank=True, null=True)
    entity_table = models.CharField(max_length=255, blank=True, null=True)
    value_table_prefix = models.CharField(max_length=255, blank=True, null=True)
    entity_id_field = models.CharField(max_length=255, blank=True, null=True)
    is_data_sharing = models.SmallIntegerField()
    data_sharing_key = models.CharField(max_length=100, blank=True, null=True)
    default_attribute_set_id = models.SmallIntegerField()
    increment_model = models.CharField(max_length=255, blank=True, null=True)
    increment_per_store = models.SmallIntegerField()
    increment_pad_length = models.SmallIntegerField()
    increment_pad_char = models.CharField(max_length=1)
    additional_attribute_table = models.CharField(max_length=255, blank=True, null=True)
    entity_attribute_collection = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_entity_type'


class EavEntityVarchar(models.Model):
    value_id = models.IntegerField(primary_key=True)
    entity_type = models.ForeignKey(EavEntityType, models.DO_NOTHING)
    attribute_id = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    entity = models.ForeignKey(EavEntity, models.DO_NOTHING)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eav_entity_varchar'
        unique_together = (('entity', 'attribute_id', 'store'),)


class EavFormElement(models.Model):
    element_id = models.IntegerField(primary_key=True)
    type = models.ForeignKey('EavFormType', models.DO_NOTHING)
    fieldset = models.ForeignKey('EavFormFieldset', models.DO_NOTHING, blank=True, null=True)
    attribute = models.ForeignKey(EavAttribute, models.DO_NOTHING)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eav_form_element'
        unique_together = (('type', 'attribute'),)


class EavFormFieldset(models.Model):
    fieldset_id = models.SmallIntegerField(primary_key=True)
    type = models.ForeignKey('EavFormType', models.DO_NOTHING)
    code = models.CharField(max_length=64)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eav_form_fieldset'
        unique_together = (('type', 'code'),)


class EavFormFieldsetLabel(models.Model):
    fieldset = models.ForeignKey(EavFormFieldset, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    label = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'eav_form_fieldset_label'
        unique_together = (('fieldset', 'store'),)


class EavFormType(models.Model):
    type_id = models.SmallIntegerField(primary_key=True)
    code = models.CharField(max_length=64)
    label = models.CharField(max_length=255)
    is_system = models.SmallIntegerField()
    theme = models.CharField(max_length=64, blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'eav_form_type'
        unique_together = (('code', 'theme', 'store'),)


class EavFormTypeEntity(models.Model):
    type = models.ForeignKey(EavFormType, models.DO_NOTHING)
    entity_type = models.ForeignKey(EavEntityType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'eav_form_type_entity'
        unique_together = (('type', 'entity_type'),)


class GiftMessage(models.Model):
    gift_message_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    sender = models.CharField(max_length=255, blank=True, null=True)
    recipient = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gift_message'


class ImportexportImportdata(models.Model):
    entity = models.CharField(max_length=50)
    behavior = models.CharField(max_length=10)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'importexport_importdata'


class IndexEvent(models.Model):
    event_id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=64)
    entity = models.CharField(max_length=64)
    entity_pk = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    old_data = models.TextField(blank=True, null=True)
    new_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_event'
        unique_together = (('type', 'entity', 'entity_pk'),)


class IndexProcess(models.Model):
    process_id = models.IntegerField(primary_key=True)
    indexer_code = models.CharField(unique=True, max_length=32)
    status = models.CharField(max_length=15)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    mode = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'index_process'


class IndexProcessEvent(models.Model):
    process = models.ForeignKey(IndexProcess, models.DO_NOTHING)
    event = models.ForeignKey(IndexEvent, models.DO_NOTHING)
    status = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'index_process_event'
        unique_together = (('process', 'event'),)


class LogCustomer(models.Model):
    log_id = models.IntegerField(primary_key=True)
    visitor_id = models.BigIntegerField(blank=True, null=True)
    customer_id = models.IntegerField()
    login_at = models.DateTimeField()
    logout_at = models.DateTimeField(blank=True, null=True)
    store_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'log_customer'


class LogQuote(models.Model):
    quote_id = models.IntegerField(primary_key=True)
    visitor_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_quote'


class LogSummary(models.Model):
    summary_id = models.BigIntegerField(primary_key=True)
    store_id = models.SmallIntegerField()
    type_id = models.SmallIntegerField(blank=True, null=True)
    visitor_count = models.IntegerField()
    customer_count = models.IntegerField()
    add_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log_summary'


class LogSummaryType(models.Model):
    type_id = models.SmallIntegerField(primary_key=True)
    type_code = models.CharField(max_length=64, blank=True, null=True)
    period = models.SmallIntegerField()
    period_type = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'log_summary_type'


class LogUrl(models.Model):
    url_id = models.BigIntegerField()
    visitor_id = models.BigIntegerField(blank=True, null=True)
    visit_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'log_url'


class LogUrlInfo(models.Model):
    url_id = models.BigIntegerField(primary_key=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_url_info'


class LogVisitor(models.Model):
    visitor_id = models.BigIntegerField(primary_key=True)
    session_id = models.CharField(max_length=64, blank=True, null=True)
    first_visit_at = models.DateTimeField(blank=True, null=True)
    last_visit_at = models.DateTimeField()
    last_url_id = models.BigIntegerField()
    store_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'log_visitor'


class LogVisitorInfo(models.Model):
    visitor_id = models.BigIntegerField(primary_key=True)
    http_referer = models.CharField(max_length=255, blank=True, null=True)
    http_user_agent = models.CharField(max_length=255, blank=True, null=True)
    http_accept_charset = models.CharField(max_length=255, blank=True, null=True)
    http_accept_language = models.CharField(max_length=255, blank=True, null=True)
    server_addr = models.CharField(max_length=16, blank=True, null=True)
    remote_addr = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_visitor_info'


class LogVisitorOnline(models.Model):
    visitor_id = models.BigIntegerField(primary_key=True)
    visitor_type = models.CharField(max_length=1)
    remote_addr = models.CharField(max_length=16, blank=True, null=True)
    first_visit_at = models.DateTimeField(blank=True, null=True)
    last_visit_at = models.DateTimeField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    last_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_visitor_online'


class NewsletterProblem(models.Model):
    problem_id = models.IntegerField(primary_key=True)
    subscriber = models.ForeignKey('NewsletterSubscriber', models.DO_NOTHING, blank=True, null=True)
    queue = models.ForeignKey('NewsletterQueue', models.DO_NOTHING)
    problem_error_code = models.IntegerField(blank=True, null=True)
    problem_error_text = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter_problem'


class NewsletterQueue(models.Model):
    queue_id = models.IntegerField(primary_key=True)
    template = models.ForeignKey('NewsletterTemplate', models.DO_NOTHING)
    newsletter_type = models.IntegerField(blank=True, null=True)
    newsletter_text = models.TextField(blank=True, null=True)
    newsletter_styles = models.TextField(blank=True, null=True)
    newsletter_subject = models.CharField(max_length=200, blank=True, null=True)
    newsletter_sender_name = models.CharField(max_length=200, blank=True, null=True)
    newsletter_sender_email = models.CharField(max_length=200, blank=True, null=True)
    queue_status = models.IntegerField()
    queue_start_at = models.DateTimeField(blank=True, null=True)
    queue_finish_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter_queue'


class NewsletterQueueLink(models.Model):
    queue_link_id = models.IntegerField(primary_key=True)
    queue = models.ForeignKey(NewsletterQueue, models.DO_NOTHING)
    subscriber = models.ForeignKey('NewsletterSubscriber', models.DO_NOTHING)
    letter_sent_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter_queue_link'


class NewsletterQueueStoreLink(models.Model):
    queue = models.ForeignKey(NewsletterQueue, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'newsletter_queue_store_link'
        unique_together = (('queue', 'store'),)


class NewsletterSubscriber(models.Model):
    subscriber_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    change_status_at = models.DateTimeField(blank=True, null=True)
    customer_id = models.IntegerField()
    subscriber_email = models.CharField(max_length=150, blank=True, null=True)
    subscriber_status = models.IntegerField()
    subscriber_confirm_code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter_subscriber'


class NewsletterTemplate(models.Model):
    template_id = models.IntegerField(primary_key=True)
    template_code = models.CharField(max_length=150, blank=True, null=True)
    template_text = models.TextField(blank=True, null=True)
    template_text_preprocessed = models.TextField(blank=True, null=True)
    template_styles = models.TextField(blank=True, null=True)
    template_type = models.IntegerField(blank=True, null=True)
    template_subject = models.CharField(max_length=200, blank=True, null=True)
    template_sender_name = models.CharField(max_length=200, blank=True, null=True)
    template_sender_email = models.CharField(max_length=200, blank=True, null=True)
    template_actual = models.SmallIntegerField(blank=True, null=True)
    added_at = models.DateTimeField(blank=True, null=True)
    modified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter_template'


class OauthConsumer(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    key = models.CharField(unique=True, max_length=32)
    secret = models.CharField(unique=True, max_length=32)
    callback_url = models.CharField(max_length=255, blank=True, null=True)
    rejected_callback_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oauth_consumer'


class OauthNonce(models.Model):
    nonce = models.CharField(unique=True, max_length=32)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oauth_nonce'


class OauthToken(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    consumer = models.ForeignKey(OauthConsumer, models.DO_NOTHING)
    admin = models.ForeignKey(AdminUser, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, blank=True, null=True)
    type = models.CharField(max_length=16)
    token = models.CharField(unique=True, max_length=32)
    secret = models.CharField(max_length=32)
    verifier = models.CharField(max_length=32, blank=True, null=True)
    callback_url = models.CharField(max_length=255)
    revoked = models.SmallIntegerField()
    authorized = models.SmallIntegerField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oauth_token'


class PaypalCert(models.Model):
    cert_id = models.SmallIntegerField(primary_key=True)
    website = models.ForeignKey(CoreWebsite, models.DO_NOTHING)
    content = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_cert'


class PaypalPaymentTransaction(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    txn_id = models.CharField(unique=True, max_length=100, blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_payment_transaction'


class PaypalSettlementReport(models.Model):
    report_id = models.IntegerField(primary_key=True)
    report_date = models.DateTimeField(blank=True, null=True)
    account_id = models.CharField(max_length=64, blank=True, null=True)
    filename = models.CharField(max_length=24, blank=True, null=True)
    last_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_settlement_report'
        unique_together = (('report_date', 'account_id'),)


class PaypalSettlementReportRow(models.Model):
    row_id = models.IntegerField(primary_key=True)
    report = models.ForeignKey(PaypalSettlementReport, models.DO_NOTHING)
    transaction_id = models.CharField(max_length=19, blank=True, null=True)
    invoice_id = models.CharField(max_length=127, blank=True, null=True)
    paypal_reference_id = models.CharField(max_length=19, blank=True, null=True)
    paypal_reference_id_type = models.CharField(max_length=3, blank=True, null=True)
    transaction_event_code = models.CharField(max_length=5, blank=True, null=True)
    transaction_initiation_date = models.DateTimeField(blank=True, null=True)
    transaction_completion_date = models.DateTimeField(blank=True, null=True)
    transaction_debit_or_credit = models.CharField(max_length=2)
    gross_transaction_amount = models.DecimalField(max_digits=20, decimal_places=6)
    gross_transaction_currency = models.CharField(max_length=3, blank=True, null=True)
    fee_debit_or_credit = models.CharField(max_length=2, blank=True, null=True)
    fee_amount = models.DecimalField(max_digits=20, decimal_places=6)
    fee_currency = models.CharField(max_length=3, blank=True, null=True)
    custom_field = models.CharField(max_length=255, blank=True, null=True)
    consumer_id = models.CharField(max_length=127, blank=True, null=True)
    payment_tracking_id = models.CharField(max_length=255, blank=True, null=True)
    store_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paypal_settlement_report_row'


class PermissionBlock(models.Model):
    block_id = models.IntegerField(primary_key=True)
    block_name = models.CharField(unique=True, max_length=255)
    is_allowed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permission_block'


class PermissionVariable(models.Model):
    variable_id = models.IntegerField()
    variable_name = models.CharField(unique=True, max_length=255)
    is_allowed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permission_variable'
        unique_together = (('variable_id', 'variable_name'),)


class PersistentSession(models.Model):
    persistent_id = models.IntegerField(primary_key=True)
    key = models.CharField(unique=True, max_length=50)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, unique=True, blank=True, null=True)
    website = models.ForeignKey(CoreWebsite, models.DO_NOTHING)
    info = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persistent_session'


class Poll(models.Model):
    poll_id = models.IntegerField(primary_key=True)
    poll_title = models.CharField(max_length=255, blank=True, null=True)
    votes_count = models.IntegerField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    date_posted = models.DateTimeField()
    date_closed = models.DateTimeField(blank=True, null=True)
    active = models.SmallIntegerField()
    closed = models.SmallIntegerField()
    answers_display = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poll'


class PollAnswer(models.Model):
    answer_id = models.IntegerField(primary_key=True)
    poll = models.ForeignKey(Poll, models.DO_NOTHING)
    answer_title = models.CharField(max_length=255, blank=True, null=True)
    votes_count = models.IntegerField()
    answer_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'poll_answer'


class PollStore(models.Model):
    poll = models.ForeignKey(Poll, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'poll_store'
        unique_together = (('poll', 'store'),)


class PollVote(models.Model):
    vote_id = models.IntegerField(primary_key=True)
    poll_id = models.IntegerField()
    poll_answer = models.ForeignKey(PollAnswer, models.DO_NOTHING)
    ip_address = models.CharField(max_length=16, blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    vote_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poll_vote'


class ProductAlertPrice(models.Model):
    alert_price_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    website = models.ForeignKey(CoreWebsite, models.DO_NOTHING)
    add_date = models.DateTimeField()
    last_send_date = models.DateTimeField(blank=True, null=True)
    send_count = models.SmallIntegerField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'product_alert_price'


class ProductAlertStock(models.Model):
    alert_stock_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    website = models.ForeignKey(CoreWebsite, models.DO_NOTHING)
    add_date = models.DateTimeField()
    send_date = models.DateTimeField(blank=True, null=True)
    send_count = models.SmallIntegerField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'product_alert_stock'


class Rating(models.Model):
    rating_id = models.SmallIntegerField(primary_key=True)
    entity = models.ForeignKey('RatingEntity', models.DO_NOTHING)
    rating_code = models.CharField(unique=True, max_length=64)
    position = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'rating'


class RatingEntity(models.Model):
    entity_id = models.SmallIntegerField(primary_key=True)
    entity_code = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'rating_entity'


class RatingOption(models.Model):
    option_id = models.IntegerField(primary_key=True)
    rating = models.ForeignKey(Rating, models.DO_NOTHING)
    code = models.CharField(max_length=32)
    value = models.SmallIntegerField()
    position = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'rating_option'


class RatingOptionVote(models.Model):
    vote_id = models.BigIntegerField(primary_key=True)
    option = models.ForeignKey(RatingOption, models.DO_NOTHING)
    remote_ip = models.CharField(max_length=50, blank=True, null=True)
    remote_ip_long = models.CharField(max_length=16, blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    entity_pk_value = models.BigIntegerField()
    rating_id = models.SmallIntegerField()
    review = models.ForeignKey('Review', models.DO_NOTHING, blank=True, null=True)
    percent = models.SmallIntegerField()
    value = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'rating_option_vote'


class RatingOptionVoteAggregated(models.Model):
    primary_id = models.IntegerField(primary_key=True)
    rating = models.ForeignKey(Rating, models.DO_NOTHING)
    entity_pk_value = models.BigIntegerField()
    vote_count = models.IntegerField()
    vote_value_sum = models.IntegerField()
    percent = models.SmallIntegerField()
    percent_approved = models.SmallIntegerField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rating_option_vote_aggregated'


class RatingStore(models.Model):
    rating = models.ForeignKey(Rating, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rating_store'
        unique_together = (('rating', 'store'),)


class RatingTitle(models.Model):
    rating = models.ForeignKey(Rating, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'rating_title'
        unique_together = (('rating', 'store'),)


class ReportComparedProductIndex(models.Model):
    index_id = models.BigIntegerField(primary_key=True)
    visitor_id = models.IntegerField(blank=True, null=True)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    added_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'report_compared_product_index'
        unique_together = (('visitor_id', 'product'), ('customer', 'product'),)


class ReportEvent(models.Model):
    event_id = models.BigIntegerField(primary_key=True)
    logged_at = models.DateTimeField()
    event_type = models.ForeignKey('ReportEventTypes', models.DO_NOTHING)
    object_id = models.IntegerField()
    subject_id = models.IntegerField()
    subtype = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'report_event'


class ReportEventTypes(models.Model):
    event_type_id = models.SmallIntegerField(primary_key=True)
    event_name = models.CharField(max_length=64)
    customer_login = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'report_event_types'


class ReportViewedProductAggregatedDaily(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=4)
    views_num = models.IntegerField()
    rating_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'report_viewed_product_aggregated_daily'
        unique_together = (('period', 'store', 'product'),)


class ReportViewedProductAggregatedMonthly(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=4)
    views_num = models.IntegerField()
    rating_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'report_viewed_product_aggregated_monthly'
        unique_together = (('period', 'store', 'product'),)


class ReportViewedProductAggregatedYearly(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=4)
    views_num = models.IntegerField()
    rating_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'report_viewed_product_aggregated_yearly'
        unique_together = (('period', 'store', 'product'),)


class ReportViewedProductIndex(models.Model):
    index_id = models.BigIntegerField(primary_key=True)
    visitor_id = models.IntegerField(blank=True, null=True)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    added_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'report_viewed_product_index'
        unique_together = (('customer', 'product'), ('visitor_id', 'product'),)


class Review(models.Model):
    review_id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField()
    entity = models.ForeignKey('ReviewEntity', models.DO_NOTHING)
    entity_pk_value = models.IntegerField()
    status = models.ForeignKey('ReviewStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'review'


class ReviewDetail(models.Model):
    detail_id = models.BigIntegerField(primary_key=True)
    review = models.ForeignKey(Review, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255)
    detail = models.TextField()
    nickname = models.CharField(max_length=128)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review_detail'


class ReviewEntity(models.Model):
    entity_id = models.SmallIntegerField(primary_key=True)
    entity_code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'review_entity'


class ReviewEntitySummary(models.Model):
    primary_id = models.BigIntegerField(primary_key=True)
    entity_pk_value = models.BigIntegerField()
    entity_type = models.SmallIntegerField()
    reviews_count = models.SmallIntegerField()
    rating_summary = models.SmallIntegerField()
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'review_entity_summary'


class ReviewStatus(models.Model):
    status_id = models.SmallIntegerField(primary_key=True)
    status_code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'review_status'


class ReviewStore(models.Model):
    review = models.ForeignKey(Review, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'review_store'
        unique_together = (('review', 'store'),)


class SalesBestsellersAggregatedDaily(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=4)
    qty_ordered = models.DecimalField(max_digits=12, decimal_places=4)
    rating_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sales_bestsellers_aggregated_daily'
        unique_together = (('period', 'store', 'product'),)


class SalesBestsellersAggregatedMonthly(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=4)
    qty_ordered = models.DecimalField(max_digits=12, decimal_places=4)
    rating_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sales_bestsellers_aggregated_monthly'
        unique_together = (('period', 'store', 'product'),)


class SalesBestsellersAggregatedYearly(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_price = models.DecimalField(max_digits=12, decimal_places=4)
    qty_ordered = models.DecimalField(max_digits=12, decimal_places=4)
    rating_pos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sales_bestsellers_aggregated_yearly'
        unique_together = (('period', 'store', 'product'),)


class SalesBillingAgreement(models.Model):
    agreement_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING)
    method_code = models.CharField(max_length=32)
    reference_id = models.CharField(max_length=32)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    agreement_label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_billing_agreement'


class SalesBillingAgreementOrder(models.Model):
    agreement = models.ForeignKey(SalesBillingAgreement, models.DO_NOTHING)
    order = models.ForeignKey('SalesFlatOrder', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sales_billing_agreement_order'
        unique_together = (('agreement', 'order'),)


class SalesFlatCreditmemo(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    adjustment_positive = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_adjustment_negative = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    adjustment_negative = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_base_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_global_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_adjustment = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    adjustment = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_adjustment_positive = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    order = models.ForeignKey('SalesFlatOrder', models.DO_NOTHING)
    email_sent = models.SmallIntegerField(blank=True, null=True)
    creditmemo_status = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    shipping_address_id = models.IntegerField(blank=True, null=True)
    billing_address_id = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    store_currency_code = models.CharField(max_length=3, blank=True, null=True)
    order_currency_code = models.CharField(max_length=3, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    global_currency_code = models.CharField(max_length=3, blank=True, null=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_hidden_tax_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_creditmemo'


class SalesFlatCreditmemoComment(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey(SalesFlatCreditmemo, models.DO_NOTHING)
    is_customer_notified = models.IntegerField(blank=True, null=True)
    is_visible_on_front = models.SmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_creditmemo_comment'


class SalesFlatCreditmemoGrid(models.Model):
    entity = models.ForeignKey(SalesFlatCreditmemo, models.DO_NOTHING, primary_key=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    store_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_base_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_global_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    order_id = models.IntegerField()
    creditmemo_status = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    invoice_id = models.IntegerField(blank=True, null=True)
    store_currency_code = models.CharField(max_length=3, blank=True, null=True)
    order_currency_code = models.CharField(max_length=3, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    global_currency_code = models.CharField(max_length=3, blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    order_increment_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    order_created_at = models.DateTimeField(blank=True, null=True)
    billing_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_creditmemo_grid'


class SalesFlatCreditmemoItem(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey(SalesFlatCreditmemo, models.DO_NOTHING)
    base_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    order_item_id = models.IntegerField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied = models.TextField(blank=True, null=True)
    base_weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_applied_row_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_row_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_creditmemo_item'


class SalesFlatInvoice(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_base_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_global_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    billing_address_id = models.IntegerField(blank=True, null=True)
    is_used_for_refund = models.SmallIntegerField(blank=True, null=True)
    order = models.ForeignKey('SalesFlatOrder', models.DO_NOTHING)
    email_sent = models.SmallIntegerField(blank=True, null=True)
    can_void_flag = models.SmallIntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    shipping_address_id = models.IntegerField(blank=True, null=True)
    store_currency_code = models.CharField(max_length=3, blank=True, null=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    order_currency_code = models.CharField(max_length=3, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    global_currency_code = models.CharField(max_length=3, blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_hidden_tax_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_invoice'


class SalesFlatInvoiceComment(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey(SalesFlatInvoice, models.DO_NOTHING)
    is_customer_notified = models.SmallIntegerField(blank=True, null=True)
    is_visible_on_front = models.SmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_invoice_comment'


class SalesFlatInvoiceGrid(models.Model):
    entity = models.ForeignKey(SalesFlatInvoice, models.DO_NOTHING, primary_key=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    order_id = models.IntegerField()
    state = models.IntegerField(blank=True, null=True)
    store_currency_code = models.CharField(max_length=3, blank=True, null=True)
    order_currency_code = models.CharField(max_length=3, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    global_currency_code = models.CharField(max_length=3, blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    order_increment_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    order_created_at = models.DateTimeField(blank=True, null=True)
    billing_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_invoice_grid'


class SalesFlatInvoiceItem(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey(SalesFlatInvoice, models.DO_NOTHING)
    base_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    order_item_id = models.IntegerField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_applied_row_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_row_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied = models.TextField(blank=True, null=True)
    weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_invoice_item'


class SalesFlatOrder(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    coupon_code = models.CharField(max_length=255, blank=True, null=True)
    protect_code = models.CharField(max_length=255, blank=True, null=True)
    shipping_description = models.CharField(max_length=255, blank=True, null=True)
    is_virtual = models.SmallIntegerField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_global_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_invoiced_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_offline_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_online_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_qty_ordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_base_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_order_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_offline_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_online_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_qty_ordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    can_ship_partially = models.SmallIntegerField(blank=True, null=True)
    can_ship_partially_item = models.SmallIntegerField(blank=True, null=True)
    customer_is_guest = models.SmallIntegerField(blank=True, null=True)
    customer_note_notify = models.SmallIntegerField(blank=True, null=True)
    billing_address_id = models.IntegerField(blank=True, null=True)
    customer_group_id = models.SmallIntegerField(blank=True, null=True)
    edit_increment = models.IntegerField(blank=True, null=True)
    email_sent = models.SmallIntegerField(blank=True, null=True)
    forced_shipment_with_invoice = models.SmallIntegerField(blank=True, null=True)
    payment_auth_expiration = models.IntegerField(blank=True, null=True)
    quote_address_id = models.IntegerField(blank=True, null=True)
    quote_id = models.IntegerField(blank=True, null=True)
    shipping_address_id = models.IntegerField(blank=True, null=True)
    adjustment_negative = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    adjustment_positive = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_adjustment_negative = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_adjustment_positive = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_due = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    payment_authorization_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_due = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    customer_dob = models.DateTimeField(blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    applied_rule_ids = models.CharField(max_length=255, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    customer_firstname = models.CharField(max_length=255, blank=True, null=True)
    customer_lastname = models.CharField(max_length=255, blank=True, null=True)
    customer_middlename = models.CharField(max_length=255, blank=True, null=True)
    customer_prefix = models.CharField(max_length=255, blank=True, null=True)
    customer_suffix = models.CharField(max_length=255, blank=True, null=True)
    customer_taxvat = models.CharField(max_length=255, blank=True, null=True)
    discount_description = models.CharField(max_length=255, blank=True, null=True)
    ext_customer_id = models.CharField(max_length=255, blank=True, null=True)
    ext_order_id = models.CharField(max_length=255, blank=True, null=True)
    global_currency_code = models.CharField(max_length=3, blank=True, null=True)
    hold_before_state = models.CharField(max_length=255, blank=True, null=True)
    hold_before_status = models.CharField(max_length=255, blank=True, null=True)
    order_currency_code = models.CharField(max_length=255, blank=True, null=True)
    original_increment_id = models.CharField(max_length=50, blank=True, null=True)
    relation_child_id = models.CharField(max_length=32, blank=True, null=True)
    relation_child_real_id = models.CharField(max_length=32, blank=True, null=True)
    relation_parent_id = models.CharField(max_length=32, blank=True, null=True)
    relation_parent_real_id = models.CharField(max_length=32, blank=True, null=True)
    remote_ip = models.CharField(max_length=255, blank=True, null=True)
    shipping_method = models.CharField(max_length=255, blank=True, null=True)
    store_currency_code = models.CharField(max_length=3, blank=True, null=True)
    store_name = models.CharField(max_length=255, blank=True, null=True)
    x_forwarded_for = models.CharField(max_length=255, blank=True, null=True)
    customer_note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    total_item_count = models.SmallIntegerField()
    customer_gender = models.IntegerField(blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_hidden_tax_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    coupon_rule_name = models.CharField(max_length=255, blank=True, null=True)
    paypal_ipn_customer_notified = models.IntegerField(blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_order'


class SalesFlatOrderAddress(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey(SalesFlatOrder, models.DO_NOTHING, blank=True, null=True)
    customer_address_id = models.IntegerField(blank=True, null=True)
    quote_address_id = models.IntegerField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.CharField(max_length=2, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    address_type = models.CharField(max_length=255, blank=True, null=True)
    prefix = models.CharField(max_length=255, blank=True, null=True)
    middlename = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=255, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    vat_id = models.TextField(blank=True, null=True)
    vat_is_valid = models.SmallIntegerField(blank=True, null=True)
    vat_request_id = models.TextField(blank=True, null=True)
    vat_request_date = models.TextField(blank=True, null=True)
    vat_request_success = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_order_address'


class SalesFlatOrderGrid(models.Model):
    entity = models.ForeignKey(SalesFlatOrder, models.DO_NOTHING, primary_key=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    store_name = models.CharField(max_length=255, blank=True, null=True)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_total_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    base_currency_code = models.CharField(max_length=3, blank=True, null=True)
    order_currency_code = models.CharField(max_length=255, blank=True, null=True)
    shipping_name = models.CharField(max_length=255, blank=True, null=True)
    billing_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_order_grid'


class SalesFlatOrderItem(models.Model):
    item_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(SalesFlatOrder, models.DO_NOTHING)
    parent_item_id = models.IntegerField(blank=True, null=True)
    quote_item_id = models.IntegerField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    product_id = models.IntegerField(blank=True, null=True)
    product_type = models.CharField(max_length=255, blank=True, null=True)
    product_options = models.TextField(blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    is_virtual = models.SmallIntegerField(blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    applied_rule_ids = models.TextField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    free_shipping = models.SmallIntegerField()
    is_qty_decimal = models.SmallIntegerField(blank=True, null=True)
    no_discount = models.SmallIntegerField()
    qty_backordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty_ordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty_shipped = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    base_price = models.DecimalField(max_digits=12, decimal_places=4)
    original_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_original_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total = models.DecimalField(max_digits=12, decimal_places=4)
    base_row_total = models.DecimalField(max_digits=12, decimal_places=4)
    row_invoiced = models.DecimalField(max_digits=12, decimal_places=4)
    base_row_invoiced = models.DecimalField(max_digits=12, decimal_places=4)
    row_weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_before_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_before_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    ext_order_item_id = models.CharField(max_length=255, blank=True, null=True)
    locked_do_invoice = models.SmallIntegerField(blank=True, null=True)
    locked_do_ship = models.SmallIntegerField(blank=True, null=True)
    price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    is_nominal = models.IntegerField()
    tax_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)
    gift_message_available = models.IntegerField(blank=True, null=True)
    base_weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_applied_row_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_row_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied = models.TextField(blank=True, null=True)
    weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_order_item'


class SalesFlatOrderPayment(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey(SalesFlatOrder, models.DO_NOTHING)
    base_shipping_captured = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_captured = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_authorized = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_paid_online = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_refunded_online = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount_authorized = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_ordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount_ordered = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_amount_canceled = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    quote_payment_id = models.IntegerField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    cc_exp_month = models.CharField(max_length=255, blank=True, null=True)
    cc_ss_start_year = models.CharField(max_length=255, blank=True, null=True)
    echeck_bank_name = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    cc_debug_request_body = models.CharField(max_length=255, blank=True, null=True)
    cc_secure_verify = models.CharField(max_length=255, blank=True, null=True)
    protection_eligibility = models.CharField(max_length=255, blank=True, null=True)
    cc_approval = models.CharField(max_length=255, blank=True, null=True)
    cc_last4 = models.CharField(max_length=255, blank=True, null=True)
    cc_status_description = models.CharField(max_length=255, blank=True, null=True)
    echeck_type = models.CharField(max_length=255, blank=True, null=True)
    cc_debug_response_serialized = models.CharField(max_length=255, blank=True, null=True)
    cc_ss_start_month = models.CharField(max_length=255, blank=True, null=True)
    echeck_account_type = models.CharField(max_length=255, blank=True, null=True)
    last_trans_id = models.CharField(max_length=255, blank=True, null=True)
    cc_cid_status = models.CharField(max_length=255, blank=True, null=True)
    cc_owner = models.CharField(max_length=255, blank=True, null=True)
    cc_type = models.CharField(max_length=255, blank=True, null=True)
    po_number = models.CharField(max_length=255, blank=True, null=True)
    cc_exp_year = models.CharField(max_length=255, blank=True, null=True)
    cc_status = models.CharField(max_length=255, blank=True, null=True)
    echeck_routing_number = models.CharField(max_length=255, blank=True, null=True)
    account_status = models.CharField(max_length=255, blank=True, null=True)
    anet_trans_method = models.CharField(max_length=255, blank=True, null=True)
    cc_debug_response_body = models.CharField(max_length=255, blank=True, null=True)
    cc_ss_issue = models.CharField(max_length=255, blank=True, null=True)
    echeck_account_name = models.CharField(max_length=255, blank=True, null=True)
    cc_avs_status = models.CharField(max_length=255, blank=True, null=True)
    cc_number_enc = models.CharField(max_length=255, blank=True, null=True)
    cc_trans_id = models.CharField(max_length=255, blank=True, null=True)
    paybox_request_number = models.CharField(max_length=255, blank=True, null=True)
    address_status = models.CharField(max_length=255, blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_order_payment'


class SalesFlatOrderStatusHistory(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey(SalesFlatOrder, models.DO_NOTHING)
    is_customer_notified = models.IntegerField(blank=True, null=True)
    is_visible_on_front = models.SmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    entity_name = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_order_status_history'


class SalesFlatQuote(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    converted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.SmallIntegerField(blank=True, null=True)
    is_virtual = models.SmallIntegerField(blank=True, null=True)
    is_multi_shipping = models.SmallIntegerField(blank=True, null=True)
    items_count = models.IntegerField(blank=True, null=True)
    items_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    orig_order_id = models.IntegerField(blank=True, null=True)
    store_to_base_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    store_to_quote_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_currency_code = models.CharField(max_length=255, blank=True, null=True)
    store_currency_code = models.CharField(max_length=255, blank=True, null=True)
    quote_currency_code = models.CharField(max_length=255, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    checkout_method = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    customer_tax_class_id = models.IntegerField(blank=True, null=True)
    customer_group_id = models.IntegerField(blank=True, null=True)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    customer_prefix = models.CharField(max_length=40, blank=True, null=True)
    customer_firstname = models.CharField(max_length=255, blank=True, null=True)
    customer_middlename = models.CharField(max_length=40, blank=True, null=True)
    customer_lastname = models.CharField(max_length=255, blank=True, null=True)
    customer_suffix = models.CharField(max_length=40, blank=True, null=True)
    customer_dob = models.DateTimeField(blank=True, null=True)
    customer_note = models.CharField(max_length=255, blank=True, null=True)
    customer_note_notify = models.SmallIntegerField(blank=True, null=True)
    customer_is_guest = models.SmallIntegerField(blank=True, null=True)
    remote_ip = models.CharField(max_length=255, blank=True, null=True)
    applied_rule_ids = models.CharField(max_length=255, blank=True, null=True)
    reserved_order_id = models.CharField(max_length=64, blank=True, null=True)
    password_hash = models.CharField(max_length=255, blank=True, null=True)
    coupon_code = models.CharField(max_length=255, blank=True, null=True)
    global_currency_code = models.CharField(max_length=255, blank=True, null=True)
    base_to_global_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_to_quote_rate = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    customer_taxvat = models.CharField(max_length=255, blank=True, null=True)
    customer_gender = models.CharField(max_length=255, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_with_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_with_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    is_changed = models.IntegerField(blank=True, null=True)
    trigger_recollect = models.SmallIntegerField()
    ext_shipping_info = models.TextField(blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)
    is_persistent = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote'


class SalesFlatQuoteAddress(models.Model):
    address_id = models.IntegerField(primary_key=True)
    quote = models.ForeignKey(SalesFlatQuote, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    customer_id = models.IntegerField(blank=True, null=True)
    save_in_address_book = models.SmallIntegerField(blank=True, null=True)
    customer_address_id = models.IntegerField(blank=True, null=True)
    address_type = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    prefix = models.CharField(max_length=40, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    middlename = models.CharField(max_length=40, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    suffix = models.CharField(max_length=40, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    postcode = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    same_as_billing = models.SmallIntegerField()
    free_shipping = models.SmallIntegerField()
    collect_shipping_rates = models.SmallIntegerField()
    shipping_method = models.CharField(max_length=255, blank=True, null=True)
    shipping_description = models.CharField(max_length=255, blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4)
    subtotal = models.DecimalField(max_digits=12, decimal_places=4)
    base_subtotal = models.DecimalField(max_digits=12, decimal_places=4)
    subtotal_with_discount = models.DecimalField(max_digits=12, decimal_places=4)
    base_subtotal_with_discount = models.DecimalField(max_digits=12, decimal_places=4)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4)
    base_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4)
    shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    grand_total = models.DecimalField(max_digits=12, decimal_places=4)
    base_grand_total = models.DecimalField(max_digits=12, decimal_places=4)
    customer_notes = models.TextField(blank=True, null=True)
    applied_taxes = models.TextField(blank=True, null=True)
    discount_description = models.CharField(max_length=255, blank=True, null=True)
    shipping_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    subtotal_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_subtotal_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_hidden_tax_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_shipping_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    vat_id = models.TextField(blank=True, null=True)
    vat_is_valid = models.SmallIntegerField(blank=True, null=True)
    vat_request_id = models.TextField(blank=True, null=True)
    vat_request_date = models.TextField(blank=True, null=True)
    vat_request_success = models.SmallIntegerField(blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote_address'


class SalesFlatQuoteAddressItem(models.Model):
    address_item_id = models.IntegerField(primary_key=True)
    parent_item = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    quote_address = models.ForeignKey(SalesFlatQuoteAddress, models.DO_NOTHING)
    quote_item = models.ForeignKey('SalesFlatQuoteItem', models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    applied_rule_ids = models.TextField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total = models.DecimalField(max_digits=12, decimal_places=4)
    base_row_total = models.DecimalField(max_digits=12, decimal_places=4)
    row_total_with_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    super_product_id = models.IntegerField(blank=True, null=True)
    parent_product_id = models.IntegerField(blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    free_shipping = models.IntegerField(blank=True, null=True)
    is_qty_decimal = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    no_discount = models.IntegerField(blank=True, null=True)
    tax_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote_address_item'


class SalesFlatQuoteItem(models.Model):
    item_id = models.IntegerField(primary_key=True)
    quote = models.ForeignKey(SalesFlatQuote, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING, blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    parent_item = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    is_virtual = models.SmallIntegerField(blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    applied_rule_ids = models.TextField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    free_shipping = models.SmallIntegerField()
    is_qty_decimal = models.SmallIntegerField(blank=True, null=True)
    no_discount = models.SmallIntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    base_price = models.DecimalField(max_digits=12, decimal_places=4)
    custom_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_discount_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total = models.DecimalField(max_digits=12, decimal_places=4)
    base_row_total = models.DecimalField(max_digits=12, decimal_places=4)
    row_total_with_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    product_type = models.CharField(max_length=255, blank=True, null=True)
    base_tax_before_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_before_discount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    original_custom_price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    redirect_url = models.CharField(max_length=255, blank=True, null=True)
    base_cost = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_price_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_row_total_incl_tax = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_hidden_tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    gift_message_id = models.IntegerField(blank=True, null=True)
    weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_row_disposition = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied = models.TextField(blank=True, null=True)
    weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weee_tax_applied_row_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_applied_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    base_weee_tax_applied_row_amnt = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote_item'


class SalesFlatQuoteItemOption(models.Model):
    option_id = models.IntegerField(primary_key=True)
    item = models.ForeignKey(SalesFlatQuoteItem, models.DO_NOTHING)
    product_id = models.IntegerField()
    code = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote_item_option'


class SalesFlatQuotePayment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    quote = models.ForeignKey(SalesFlatQuote, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    method = models.CharField(max_length=255, blank=True, null=True)
    cc_type = models.CharField(max_length=255, blank=True, null=True)
    cc_number_enc = models.CharField(max_length=255, blank=True, null=True)
    cc_last4 = models.CharField(max_length=255, blank=True, null=True)
    cc_cid_enc = models.CharField(max_length=255, blank=True, null=True)
    cc_owner = models.CharField(max_length=255, blank=True, null=True)
    cc_exp_month = models.SmallIntegerField(blank=True, null=True)
    cc_exp_year = models.SmallIntegerField(blank=True, null=True)
    cc_ss_owner = models.CharField(max_length=255, blank=True, null=True)
    cc_ss_start_month = models.SmallIntegerField(blank=True, null=True)
    cc_ss_start_year = models.SmallIntegerField(blank=True, null=True)
    po_number = models.CharField(max_length=255, blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    cc_ss_issue = models.CharField(max_length=255, blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)
    paypal_payer_id = models.CharField(max_length=255, blank=True, null=True)
    paypal_payer_status = models.CharField(max_length=255, blank=True, null=True)
    paypal_correlation_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote_payment'


class SalesFlatQuoteShippingRate(models.Model):
    rate_id = models.IntegerField(primary_key=True)
    address = models.ForeignKey(SalesFlatQuoteAddress, models.DO_NOTHING)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    carrier = models.CharField(max_length=255, blank=True, null=True)
    carrier_title = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    method_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    error_message = models.TextField(blank=True, null=True)
    method_title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_quote_shipping_rate'


class SalesFlatShipment(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    total_weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    email_sent = models.SmallIntegerField(blank=True, null=True)
    order = models.ForeignKey(SalesFlatOrder, models.DO_NOTHING)
    customer_id = models.IntegerField(blank=True, null=True)
    shipping_address_id = models.IntegerField(blank=True, null=True)
    billing_address_id = models.IntegerField(blank=True, null=True)
    shipment_status = models.IntegerField(blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    packages = models.TextField(blank=True, null=True)
    shipping_label = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_shipment'


class SalesFlatShipmentComment(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey(SalesFlatShipment, models.DO_NOTHING)
    is_customer_notified = models.IntegerField(blank=True, null=True)
    is_visible_on_front = models.SmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_shipment_comment'


class SalesFlatShipmentGrid(models.Model):
    entity = models.ForeignKey(SalesFlatShipment, models.DO_NOTHING, primary_key=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    total_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    order_id = models.IntegerField()
    shipment_status = models.IntegerField(blank=True, null=True)
    increment_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    order_increment_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    order_created_at = models.DateTimeField(blank=True, null=True)
    shipping_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_shipment_grid'


class SalesFlatShipmentItem(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey(SalesFlatShipment, models.DO_NOTHING)
    row_total = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    order_item_id = models.IntegerField(blank=True, null=True)
    additional_data = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_shipment_item'


class SalesFlatShipmentTrack(models.Model):
    entity_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey(SalesFlatShipment, models.DO_NOTHING)
    weight = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    order_id = models.IntegerField()
    track_number = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    carrier_code = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_flat_shipment_track'


class SalesInvoicedAggregated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    orders_count = models.IntegerField()
    orders_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    invoiced_captured = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    invoiced_not_captured = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_invoiced_aggregated'
        unique_together = (('period', 'store', 'order_status'),)


class SalesInvoicedAggregatedOrder(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    order_status = models.CharField(max_length=50)
    orders_count = models.IntegerField()
    orders_invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    invoiced = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    invoiced_captured = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    invoiced_not_captured = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_invoiced_aggregated_order'
        unique_together = (('period', 'store', 'order_status'),)


class SalesOrderAggregatedCreated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    order_status = models.CharField(max_length=50)
    orders_count = models.IntegerField()
    total_qty_ordered = models.DecimalField(max_digits=12, decimal_places=4)
    total_qty_invoiced = models.DecimalField(max_digits=12, decimal_places=4)
    total_income_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_revenue_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_profit_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_invoiced_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_canceled_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_paid_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_refunded_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_tax_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_tax_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    total_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_shipping_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    total_discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_discount_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'sales_order_aggregated_created'
        unique_together = (('period', 'store', 'order_status'),)


class SalesOrderAggregatedUpdated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    order_status = models.CharField(max_length=50)
    orders_count = models.IntegerField()
    total_qty_ordered = models.DecimalField(max_digits=12, decimal_places=4)
    total_qty_invoiced = models.DecimalField(max_digits=12, decimal_places=4)
    total_income_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_revenue_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_profit_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_invoiced_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_canceled_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_paid_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_refunded_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_tax_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_tax_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    total_shipping_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_shipping_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)
    total_discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    total_discount_amount_actual = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'sales_order_aggregated_updated'
        unique_together = (('period', 'store', 'order_status'),)


class SalesOrderStatus(models.Model):
    status = models.CharField(primary_key=True, max_length=32)
    label = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'sales_order_status'


class SalesOrderStatusLabel(models.Model):
    status = models.ForeignKey(SalesOrderStatus, models.DO_NOTHING, db_column='status')
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    label = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'sales_order_status_label'
        unique_together = (('status', 'store'),)


class SalesOrderStatusState(models.Model):
    status = models.ForeignKey(SalesOrderStatus, models.DO_NOTHING, db_column='status')
    state = models.CharField(max_length=32)
    is_default = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sales_order_status_state'
        unique_together = (('status', 'state'),)


class SalesOrderTax(models.Model):
    tax_id = models.IntegerField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    percent = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    priority = models.IntegerField()
    position = models.IntegerField()
    base_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    process = models.SmallIntegerField()
    base_real_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hidden = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sales_order_tax'


class SalesOrderTaxItem(models.Model):
    tax_item_id = models.IntegerField(primary_key=True)
    tax = models.ForeignKey(SalesOrderTax, models.DO_NOTHING)
    item = models.ForeignKey(SalesFlatOrderItem, models.DO_NOTHING)
    tax_percent = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'sales_order_tax_item'
        unique_together = (('tax', 'item'),)


class SalesPaymentTransaction(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(SalesFlatOrder, models.DO_NOTHING)
    payment = models.ForeignKey(SalesFlatOrderPayment, models.DO_NOTHING)
    txn_id = models.CharField(max_length=100, blank=True, null=True)
    parent_txn_id = models.CharField(max_length=100, blank=True, null=True)
    txn_type = models.CharField(max_length=15, blank=True, null=True)
    is_closed = models.SmallIntegerField()
    additional_information = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_payment_transaction'
        unique_together = (('order', 'payment', 'txn_id'),)


class SalesRecurringProfile(models.Model):
    profile_id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=20)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    method_code = models.CharField(max_length=32)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    reference_id = models.CharField(max_length=32, blank=True, null=True)
    subscriber_name = models.CharField(max_length=150, blank=True, null=True)
    start_datetime = models.DateTimeField()
    internal_reference_id = models.CharField(unique=True, max_length=42)
    schedule_description = models.CharField(max_length=255)
    suspension_threshold = models.SmallIntegerField(blank=True, null=True)
    bill_failed_later = models.SmallIntegerField()
    period_unit = models.CharField(max_length=20)
    period_frequency = models.SmallIntegerField(blank=True, null=True)
    period_max_cycles = models.SmallIntegerField(blank=True, null=True)
    billing_amount = models.DecimalField(max_digits=12, decimal_places=4)
    trial_period_unit = models.CharField(max_length=20, blank=True, null=True)
    trial_period_frequency = models.SmallIntegerField(blank=True, null=True)
    trial_period_max_cycles = models.SmallIntegerField(blank=True, null=True)
    trial_billing_amount = models.TextField(blank=True, null=True)
    currency_code = models.CharField(max_length=3)
    shipping_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    init_amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    init_may_fail = models.SmallIntegerField()
    order_info = models.TextField()
    order_item_info = models.TextField()
    billing_address_info = models.TextField()
    shipping_address_info = models.TextField(blank=True, null=True)
    profile_vendor_info = models.TextField(blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_recurring_profile'


class SalesRecurringProfileOrder(models.Model):
    link_id = models.IntegerField(primary_key=True)
    profile = models.ForeignKey(SalesRecurringProfile, models.DO_NOTHING)
    order = models.ForeignKey(SalesFlatOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sales_recurring_profile_order'
        unique_together = (('profile', 'order'),)


class SalesRefundedAggregated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    order_status = models.CharField(max_length=50)
    orders_count = models.IntegerField()
    refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    online_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    offline_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_refunded_aggregated'
        unique_together = (('period', 'store', 'order_status'),)


class SalesRefundedAggregatedOrder(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    orders_count = models.IntegerField()
    refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    online_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    offline_refunded = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_refunded_aggregated_order'
        unique_together = (('period', 'store', 'order_status'),)


class SalesShippingAggregated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    shipping_description = models.CharField(max_length=255, blank=True, null=True)
    orders_count = models.IntegerField()
    total_shipping = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_shipping_actual = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_shipping_aggregated'
        unique_together = (('period', 'store', 'order_status', 'shipping_description'),)


class SalesShippingAggregatedOrder(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    shipping_description = models.CharField(max_length=255, blank=True, null=True)
    orders_count = models.IntegerField()
    total_shipping = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    total_shipping_actual = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales_shipping_aggregated_order'
        unique_together = (('period', 'store', 'order_status', 'shipping_description'),)


class Salesrule(models.Model):
    rule_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    uses_per_customer = models.IntegerField()
    is_active = models.SmallIntegerField()
    conditions_serialized = models.TextField(blank=True, null=True)
    actions_serialized = models.TextField(blank=True, null=True)
    stop_rules_processing = models.SmallIntegerField()
    is_advanced = models.SmallIntegerField()
    product_ids = models.TextField(blank=True, null=True)
    sort_order = models.IntegerField()
    simple_action = models.CharField(max_length=32, blank=True, null=True)
    discount_amount = models.DecimalField(max_digits=12, decimal_places=4)
    discount_qty = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    discount_step = models.IntegerField()
    simple_free_shipping = models.SmallIntegerField()
    apply_to_shipping = models.SmallIntegerField()
    times_used = models.IntegerField()
    is_rss = models.SmallIntegerField()
    coupon_type = models.SmallIntegerField()
    use_auto_generation = models.SmallIntegerField()
    uses_per_coupon = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salesrule'


class SalesruleCoupon(models.Model):
    coupon_id = models.IntegerField(primary_key=True)
    rule = models.ForeignKey(Salesrule, models.DO_NOTHING)
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)
    usage_limit = models.IntegerField(blank=True, null=True)
    usage_per_customer = models.IntegerField(blank=True, null=True)
    times_used = models.IntegerField()
    expiration_date = models.DateTimeField(blank=True, null=True)
    is_primary = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesrule_coupon'
        unique_together = (('rule', 'is_primary'),)


class SalesruleCouponUsage(models.Model):
    coupon = models.ForeignKey(SalesruleCoupon, models.DO_NOTHING)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING)
    times_used = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salesrule_coupon_usage'
        unique_together = (('coupon', 'customer'),)


class SalesruleCustomer(models.Model):
    rule_customer_id = models.IntegerField(primary_key=True)
    rule = models.ForeignKey(Salesrule, models.DO_NOTHING)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING)
    times_used = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'salesrule_customer'


class SalesruleCustomerGroup(models.Model):
    rule = models.ForeignKey(Salesrule, models.DO_NOTHING)
    customer_group = models.ForeignKey(CustomerGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'salesrule_customer_group'
        unique_together = (('rule', 'customer_group'),)


class SalesruleLabel(models.Model):
    label_id = models.IntegerField(primary_key=True)
    rule = models.ForeignKey(Salesrule, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    label = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salesrule_label'
        unique_together = (('rule', 'store'),)


class SalesruleProductAttribute(models.Model):
    rule = models.ForeignKey(Salesrule, models.DO_NOTHING)
    website = models.ForeignKey(CoreWebsite, models.DO_NOTHING)
    customer_group = models.ForeignKey(CustomerGroup, models.DO_NOTHING)
    attribute = models.ForeignKey(EavAttribute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'salesrule_product_attribute'
        unique_together = (('rule', 'website', 'customer_group', 'attribute'),)


class SalesruleWebsite(models.Model):
    rule = models.ForeignKey(Salesrule, models.DO_NOTHING)
    website = models.ForeignKey(CoreWebsite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'salesrule_website'
        unique_together = (('rule', 'website'),)


class SendfriendLog(models.Model):
    log_id = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=16, blank=True, null=True)
    time = models.IntegerField()
    website_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'sendfriend_log'


class ShippingTablerate(models.Model):
    pk = models.IntegerField(primary_key=True)
    website_id = models.IntegerField()
    dest_country_id = models.CharField(max_length=4)
    dest_region_id = models.IntegerField()
    dest_zip = models.CharField(max_length=10)
    condition_name = models.CharField(max_length=20)
    condition_value = models.DecimalField(max_digits=12, decimal_places=4)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    cost = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'shipping_tablerate'
        unique_together = (('website_id', 'dest_country_id', 'dest_region_id', 'dest_zip', 'condition_name', 'condition_value'),)


class Sitemap(models.Model):
    sitemap_id = models.IntegerField(primary_key=True)
    sitemap_type = models.CharField(max_length=32, blank=True, null=True)
    sitemap_filename = models.CharField(max_length=32, blank=True, null=True)
    sitemap_path = models.CharField(max_length=255, blank=True, null=True)
    sitemap_time = models.DateTimeField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sitemap'


class Tag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField()
    first_customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, blank=True, null=True)
    first_store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag'


class TagProperties(models.Model):
    tag = models.ForeignKey(Tag, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    base_popularity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tag_properties'
        unique_together = (('tag', 'store'),)


class TagRelation(models.Model):
    tag_relation_id = models.IntegerField(primary_key=True)
    tag = models.ForeignKey(Tag, models.DO_NOTHING)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    active = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag_relation'
        unique_together = (('tag', 'customer', 'product', 'store'),)


class TagSummary(models.Model):
    tag = models.ForeignKey(Tag, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    customers = models.IntegerField()
    products = models.IntegerField()
    uses = models.IntegerField()
    historical_uses = models.IntegerField()
    popularity = models.IntegerField()
    base_popularity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tag_summary'
        unique_together = (('tag', 'store'),)


class TaxCalculation(models.Model):
    tax_calculation_id = models.IntegerField(primary_key=True)
    tax_calculation_rate = models.ForeignKey('TaxCalculationRate', models.DO_NOTHING)
    tax_calculation_rule = models.ForeignKey('TaxCalculationRule', models.DO_NOTHING)
    customer_tax_class = models.ForeignKey('TaxClass', models.DO_NOTHING)
    product_tax_class = models.ForeignKey('TaxClass', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tax_calculation'


class TaxCalculationRate(models.Model):
    tax_calculation_rate_id = models.IntegerField(primary_key=True)
    tax_country_id = models.CharField(max_length=2)
    tax_region_id = models.IntegerField()
    tax_postcode = models.CharField(max_length=21, blank=True, null=True)
    code = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=12, decimal_places=4)
    zip_is_range = models.SmallIntegerField(blank=True, null=True)
    zip_from = models.IntegerField(blank=True, null=True)
    zip_to = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_calculation_rate'


class TaxCalculationRateTitle(models.Model):
    tax_calculation_rate_title_id = models.IntegerField(primary_key=True)
    tax_calculation_rate = models.ForeignKey(TaxCalculationRate, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tax_calculation_rate_title'


class TaxCalculationRule(models.Model):
    tax_calculation_rule_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255)
    priority = models.IntegerField()
    position = models.IntegerField()
    calculate_subtotal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tax_calculation_rule'


class TaxClass(models.Model):
    class_id = models.SmallIntegerField(primary_key=True)
    class_name = models.CharField(max_length=255)
    class_type = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'tax_class'


class TaxOrderAggregatedCreated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=255)
    order_status = models.CharField(max_length=50)
    percent = models.FloatField(blank=True, null=True)
    orders_count = models.IntegerField()
    tax_base_amount_sum = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_order_aggregated_created'
        unique_together = (('period', 'store', 'code', 'percent', 'order_status'),)


class TaxOrderAggregatedUpdated(models.Model):
    period = models.DateField(blank=True, null=True)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=255)
    order_status = models.CharField(max_length=50)
    percent = models.FloatField(blank=True, null=True)
    orders_count = models.IntegerField()
    tax_base_amount_sum = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax_order_aggregated_updated'
        unique_together = (('period', 'store', 'code', 'percent', 'order_status'),)


class WeeeDiscount(models.Model):
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    website = models.ForeignKey(CoreWebsite, models.DO_NOTHING)
    customer_group = models.ForeignKey(CustomerGroup, models.DO_NOTHING)
    value = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'weee_discount'


class WeeeTax(models.Model):
    value_id = models.IntegerField(primary_key=True)
    website = models.ForeignKey(CoreWebsite, models.DO_NOTHING)
    entity = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    country = models.ForeignKey(DirectoryCountry, models.DO_NOTHING, db_column='country', blank=True, null=True)
    value = models.DecimalField(max_digits=12, decimal_places=4)
    state = models.CharField(max_length=255)
    attribute = models.ForeignKey(EavAttribute, models.DO_NOTHING)
    entity_type_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'weee_tax'


class Widget(models.Model):
    widget_id = models.IntegerField(primary_key=True)
    widget_code = models.CharField(max_length=255, blank=True, null=True)
    widget_type = models.CharField(max_length=255, blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'widget'


class WidgetInstance(models.Model):
    instance_id = models.IntegerField(primary_key=True)
    instance_type = models.CharField(max_length=255, blank=True, null=True)
    package_theme = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    store_ids = models.CharField(max_length=255)
    widget_parameters = models.TextField(blank=True, null=True)
    sort_order = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'widget_instance'


class WidgetInstancePage(models.Model):
    page_id = models.IntegerField(primary_key=True)
    instance = models.ForeignKey(WidgetInstance, models.DO_NOTHING)
    page_group = models.CharField(max_length=25, blank=True, null=True)
    layout_handle = models.CharField(max_length=255, blank=True, null=True)
    block_reference = models.CharField(max_length=255, blank=True, null=True)
    page_for = models.CharField(max_length=25, blank=True, null=True)
    entities = models.TextField(blank=True, null=True)
    page_template = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'widget_instance_page'


class WidgetInstancePageLayout(models.Model):
    page = models.ForeignKey(WidgetInstancePage, models.DO_NOTHING)
    layout_update = models.ForeignKey(CoreLayoutUpdate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'widget_instance_page_layout'
        unique_together = (('layout_update', 'page'),)


class Wishlist(models.Model):
    wishlist_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(CustomerEntity, models.DO_NOTHING, unique=True)
    shared = models.SmallIntegerField()
    sharing_code = models.CharField(max_length=32, blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wishlist'


class WishlistItem(models.Model):
    wishlist_item_id = models.IntegerField(primary_key=True)
    wishlist = models.ForeignKey(Wishlist, models.DO_NOTHING)
    product = models.ForeignKey(CatalogProductEntity, models.DO_NOTHING)
    store = models.ForeignKey(CoreStore, models.DO_NOTHING, blank=True, null=True)
    added_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    qty = models.DecimalField(max_digits=12, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'wishlist_item'


class WishlistItemOption(models.Model):
    option_id = models.IntegerField(primary_key=True)
    wishlist_item = models.ForeignKey(WishlistItem, models.DO_NOTHING)
    product_id = models.IntegerField()
    code = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wishlist_item_option'
