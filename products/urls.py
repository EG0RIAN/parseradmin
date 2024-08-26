from django.urls import path
from .views import export_products_to_csv, export_products_by_parser

urlpatterns = [
    path('export/all_products/', export_products_to_csv, name='export_products_csv'),
    path('export/parser/<int:parser_id>/', export_products_by_parser, name='export_products_by_parser'),

]
