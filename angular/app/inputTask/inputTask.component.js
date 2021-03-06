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
var task_service_1 = require("../taskService/task.service");
var interest_service_1 = require("../interestService/interest.service");
var InputTaskComponent = (function () {
    function InputTaskComponent(inputTaskService, interestService) {
        this.inputTaskService = inputTaskService;
        this.interestService = interestService;
        this.load = true;
        this.inputTaskList = [];
        this.interestList = [];
        this.counter = 0;
        this.important = [
            new selectItem('N', 'Не важно'),
            new selectItem('I', 'Важно'),
        ];
        this.urgency = [
            new selectItem('N', 'Не срочно'),
            new selectItem('U', 'Срочно'),
        ];
        this.load = true;
    }
    InputTaskComponent.prototype.getInputTasks = function () {
        var _this = this;
        this.inputTaskService
            .getInputTasks()
            .then(function (tasks) {
            _this.inputTaskList = tasks;
            _this.selectedTask = tasks[0];
            _this.load = false;
        });
        this.interestService
            .getInterests()
            .then(function (interests) {
            _this.interestList = interests;
        });
    };
    InputTaskComponent.prototype.ngOnInit = function () {
        this.getInputTasks();
    };
    InputTaskComponent.prototype.deleteTask = function () {
        this.inputTaskService.deleteTask(this.selectedTask)
            .then(function (Response) { return console.log(Response); });
        this.inputTaskList.splice(0, 1);
        if (this.inputTaskList.length > 1) {
            this.selectedTask = this.inputTaskList[0];
        }
        else {
            this.selectedTask = null;
        }
    };
    InputTaskComponent.prototype.toInterest = function (i) {
        this.selectedTask.list_key = i.list_key;
        this.inputTaskService.saveInputTask(this.selectedTask);
        this.inputTaskList.splice(0, 1);
        if (this.inputTaskList.length > 1) {
            this.selectedTask = this.inputTaskList[0];
        }
        else {
            this.selectedTask = null;
        }
    };
    InputTaskComponent.prototype.saveTask = function () {
        this.selectedTask.labels = this.urg.concat(this.imp.toString());
        this.inputTaskService.saveInputTask(this.selectedTask)
            .then(function (resp) { return console.log(resp.toString()); });
        if (this.inputTaskList.length > 1) {
            this.selectedTask = this.inputTaskList[0];
        }
        else {
            this.selectedTask = null;
        }
    };
    return InputTaskComponent;
}());
InputTaskComponent = __decorate([
    core_1.Component({
        selector: 'inputTask',
        templateUrl: 'ng/app/inputTask/inputTask.component.html'
    }),
    __metadata("design:paramtypes", [task_service_1.TaskService,
        interest_service_1.InterestService])
], InputTaskComponent);
exports.InputTaskComponent = InputTaskComponent;
var selectItem = (function () {
    function selectItem(value, name) {
        this.name = name;
        this.value = value;
    }
    return selectItem;
}());
exports.selectItem = selectItem;
;
//# sourceMappingURL=inputTask.component.js.map