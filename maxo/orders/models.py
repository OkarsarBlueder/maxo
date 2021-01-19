from django.db import models


class MOrders(models.Model):
    """
    Create t_maxo_orders tables
    """
    order_id = models.CharField("ORDER_ID", max_length=150)
    customer_id = models.CharField("ORDER_ID", max_length=150)
    order_date = models.DateField("ORDER_DATE")
    ship_date = models.DateField("SHIP_DATE")
    product_id = models.CharField("PRODUCT_ID", max_length=150)
    product_name = models.CharField("PRODUCT_NAME", max_length=150)
    category = models.CharField("CATEGORY", max_length=150)
    description = models.CharField("DESCRIPTION", max_length=150)
    name = models.CharField("CUSTOMER_NAME", max_length=150)
    year_of_birth = models.CharField("YEAR_OF_BIRTH", max_length=4)
    gender = models.CharField("GENDER", max_length=150)
    address_line_1 = models.CharField("ADDRESS_LINE_1", max_length=150)
    city = models.CharField("CITY", max_length=150)
    postal_code = models.CharField("POSTAL_CODE", max_length=150)
    country = models.CharField("COUNTRY", max_length=150)

    def __str__(self):
        return self.order_id

    class Meta:
        db_table = "t_maxo_orders"
        verbose_name = "maxo_orders"
        verbose_name_plural = verbose_name


class AOrders(models.Model):
    """
    Create table t_acme_orders
    """
    order_id = models.CharField("ORDER_ID", max_length=150)
    customer_id = models.CharField("CUSTOMER_ID", max_length=150)
    order_date = models.DateField("ORDER_DATE")
    shipping_date = models.DateField("SHIPPING_DATE")
    product_id = models.CharField("PRODUCT_ID", max_length=150)
    product_category = models.CharField("PRODUCT_CATEGORY", max_length=150)
    name = models.CharField("NAME", max_length=150)
    gender = models.CharField("GENDER", max_length=150)
    street_address = models.CharField("STREET_ADDRESS", max_length=150)
    city = models.CharField("CITY", max_length=150)
    state = models.CharField("STATE", max_length=150)
    postal_code = models.CharField("POSTAL_CODE", max_length=150)
    country = models.CharField("COUNTRY", max_length=150)

    def __str__(self):
        return self.product_id

    class Meta:
        db_table = "t_acme_orders"
        verbose_name = "acme_orders"
        verbose_name_plural = verbose_name
