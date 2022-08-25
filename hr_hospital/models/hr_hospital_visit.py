import datetime
from odoo import fields, models, api


class Visit(models.Model):
    _name = 'hr_hospital.visit'
    _description = 'Visit'

    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor',
                                index=True, required=True)
    patient_id = fields.Many2one('hr_hospital.patient', string='Patient',
                                 index=True, required=True)
    date_of_visit = fields.Datetime(required=True)
    end_of_visit = fields.Datetime(compute='_compute_end_of_visit')
    time_reception = fields.Integer(required=True)
    study_ids = fields.Many2many('hr_hospital.patient.study', string='Studies')
    diagnosis_id = fields.Many2one('hr_hospital.diagnosis', string='Diagnosis')
    recommendation = fields.Text(required=True)

    @api.depends('date_of_visit', 'time_reception')
    def _compute_end_of_visit(self):
        for rec in self:
            rec.end_of_visit = rec.date_of_visit \
                + datetime.timedelta(minutes=rec.time_reception)

    def name_get(self):
        return [(rec.id, "Visit %s at %s" % (rec.id, rec.date_of_visit))
                for rec in self]
