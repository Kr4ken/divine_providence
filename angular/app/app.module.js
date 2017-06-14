"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var core_1 = require("@angular/core");
var platform_browser_1 = require("@angular/platform-browser");
var http_1 = require("@angular/http");
var router_1 = require("@angular/router");
var forms_1 = require("@angular/forms");
var app_component_1 = require("./app.component");
var complete_component_1 = require("./complete/complete.component");
var control_component_1 = require("./control/control.component");
var inputTask_component_1 = require("./inputTask/inputTask.component");
var interest_service_1 = require("./interestService/interest.service");
var Control_service_1 = require("./controlService/Control.service");
var task_service_1 = require("./taskService/task.service");
var appRoutes = [
    { path: 'interests', component: complete_component_1.CompleteComponent },
    { path: 'control', component: control_component_1.ControlComponent },
    { path: 'tasks', component: inputTask_component_1.InputTaskComponent },
    { path: '',
        redirectTo: '/interests',
        pathMatch: 'full'
    }
];
var AppModule = (function () {
    function AppModule() {
    }
    return AppModule;
}());
AppModule = __decorate([
    core_1.NgModule({
        imports: [
            platform_browser_1.BrowserModule,
            http_1.HttpModule,
            router_1.RouterModule.forRoot(appRoutes),
            forms_1.FormsModule
        ],
        declarations: [
            app_component_1.AppComponent,
            complete_component_1.CompleteComponent,
            control_component_1.ControlComponent,
            inputTask_component_1.InputTaskComponent
        ],
        providers: [
            interest_service_1.InterestService,
            Control_service_1.ControlService,
            task_service_1.TaskService
        ],
        bootstrap: [app_component_1.AppComponent]
    })
], AppModule);
exports.AppModule = AppModule;
//# sourceMappingURL=app.module.js.map