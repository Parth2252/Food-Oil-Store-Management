{
    "name": "Store Management",
    "license": "LGPL-3",
    "version": "16.0",
    "category": "for study  purpose",
    "summary": "Custom module for management of store",
    "description": """
        This is a custom module for management of store with a 'store' model.
    """,
    "author": "serpentcs",
    "website": "https://www.serpentcs.com/",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/my_customer_management.xml",
        "views/my_inventory_management.xml",
        "views/my_product_sale_management.xml",
        "views/store_contact_details.xml"
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
