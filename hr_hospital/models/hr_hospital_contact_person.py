from odoo import models, fields


class ContactPerson(models.Model):
    _name = 'hr_hospital.contact.person'
    _inherit = ['hr_hospital.person.mixin', ]
    _description = 'Contact person'

    description = fields.Text()
