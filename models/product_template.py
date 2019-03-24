from odoo import fields, models

class ProductTemplate(models.Model):
	_inherit = 'product.template'
	school_category = fields.Selection([('m','Maternelle'), ('p','Primaire'),('c','College'),
					    ('l','Lycee'),('s','Superieur')],
                   			     'Ecole préférentielle', required=True)
