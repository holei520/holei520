# -*- coding: utf-8 -*-
{
    'name': '练习题',
    'version': '12.0.1.0',
    'summary': 'PS Cloud 培训',
    'author': "chenhl",
    'website': 'https://www.mypscloud.com/',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/student_regiester_views.xml',
        'views/kemu_views.xml',
    ],
    'demo': [
        'demo/pscloud_demo.xml',
    ],
    'qweb': [],
    'js': [],
    'css': [],
    'auto_install': False,
    'application': True,
}