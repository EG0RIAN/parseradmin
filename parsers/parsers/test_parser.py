import random
from faker import Faker
from products.models import Product, ProductImage
from parsers.models import Parser


def run_test_parser():
    fake = Faker()
    parser = "1"
    product_name = fake.word().capitalize()
    product_url = fake.url()
    product_brand = fake.company()
    product_categories = ', '.join([fake.word() for _ in range(3)])
    product_discount = random.randint(5, 50)
    product_discount_type = random.choice(['fix', 'percentage'])
    product_sku = fake.unique.ean(length=8)
    product_size = random.choice(['Small', 'Medium', 'Large'])
    product_in_stock = random.randint(1, 100)
    product_color = fake.color_name()
    product_made_in = fake.country()
    product_height = random.randint(10, 200)
    product_width = random.randint(10, 200)
    product_depth = random.randint(10, 200)
    product_description = fake.text()
    product_details = fake.paragraph()

    # Генерация и сохранение тестового изображения продукта
    product_image = ProductImage.objects.create(
        image_url=fake.image_url()
    )

    # Сохранение данных в модель Product
    product = Product.objects.create(
        parser_id=parser,
        name=product_name,
        url=product_url,
        images=product_image,
        brand=product_brand,
        categories=product_categories,
        discount=product_discount,
        discount_type=product_discount_type,
        sku=product_sku,
        size=product_size,
        in_stock=product_in_stock,
        color=product_color,
        made_in=product_made_in,
        height=product_height,
        width=product_width,
        depth=product_depth,
        description=product_description,
        details=product_details
    )

    print(f"Product '{product.name}' has been created and saved to the database.")

for i in range(10):
    run_test_parser()