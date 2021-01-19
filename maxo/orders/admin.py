from django.contrib import admin
from django.db.models import Count
from django.db.models.functions import TruncMonth
from import_export.admin import ImportExportModelAdmin

from .models import AOrders, MOrders


class AOrdersAdmin(admin.ModelAdmin):
    """
    AOrders admin
    """
    date_hierarchy = "order_date"
    list_display = ["order_id", "customer_id", "order_date",
                    "shipping_date", "product_category", "name", "gender",
                    "street_address", "city",
                    "state", "postal_code", "country"]
    list_editable = []
    search_fields = ("name",)
    list_per_page = 15


class MOrderAdmin(admin.ModelAdmin):
    """
    MOrders admin
    """
    list_display = ["order_id", "customer_id", "order_date",
                    "ship_date", "product_id",
                    "product_name", "category", "description", "name", "year_of_birth",
                    "gender", "address_line_1", "city",
                    "postal_code", "country"]
    search_fields = ("product_name",)
    date_hierarchy = "order_date"
    list_per_page = 15


class ViewsMTop10(MOrders):
    class Meta:
        proxy = True
        verbose_name = "MAXO_top10"
        verbose_name_plural = verbose_name


class ViewsATop10(AOrders):
    class Meta:
        proxy = True
        verbose_name = "ACME_top10"
        verbose_name_plural = verbose_name


class ViewsMTop10Admin(ImportExportModelAdmin):
    change_list_template = 'admin/admin_test.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request, extra_context=extra_context
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response
        month_order_static = qs.annotate(month=TruncMonth('order_date')).values("month").order_by("month").annotate(
            nums=Count("month"))
        top10 = qs.values_list("customer_id").annotate(order_nums=Count('customer_id')).order_by("-order_nums")
        customer_ids = [customer[0] for customer in top10[:10]]
        top10_customers = [qs.filter(customer_id=customer_id)[1] for customer_id in customer_ids]
        response.context_data['month_order_static'] = month_order_static
        response.context_data['top10_customers'] = top10_customers
        response.context_data['orders_top10'] = list(
            top10[:10]
        )
        return response


def allow_anonymous_user():
    from django.contrib.auth.models import AnonymousUser
    AnonymousUser.id = 1
    AnonymousUser.pk = 1
    AnonymousUser.is_active = True
    AnonymousUser.is_staff = True
    AnonymousUser.is_superuser = True
    AnonymousUser.is_authenticated = True
    import types
    AnonymousUser.has_perm = types.MethodType(lambda self, perm, obj=None: True, AnonymousUser)
    AnonymousUser.has_perms = types.MethodType(lambda self, perm_list, obj=None: True, AnonymousUser)
    AnonymousUser.has_module_perms = types.MethodType(lambda self, module, obj=None: True, AnonymousUser)


allow_anonymous_user()

admin.site.site_header = 'Orders'
admin.site.site_title = 'Orders backends'
admin.site.index_title = 'Orders'
admin.site.register(ViewsATop10, ViewsMTop10Admin)
admin.site.register(ViewsMTop10, ViewsMTop10Admin)
admin.site.register(AOrders, AOrdersAdmin)
admin.site.register(MOrders, MOrderAdmin)
