"use strict";
var router_1 = require('@angular/router');
var component1_component_1 = require("./component1.component");
var component2_component_1 = require("./component2.component");
var django_component_1 = require("./django.component");
var complete_component_1 = require("./complete/complete.component");
var routes = [
    { path: '', redirectTo: '/component1', pathMatch: 'full' },
    { path: 'component1', component: component1_component_1.Component1Component },
    { path: 'component2', component: component2_component_1.Component2Component },
    { path: 'completeComponent', component: complete_component_1.CompleteComponent },
    { path: 'djcomponent', component: django_component_1.DjangoComponent },
];
exports.appRouterProviders = [
    router_1.provideRouter(routes)
];
//# sourceMappingURL=app.route.js.map