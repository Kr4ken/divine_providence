"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require("@angular/core");
var Control_service_1 = require("../controlService/Control.service");
var ControlComponent = (function () {
    function ControlComponent(controlService) {
        this.controlService = controlService;
        this.syncIdsStatus = 'Не выполнялась';
        this.status = 0;
        this.syncing = false;
        this.syncInterestsIdsStatus = 'Не выполнялась';
        this.statusInterests = 0;
        this.syncingInterests = false;
        this.syncInputTasksStatus = 'Не выполнялась';
        this.statusInputTasks = 0;
        this.syncingInputTasks = false;
    }
    ControlComponent.prototype.SyncIds = function () {
        var _this = this;
        console.log('Start');
        this.syncing = true;
        this.controlService.syncAllIds()
            .then(function (status) {
            _this.syncing = false;
            _this.syncIdsStatus = status;
            _this.status = 1;
        })
            .catch(function (err) {
            _this.syncing = false;
            _this.syncIdsStatus = err;
            _this.status = 2;
        });
    };
    ControlComponent.prototype.SyncInterestsIds = function () {
        var _this = this;
        console.log('Start');
        this.syncingInterests = true;
        this.controlService.syncInterestsIds()
            .then(function (status) {
            _this.syncingInterests = false;
            _this.syncInterestsIdsStatus = status;
            _this.statusInterests = 1;
        })
            .catch(function (err) {
            _this.syncingInterests = false;
            _this.syncInterestsIdsStatus = err;
            _this.statusInterests = 2;
        });
    };
    ControlComponent.prototype.SyncInputTasks = function () {
        var _this = this;
        console.log('Start');
        this.syncingInputTasks = true;
        this.controlService.syncInputTasks()
            .then(function (status) {
            _this.syncingInputTasks = false;
            _this.syncInputTasksStatus = status;
            _this.statusInputTasks = 1;
        })
            .catch(function (err) {
            _this.syncingInputTasks = false;
            _this.syncInputTasksStatus = err;
            _this.statusInputTasks = 2;
        });
    };
    return ControlComponent;
}());
ControlComponent = __decorate([
    core_1.Component({
        selector: 'control',
        templateUrl: 'ng/app/control/control.component.html'
    }),
    __metadata("design:paramtypes", [Control_service_1.ControlService])
], ControlComponent);
exports.ControlComponent = ControlComponent;
//# sourceMappingURL=control.component.js.map