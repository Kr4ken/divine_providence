import {Component} from "@angular/core";

import { TaskService } from '../taskService/task.service'
import { Task } from '../taskService/task'

@Component({
    selector: 'inputTask',
    templateUrl:'ng/app/inputTask/inputTask.component.html'
})

export class InputTaskComponent{
	inputTaskList: Task[] =[];
	selectedTask:Task;

	  constructor(
    private inputTaskService: TaskService) { }

	  getInputTasks():void{
	  	this.inputTaskService
	  		.getInputTasks()
	  		.then(tasks => {
	  			this.inputTaskList = tasks;
	  			this.selectedTask = tasks[0];
	  		})
	  }

	  ngOnInit():void {
	  	this.getInputTasks();
	  }
}