from datetime import date

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api


class HospitalPatient(models.Model):
    """A class used to represent a Patient"""
    _name = 'hr_hospital.patient'
    _inherit = ['hr_hospital.person.mixin', ]
    _description = "Hospital patient"

    date_of_birth = fields.Date(required=True)
    age = fields.Integer(compute='_compute_age', compute_sudo=True, store=True)

    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], )
    degree_of_morbidity = fields.Selection([('1', 'Good'),
                                            ('2', 'Normal'),
                                            ('3', 'Bad')],
                                           default='1', required=True)

    passport_series = fields.Char(size=2, )
    passport_number = fields.Char(size=6, )
    passport_issued = fields.Date()
    passport_issued_by = fields.Char()

    contact_person_id = fields.Many2one('hr_hospital.contact.person',
                                        string='Contact person')
    personal_doctor_id = fields.Many2one('hr_hospital.doctor',
                                         string='Personal doctor',
                                         required=True)
    personal_doctor_history_ids = fields.One2many(
        comodel_name='hr_hospital.personal.doctor.history',
        inverse_name='patient_id',
        string='Doctor History')

    visit_ids = fields.One2many(
        comodel_name='hr_hospital.visit',
        inverse_name='patient_id',
        string='Visits History')

    diagnosis_ids = fields.One2many(
        comodel_name='hr_hospital.diagnosis',
        inverse_name='patient_id',
        string='Diagnosis')

    description = fields.Text()

    @api.depends('date_of_birth')
    def _compute_age(self):
        for man in self:
            man.age = \
                relativedelta(fields.Date.today(), man.date_of_birth).years \
                    if man.date_of_birth else 0

    @api.model
    def create(self, vals):
        new_record = super().create(vals)
        if 'personal_doctor_id' in vals:
            self.env['hr_hospital.personal.doctor.history'].create({
                'doctor_id': vals['personal_doctor_id'],
                'patient_id': new_record.id,
                'appointment_date': date.today(), })
        return new_record

    def write(self, vals):
        if 'personal_doctor_id' not in vals:
            return super().write(vals)
        for obj in self:
            if obj.personal_doctor_id.id != vals.get('personal_doctor_id'):
                self.env['hr_hospital.personal.doctor.history'].create({
                    'doctor_id': vals.get('personal_doctor_id'),
                    'patient_id': obj.id, 'appointment_date': date.today(), })
            val = vals.deepcopy()
            if obj.contact_person_id:
                val['passport_number'] = '1111 {}'.format(obj.passport_series)
            super('Patient', obj).write(val)
        return True
