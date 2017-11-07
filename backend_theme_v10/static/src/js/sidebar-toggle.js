/* Copyright 2017 Openworx.
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl). */

odoo.define('backend_theme_v10.sidebar-toggle', function (require) {
    "use strict";
    
    var session = require('web.session');
    var Model = require('web.DataModel');
    
    var id = session.uid;
    
    new Model('res.users').query(['sidebar_visible'])
        .filter([['id', '=', id]])
        .first()
        .then(function(res) {
            var toggle = res["sidebar_visible"];
            if (toggle === true) {
                $("#app-sidebar").removeClass("toggle-sidebar");
            } else {
                $("#app-sidebar").addClass("toggle-sidebar");
            };
    });   
});
