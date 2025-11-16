## ./models/product_template.py
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    list_price_display = fields.Float(
        string='Precio de Venta',
        compute='_compute_list_price_display',
        inverse='_inverse_list_price_display',
        digits='Product Price',
        help="Precio de venta del producto. Visible solo para usuarios autorizados."
    )
    
    @api.depends('list_price')
    def _compute_list_price_display(self):
        can_see_price = self.env.user.has_group('product_price_security.group_product_price_viewer')
        _logger.warning(f"=== COMPUTE PRICE DISPLAY ===")
        _logger.warning(f"Usuario: {self.env.user.name} (ID: {self.env.user.id})")
        _logger.warning(f"Tiene permiso: {can_see_price}")
        
        for record in self:
            if can_see_price:
                record.list_price_display = record.list_price
                _logger.warning(f"Producto {record.name}: Mostrando precio ${record.list_price}")
            else:
                record.list_price_display = 0.0
                _logger.warning(f"Producto {record.name}: Ocultando precio (${record.list_price} -> $0.0)")
    
    def _inverse_list_price_display(self):
        can_see_price = self.env.user.has_group('product_price_security.group_product_price_viewer')
        _logger.warning(f"=== INVERSE PRICE DISPLAY ===")
        _logger.warning(f"Usuario: {self.env.user.name}")
        _logger.warning(f"Tiene permiso: {can_see_price}")
        
        if can_see_price:
            for record in self:
                _logger.warning(f"Guardando precio: ${record.list_price_display}")
                record.list_price = record.list_price_display
        else:
            _logger.warning(f"Usuario sin permiso intentó modificar precio")