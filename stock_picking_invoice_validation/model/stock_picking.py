# coding: utf-8
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#    coded by: hugo@vauxoo.com
#    planned by: Nhomar Hernandez <nhomar@vauxoo.com>
############################################################################
from openerp import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    invoice_id = fields.Many2one(
        string='Invoice', comodel_name='account.invoice',
        ondelete='cascade')
    check_invoice = fields.Selection(
        [('check', 'Check'),
         ('no_check', 'No Check')], "Check invoice vs picking",
        readonly=True,)
