from odoo import models, fields, api


class CustomerDetails(models.Model):
    _name = "customer.details"
    _description = "User Details"

    name = fields.Char(required=True)
    mobile_no = fields.Char(string="Mobile Number",required=True)
    email = fields.Char(string="Email Id")
    image = fields.Binary(string='Customer Image', attachment=True, help='Select an image file')
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    new_address = fields.Char(string='Full Address', compute='_compute_full_address', store=True)

    @api.depends('street', 'street2', 'zip', 'city', 'state_id', 'country_id')
    def _compute_full_address(self):
        for address in self:
            # print("r.street............", address.street)
            address.new_address = f'{address.street}, {address.street2}, {address.city}, {address.state_id.name}, {address.country_id.name}, {address.zip}'

    def name_get(self):
        print("::::::::::self",self._context, dict(self.env.context), type(self.env.context))
        return super().name_get()


       
