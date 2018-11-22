# -*- coding: utf-8 -*-
# Copyright 2016, 2018 Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Openworx Backend Theme",
    "summary": "Openworx Backend Theme 	",
    "version": "12.0.0.1",
    "category": "Theme/Backend",
    "website": "http://www.openworx.nl",
	"description": """
		Backend theme for Odoo 12.0 community edition.
    """,
	'images':[
        'images/screen.png'
	],
    "author": "Openworx",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web',
    ],
    "data": [
        'views/assets.xml',
        'views/sidebar.xml',
    ],
    'live_test_url': 'https://youtu.be/qTSup3fqwlU'

}

