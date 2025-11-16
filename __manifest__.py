## ./__manifest__.py
{
    'name': 'Product Price Security',
    'version': '19.0.1.0.0',
    'category': 'Product',
    'depends': ['product', 'stock'],
    'data': [
        'security/product_security.xml',
        'views/product_template_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'product_price_security/static/src/scss/product_price.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}