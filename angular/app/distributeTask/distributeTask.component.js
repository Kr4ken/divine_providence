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
var DistributeTaskComponent = (function () {
    function DistributeTaskComponent(TaskService) {
        this.TaskService = TaskService;
        this.load = true;
        this.distributeTaskList = [];
        this.load = true;
    }
    DistributeTaskComponent.prototype.updateSelectedTask = function () {
        if (this.distributeTaskList && this.distributeTaskList.length > 1) {
            this.selectedTask = this.distributeTaskList[0];
            var checklist = void 0;
            checklist = this.selectedTask.checklist.split(';');
            this.selectedChecklist = [];
            this.selectedChecklistName = checklist[0];
            checklist.splice(0, 1);
            for (var _i = 0, checklist_1 = checklist; _i < checklist_1.length; _i++) {
                var check = checklist_1[_i];
                console.log(check);
                var checkName = void 0;
                var checked = void 0;
                checked = check.endsWith(" +");
                checkName = checked ? check.substring(0, check.length - 2) : check;
                this.selectedChecklist.push(new checklistItem(checked, checkName));
                this.newChecklistItem = new checklistItem(false, "");
            }
            this.selectedSpecial = JSON.parse(this.selectedTask.special.toString());
        }
        else {
            this.selectedTask = null;
        }
    };
    DistributeTaskComponent.prototype.checkListClear = function () {
        if (this.selectedChecklistName == '') {
            this.selectedChecklist = [];
        }
    };
    DistributeTaskComponent.prototype.checkListDelete = function (check) {
        var index = this.selectedChecklist.indexOf(check, 0);
        if (index > -1) {
            this.selectedChecklist.splice(index, 1);
        }
    };
    DistributeTaskComponent.prototype.onNewCheckListItemChange = function () {
        if (this.newChecklistItem.name != '') {
            this.selectedChecklist.push(this.newChecklistItem);
            this.newChecklistItem = new checklistItem(false, "");
        }
    };
    DistributeTaskComponent.prototype.onCheckListClick = function (item) {
        item.complete = !item.complete;
    };
    DistributeTaskComponent.prototype.getDistributeTasks = function () {
        var _this = this;
        this.TaskService
            .getDistributeTasks()
            .then(function (tasks) {
            _this.distributeTaskList = tasks;
            // this.selectedTask = tasks[0];
            _this.updateSelectedTask();
            _this.load = false;
        });
    };
    DistributeTaskComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.getDistributeTasks();
        this.TaskService
            .getTaskTypes()
            .then(function (types) {
            _this.taskTypes = types;
            console.log(types);
        });
    };
    DistributeTaskComponent.prototype.deleteTask = function () {
        this.TaskService.deleteTask(this.selectedTask)
            .then(function (Response) { return console.log(Response); });
        this.distributeTaskList.splice(0, 1);
        this.updateSelectedTask();
    };
    DistributeTaskComponent.prototype.saveTask = function () {
        this.TaskService.saveInputTask(this.selectedTask)
            .then(function (resp) { return console.log(resp.toString()); });
        this.distributeTaskList.splice(0, 1);
        this.updateSelectedTask();
    };
    return DistributeTaskComponent;
}());
DistributeTaskComponent = __decorate([
    core_1.Component({
        selector: 'distributeTask',
        templateUrl: 'ng/app/distributeTask/distributeTask.component.html'
    }),
    __metadata("design:paramtypes", [task_service_1.TaskService])
], DistributeTaskComponent);
exports.DistributeTaskComponent = DistributeTaskComponent;
var checklistItem = (function () {
    function checklistItem(complete, name) {
        this.name = name;
        this.complete = complete;
    }
    return checklistItem;
}());
exports.checklistItem = checklistItem;
;
var special = (function () {
    function special() {
    }
    return special;
}());
exports.special = special;
//# sourceMappingURL=distributeTask.component.js.map