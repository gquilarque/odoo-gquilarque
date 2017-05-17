# -*- coding: utf-8 -*-
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    coded by: Gabriela Quilarque <gabrielaquilarque97@gmail.com>
############################################################################

import odoo.addons.decimal_precision as dp
from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_credit_limit = fields.Float(
        related='partner_id.credit_limit',
        digits=dp.get_precision('Account'),
        readonly=True)
    partner_credit_available = fields.Float(
        related='partner_id.credit_available',
        digits=dp.get_precision('Account'),
        readonly=True)
    credit_requested = fields.Monetary(
        related='amount_total',
        readonly=True)
