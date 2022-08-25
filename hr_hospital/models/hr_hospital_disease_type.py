from odoo import fields, models


class DiseaseType(models.Model):
    _name = 'hr_hospital.disease.type'
    _description = 'Type of disease'
    _parent_name = "parent_id"
    _parent_store = True

    name = fields.Char(index=True, required=True)
    active = fields.Boolean(default=True)
    parent_id = fields.Many2one('hr_hospital.disease.type',
                                'Parent Type', index=True,
                                ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('hr_hospital.disease.type',
                               'parent_id', 'Child Type')
