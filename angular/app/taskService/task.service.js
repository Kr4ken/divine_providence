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
var http_1 = require("@angular/http");
require("rxjs/add/operator/toPromise");
var TaskService = (function () {
    function TaskService(http) {
        this.http = http;
        this.headers = new http_1.Headers({ 'Content-Type': 'application/json' });
        this.taskUrl = '/rest/tasks/'; // URL to web api
    }
    TaskService.prototype.getInputTasks = function () {
        return this.http.get(this.taskUrl + 'input/')
            .toPromise()
            .then(function (response) { return response.json(); });
    };
    TaskService.prototype.getDistributeTasks = function () {
        return this.http.get(this.taskUrl + 'distribute/')
            .toPromise()
            .then(function (response) { console.log(response.json()); return response.json(); });
    };
    TaskService.prototype.getTaskTypes = function () {
        return this.http.get(this.taskUrl + 'types/')
            .toPromise()
            .then(function (response) { return response.json(); });
    };
    TaskService.prototype.saveInputTask = function (task) {
        return this.http.post(this.taskUrl + 'input/' + task.key + '/', JSON.stringify(task))
            .toPromise()
            .then(function (response) { return response.text(); });
    };
    TaskService.prototype.saveDistributeTask = function (task) {
        return this.http.post(this.taskUrl + 'distribute/' + task.key + '/', JSON.stringify(task))
            .toPromise()
            .then(function (response) { return response.text(); });
    };
    TaskService.prototype.deleteTask = function (task) {
        return this.http.delete(this.taskUrl + 'input/' + task.key + '/')
            .toPromise()
            .then(function (response) { return response.text(); });
    };
    return TaskService;
}());
TaskService = __decorate([
    core_1.Injectable(),
    __metadata("design:paramtypes", [http_1.Http])
], TaskService);
exports.TaskService = TaskService;
//# sourceMappingURL=task.service.js.map