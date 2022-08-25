from odoo import fields, models


class PersonalDoctorHistory(models.Model):
    _name = 'hr_hospital.personal.doctor.history'
    _description = 'History of personal doctors'

    doctor_id = fields.Many2one('hr_hospital.doctor', string='Personal doctor',
                                index=True, required=True)
    patient_id = fields.Many2one('hr_hospital.patient', string='Patient',
                                 index=True, required=True)
    appointment_date = fields.Date('appointment date',
                                   index=True, required=True)

    def name_get(self):
        return [(tag.id, "%s" % tag.appointment_date)
                for tag in self]
