from odoo import fields, models


class PatientStudy(models.Model):
    _name = 'hr_hospital.patient.study'
    _description = 'Studies of patients'

    name = fields.Char(index=True, required=True)
    patient_id = fields.Many2one('hr_hospital.patient', string='Patient',
                                 index=True, required=True)
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor',
                                index=True, required=True)
    study_id = fields.Many2one('hr_hospital.study.type', string='Study',
                               index=True, required=True)
    sample_id = fields.Many2one('hr_hospital.sample.type',
                                string='Sample type',
                                index=True, required=True)
    conclusion = fields.Text(required=True)
    telephone = fields.Char(related='patient_id.phone')
