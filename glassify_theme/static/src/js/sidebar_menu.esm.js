/** @odoo-module **/
/* Copyright 2024 Glassify Theme
 * License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl). */

import {Component, useState} from "@odoo/owl";
import {useBus, useService} from "@web/core/utils/hooks";
import {WebClient} from "@web/webclient/webclient";
import {getWebIconData} from "@web_responsive/components/apps_menu_tools.esm";

export class SidebarMenu extends Component {
    static template = "glassify_theme.SidebarMenu";
    static props = {};

    setup() {
        this.menuService = useService("menu");
        this.state = useState({
            collapsed: false,
        });
        useBus(this.env.bus, "MENUS:APP-CHANGED", () => {
            this.state.collapsed = false;
            this.render();
        });
    }

    get apps() {
        return this.menuService.getApps();
    }

    get currentApp() {
        return this.menuService.getCurrentApp();
    }

    get currentAppSections() {
        if (!this.currentApp) return [];
        const tree = this.menuService.getMenuAsTree(this.currentApp.id);
        return tree.childrenTree || [];
    }

    getAppIconSrc(app) {
        return getWebIconData(app);
    }

    getMenuItemHref(menu) {
        return `/odoo/${menu.actionPath || "action-" + menu.actionID}`;
    }

    onAppClick(app) {
        this.menuService.selectMenu(app);
    }

    onMenuClick(menu) {
        this.menuService.selectMenu(menu);
    }

    toggleCollapsed() {
        this.state.collapsed = !this.state.collapsed;
    }
}

// Register SidebarMenu as a sub-component of WebClient
Object.assign(WebClient.components, {SidebarMenu});
