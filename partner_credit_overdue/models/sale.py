# -*- coding: utf-8 -*-
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    coded by: Gabriela Quilarque <gabrielaquilarque97@gmail.com>
############################################################################

import odoo.addons.decimal_precision as dp
from odoo import fields, models, api


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
    payment_overdue_ids = fields.One2many(
        comodel_name='account.move.line',
        inverse_name='move_id',
        string='Payments Overdue',
        compute="_compute_payment_overdue")
    payment_pending_ids = fields.One2many(
        comodel_name='account.move.line',
        inverse_name='move_id',
        string='Payments Pendings',
        compute="_compute_payment_overdue")

    @api.multi
    def _compute_payment_overdue(self):
        moveline_obj = self.env['account.move.line']
        for sale in self:
            movelines = moveline_obj.search(
                [('partner_id', '=', sale.partner_id.id),
                 ('account_id.user_type_id.type', '=', 'receivable'),
                 ('debit', '!=', 0),
                 ('move_id.state', '!=', 'draft'),
                 ('reconciled', '=', False)])
            movelines_overdue = []
            movelines_pending = []
            for move in movelines:
                if move.date_maturity <= fields.Date.today():
                    movelines_overdue.append(move.id)
                else:
                    movelines_pending.append(move.id)
            sale.payment_overdue_ids = movelines_overdue
            sale.payment_pending_ids = movelines_pending
