# -*- coding: utf-8 -*-
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    coded by: Gabriela Quilarque <gabrielaquilarque97@gmail.com>
############################################################################

import odoo.addons.decimal_precision as dp
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_available = fields.Float(
        digits=dp.get_precision('Account'),
        compute="_compute_get_credit_available")

    @api.multi
    def _compute_get_credit_available(self):
        for partner in self:
            partner_credit = partner.sudo().credit_limit
            credit = partner_credit if partner_credit > 0 else 0
            partner.credit_available = partner.credit_limit - credit
