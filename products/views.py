import csv
from django.http import HttpResponse
from .models import Product

def export_products_to_csv(request):
    # Создаем HttpResponse с правильным заголовком для CSV-файла
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    # Записываем заголовки столбцов
    writer.writerow([
        'ID', 'Name', 'URL', 'Brand', 'Categories', 'Discount', 'Discount Type', 
        'SKU', 'Size', 'In Stock', 'Color', 'Made In', 'Height', 
        'Width', 'Depth', 'Description', 'Details'
    ])

    # Получаем все объекты Product из базы данных
    products = Product.objects.all()

    for product in products:
        writer.writerow([
            product.id,
            product.name,
            product.url,
            product.brand,
            product.categories,
            product.discount,
            product.discount_type,
            product.sku,
            product.size,
            product.in_stock,
            product.color,
            product.made_in,
            product.height,
            product.width,
            product.depth,
            product.description,
            product.details
        ])

    return response


def export_products_by_parser(request, parser_id):
    # Создаем HttpResponse с правильным заголовком для CSV-файла
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="products_parser_{parser_id}.csv"'

    writer = csv.writer(response)
    # Записываем заголовки столбцов
    writer.writerow([
        'ID', 'Name', 'URL', 'Brand', 'Categories', 'Discount', 'Discount Type',
        'SKU', 'Size', 'In Stock', 'Color', 'Made In', 'Height',
        'Width', 'Depth', 'Description', 'Details'
    ])

    # Получаем объекты Product, фильтруя по parser_id
    products = Product.objects.filter(parser_id=parser_id)

    for product in products:
        writer.writerow([
            product.id,
            product.name,
            product.url,
            product.brand,
            product.categories,
            product.discount,
            product.discount_type,
            product.sku,
            product.size,
            product.in_stock,
            product.color,
            product.made_in,
            product.height,
            product.width,
            product.depth,
            product.description,
            product.details
        ])

    return response
