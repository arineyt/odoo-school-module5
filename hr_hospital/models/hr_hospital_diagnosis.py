from odoo import models, fields


class HospitalDiagnosis(models.Model):
    """A class used to represent a Diagnosis"""
    _name = 'hr_hospital.diagnosis'
    _description = "Hospital diagnosis"

    name = fields.Char(index=True, required=True)
    active = fields.Boolean(default=True)
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor',
                                index=True, required=True)
    patient_id = fields.Many2one('hr_hospital.patient', string='Patient',
                                 index=True, required=True)
    disease_id = fields.Many2one('hr_hospital.disease', string='Disease',
                                 index=True, required=True)
    date_of_diagnosis = fields.Date()
    study_ids = fields.Many2many('hr_hospital.patient.study', string='Studies')
    treatment = fields.Text(required=True)
    comments_of_mentor = fields.Text(required=False)
    disease_type_id = fields.Many2one('hr_hospital.disease.type',
                                      related='disease_id.disease_type_id',
                                      store=True)
