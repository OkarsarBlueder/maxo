import os


def import_orders():
    """
    import ACME and MAXO orders  to database
    :return: None
    """
    import datetime
    from itertools import islice
    from orders.models import AOrders, MOrders

    orders = open("ACME_FILTER_ORDERS_2017.txt")
    for order in islice(orders, 1, None):
        if len(order) < 20:
            continue
        order = order.strip().split("|")
        AOrders.objects.create(
            order_id=order[0], customer_id=order[1], order_date=datetime.datetime.strptime(order[2], '%m/%d/%Y'),
            shipping_date=datetime.datetime.strptime(order[3], '%m/%d/%Y'), product_id=order[4],
            product_category=order[5],
            name=order[6], gender=order[7], street_address=order[8], city=order[9], state=order[10],
            postal_code=order[11], country=order[12]
        )

    orders = open("MAXO_FILTER_ORDERS_2017.csv")
    for order in islice(orders, 1, None):
        if len(order) < 20:
            continue
        order = order.strip().split("|")

        MOrders.objects.create(
            order_id=order[0], customer_id=order[1], order_date=datetime.datetime.strptime(order[2], '%m/%d/%Y'),
            ship_date=datetime.datetime.strptime(order[3], '%m/%d/%Y'), product_id=order[4],
            product_name=order[5], category=order[6], description=order[7], name=order[8], year_of_birth=order[9],
            gender=order[10], address_line_1=order[11].replace("\"", ""), city=order[12],
            postal_code=order[13], country=order[14]
        )


if __name__ == '__main__':
    import django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maxo.settings')
    django.setup()
    import_orders()
