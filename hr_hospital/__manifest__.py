{
    'name': "Hospital",

    'summary': """
        Hospital System""",

    'author': "Dmytro Stopchak",
    'category': 'Uncategorized',
    'version': '15.0.1.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menus.xml',
        'views/hr_hospital_contact_person_views.xml',
        'views/hr_hospital_disease_type_views.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_patient_study_views.xml',
        'views/hr_hospital_personal_doctor_history_views.xml',
        'views/hr_hospital_study_type_views.xml',
        'views/hr_hospital_diagnosis_views.xml',
        'views/hr_hospital_disease_views.xml',
        'views/hr_hospital_menus.xml',
        'views/hr_hospital_sample_type_views.xml',
        'views/hr_hospital_visit_views.xml',
        'views/hr_hospital_patient_views.xml',
        'data/hr_hospital_data.xml',
        'wizard/hr_hospital_set_personal_doctor_view.xml',
        'report/hr_hospital_doctor_report.xml',
        'report/hr_hospital_doctor_templates.xml',
    ],

    # only loaded in demonstration mode
    'demo': [],
    'application': True,
    'license': 'LGPL-3',
}
