from odoo import models, fields, api

class MyInventoryManagement(models.Model):
    _name = 'my.inventory.management'
    _description = 'Inventory Management'
    _rec_name = 'product_name'

    product_name = fields.Char(string='Product Name', required=True)
    product_brand_name = fields.Char(string='Product Brand Name')
    quantity_on_hand = fields.Float(string='Quantity On Hand')
    cost_price = fields.Float(string='Cost Price')
    selling_price = fields.Float(string='Selling Price')
    product_image = fields.Binary(string='Product Image', attachment=True, help='Select an image file')
    last_selling_price = fields.Float(string='Last Selling Price')


    def search_button(self):
        search_var = self.env["my.inventory.management"].search([('product_brand_name', '=', 'Gulab')])
        print(search_var)
        for record in search_var:
            print("product name..............", record.product_name, "product brand name--->>>", record.product_brand_name)


    def search_count_button(self):
        search_count_var = self.env["my.inventory.management"].search_count([('product_brand_name', '=', 'Gulab')])
        print("count number------------->>>>>>>", search_count_var)
        

    # def browse_button(self, values):
    #     browse_var = self.env["my.inventory.management"].browse([values])
    #     for record in browse_var:
    #         print("product name..............", record.product_name, "product brand name............", record.product_brand_name, "product cost price............", record.cost_price)
        

    def copy_button(self):
        browse_var = self.env["my.inventory.management"].browse(4)
        browse_var.copy()
        print(browse_var)
        

    def unlink_button(self):
        browse_var = self.env["my.inventory.management"].browse(4)
        browse_var.unlink()
        

    def name_get(self):
        print("::::::::::self",self._context, dict(self.env.context), type(self.env.context))
        result = []
        for product_name in self.sudo():
            name = '%s - %s' % (product_name.product_name, product_name.product_brand_name)
            result.append((product_name.id, name))
        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        res = super()._name_search(name, args, operator, limit, name_get_uid)
        print(":::::::::res", res)
        # args = args or []
        # equipment_ids = []
        # if name and operator not in expression.NEGATIVE_TERM_OPERATORS and operator != '=':
        #     equipment_ids = self._search([('name', '=', name)] + args, limit=limit, access_rights_uid=name_get_uid)
        return res
