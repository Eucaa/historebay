from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.


"""
To create tables in the database.
"""


# To render the Order-class in the admin-interface (checkout-folder, models.py-file).
class OrderLineAdminInline(admin.TabularInline):  # Within the subclass, the TabularInline subclass defines the template of the class Order. StackedInline can also be used, depending on the template redering.
    model = OrderLineItem  # Uses the OrderLineItem as a model for that.


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )  # The admin interface has the ability to edit more than one model on a single page. This is called inlines.


admin.site.register(Order, OrderAdmin)
