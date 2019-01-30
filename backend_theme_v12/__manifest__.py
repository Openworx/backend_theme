# -*- coding: utf-8 -*-
# Copyright 2016, 2019 Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Openworx Material Backend Theme V12",
    "summary": "Openworx Material Backend Theme V12	",
    "version": "12.0.0.1",
    "category": "Theme/Backend",
    "website": "http://www.openworx.nl",
	"description": """
		Openworx Material Backend theme for Odoo 12.0 community edition.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "Openworx",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
        'web_responsive',

    ],
    "data": [
        'views/assets.xml',
		'views/res_company_view.xml',
		'views/users.xml',
        'views/sidebar.xml',
		#'views/web.xml',
    ],
    'live_test_url': 'https://youtu.be/JX-ntw2ORl8'

}

