## ./__manifest__.py
{
    'name': 'Product Price Security',
    'version': '19.0.1.1.0',
    'category': 'Product',
    'author': 'Alphaqueb Consulting SAS',
    'website': 'https://www.alphaqueb.com',
    'license': 'AGPL-3',
    'summary': 'Control access to product sale prices based on user groups.',
    'description': """
        This module restricts the visibility and modification of product sale prices
        to users who belong to a specific group. Unauthorized users will see the
        sale price as zero.
    """,
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