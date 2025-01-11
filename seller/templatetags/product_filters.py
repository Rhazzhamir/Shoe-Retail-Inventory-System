from django import template

register = template.Library()

@register.filter
def filter_stock(products, level):
    if level == "0":
        return [p for p in products if p.stock <= 0]
    elif level == "1":
        return [p for p in products if p.stock == 1]
    return products

@register.simple_tag
def get_stock_status(product):
    if product.stock <= 0:
        return 'out-of-stock'
    elif product.stock <= 1:
        return 'low-stock'
    return 'in-stock'