from odoo import models, fields, api


class MyProductSaleManagement(models.Model):
    _name = "my.product.sale.management"
    _inherit = ["mail.thread", "mail.activity.mixin", "image.mixin"]
    _description = "Product Details"
    _rec_name = "customer_id"

    customer_id = fields.Many2one(
        "customer.details",
        string="Customer",
    )
    mobile_no_id = fields.Char(
        string="Mobile Number",
        related="customer_id.mobile_no",
        store=True,
        readonly=True,
    )
    email_id = fields.Char(
        string="Email Id",
        related="customer_id.email",
        store=True,
    )
    product_sale_line_ids = fields.One2many(
        "product.sale.order.line",
        "product_sale_management_id",
        string="Sale Order Line Id",
    )
    new_address_id = fields.Char(
        string="Address",
        related="customer_id.new_address",
        store=True,
    )
    order_date = fields.Date(string="Order Date", default=fields.Date.today())
    final_total = fields.Float(
        string="Total", compute="_compute_final_total", store=True
    )
    status = fields.Selection(
        [("draft", "Draft"), ("confirm", "Confirm"), ("paid", "Paid")],
        string="Confirm",
        default="draft",
    )
    company_partnerr_id = fields.Many2one("res.partner", string="Contact2", store=True)

    @api.depends("product_sale_line_ids.total_amount")
    def _compute_final_total(self):
        """note:"""
        for order in self:
            order.final_total = sum(order.product_sale_line_ids.mapped("total_amount"))

    def confirm_button(self):
        self.status = "confirm"

    def paid_button(self):
        self.status = "paid"

    def reset_draft(self):
        self.write({'status' : 'draft'})

    # @api.model
    # def get_view(self, view_id=None, view_type='form', **options):
    #     print("::::::::::ddddddddddddddddddself",self._context)
    #     res = super().get_view(view_id, view_type, **options)
    #     return res


class ProductSaleOrderLine(models.Model):
    _name = "product.sale.order.line"
    _description = "Order Details"

    product_name_id = fields.Many2one(
        string="Product Name", comodel_name="my.inventory.management", store=True
    )
    product_brand_name = fields.Char(
        string="Product Brand Name",
        related="product_name_id.product_brand_name",
        store=True,
    )
    consumer_quantity = fields.Integer(string="Quantity", required=True)

    selling_price = fields.Float(
        string="Price", related="product_name_id.selling_price"
    )
    tax = fields.Float()
    total_amount = fields.Float(
        string="Total Amount", compute="_compute_total_amount", store=True
    )
    product_sale_management_id = fields.Many2one(
        "my.product.sale.management", "Sale Management Id"
    )
    last_selling_price = fields.Float(string="Last Selling Price")

    @api.depends("consumer_quantity", "selling_price")
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = record.consumer_quantity * record.selling_price

    @api.model
    def create(self, values):
        res = super(ProductSaleOrderLine, self).create(values)
        res.product_name_id.last_selling_price = res.last_selling_price
        # print("values---------->>>>",values)
        return res

    def write(self, values):
        result = super(ProductSaleOrderLine, self).write(values)
        print(":::::::::::::::", self.product_name_id.id)
        self.product_name_id.browse_button(self.product_name_id.id)
        if "last_selling_price" in values:
            for record in self:
                record.product_name_id.last_selling_price = values["last_selling_price"]
        return result



    