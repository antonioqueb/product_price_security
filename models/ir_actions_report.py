# -*- coding: utf-8 -*-
import logging

from odoo import api, models

_logger = logging.getLogger(__name__)

HOLD_PRICE_REPORT_XMLIDS = (
    'stock_lot_dimensions.action_report_stock_lot_hold_order_detail',
    'stock_lot_dimensions.action_report_stock_lot_hold_order_summary',
)


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    @api.model
    def _pps_restrict_hold_price_reports(self):
        """Restringe los reportes de hold CON precios al grupo de precios.

        Se hace por código (no por <record> XML) porque el nombre del campo
        de grupos en ir.actions.report cambió en Odoo 19: escribir
        'groups_id' fijo tumbaba la carga del registro con
        "Invalid field 'groups_id'". Aquí se detecta el campo real y, si el
        modelo no expone ninguno, se omite sin romper nada (las variantes
        'sin precios' siguen disponibles para todos en cualquier caso).
        """
        group = self.env.ref(
            'product_price_security.group_product_price_viewer',
            raise_if_not_found=False,
        )
        if not group:
            return True

        field_name = next(
            (f for f in ('groups_id', 'group_ids') if f in self._fields),
            None,
        )
        if not field_name:
            _logger.warning(
                '[PRICE SECURITY] ir.actions.report no expone campo de grupos '
                'en esta versión; los reportes de hold con precios quedan sin '
                'restricción de grupo (las vistas ya ocultan los precios).'
            )
            return True

        for xmlid in HOLD_PRICE_REPORT_XMLIDS:
            action = self.env.ref(xmlid, raise_if_not_found=False)
            if action:
                action.write({field_name: [(4, group.id)]})

        return True
