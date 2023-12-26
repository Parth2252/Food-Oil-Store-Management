from odoo import models, fields

class OwnerPurchaseOrder(models.Model):
    _name = 'owner_purchase_order'
    _description = 'Owner Purchase Order'

    product_name = fields.Char(string='Product Name', required=True)
    product_brand_name = fields.Char(string='Product Brand Name', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    total_cost = fields.Float(string='Total Cost', required=True)
    expected_delivery_date = fields.Date(string='Expected Delivery Date', required=True)
