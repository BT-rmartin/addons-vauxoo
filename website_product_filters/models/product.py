# coding: utf-8
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C)2010-  OpenERP SA (<http://openerp.com>). All Rights Reserved
#    App Author: Vauxoo
#
#    Developed by Oscar Alcala
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api
from datetime import datetime
import time


class WebsiteSeoMetadata(models.Model):
    _inherit = ["website.seo.metadata"]
    views = fields.Integer(
        'Views',
        help='This field shows the number of times a product has been'
             'viewed on the website in order to get popularity of it.')
    decimal_time = fields.Integer(
        'Decimal Time',
        help='This field shows the decimal time when a product is published'
        'on the website.')

    @api.multi
    def write(self, values):
        for record in self:
            if values.get('website_published', False):
                now = datetime.now()
                self.decimal_time = time.mktime(now.timetuple())
                values['decimal_time'] = self.decimal_time
        return super(WebsiteSeoMetadata, self).write(values)


class WebsiteProductMetadata(models.Model):
    _inherit = ["product.template", "website.seo.metadata"]
    _name = "product.template"


class ProductPriceRanges(models.Model):
    _name = "product.price.ranges"

    lower = fields.Float("Lower")
    upper = fields.Float("Upper")