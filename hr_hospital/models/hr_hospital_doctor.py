from odoo import models, fields


class HospitalDoctor(models.Model):
    """A class used to represent a Doctor"""
    _name = 'hr_hospital.doctor'
    _inherit = ['hr_hospital.person.mixin', ]
    _description = "Hospital doctor"

    specialty = fields.Char('specialty', required=True)
    is_intern = fields.Boolean()
    color = fields.Integer()
    intern_ids = fields.One2many(comodel_name='hr_hospital.doctor',
                                 inverse_name='mentor_id',
                                 string='Interns',
                                 domain=[('is_intern', '=', True)])
    patient_ids = fields.One2many(comodel_name='hr_hospital.patient',
                                  inverse_name='personal_doctor_id')
    mentor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                string='Mentor',
                                domain=[('is_intern', '=', False)])

    visit_ids = fields.One2many(comodel_name='hr_hospital.visit',
                                inverse_name='doctor_id',)

    description = fields.Text()

    def name_get(self):
        return [(rec.id,
                 "%s %s %s" % (rec.last_name, rec.middle_name, rec.first_name)
                 ) for rec in self]
