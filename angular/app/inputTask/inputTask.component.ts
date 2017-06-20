import {Component} from "@angular/core";
import { FormsModule }   from '@angular/forms';

import { TaskService } from '../taskService/task.service'
import { InterestService } from '../interestService/interest.service'
import { Task } from '../taskService/task'
import { Interest } from '../interestService/interest'

@Component({
    selector: 'inputTask',
    templateUrl:'ng/app/inputTask/inputTask.component.html'
})

export class InputTaskComponent{
	load:Boolean=true;
	inputTaskList: Task[] =[];
	interestList: Interest[]=[];
	selectedTask:Task;
	imp:String;
	urg:String;
	counter:Number = 0;

	important:selectItem[] = [
		new selectItem('N','Не важно'),
		new selectItem('I','Важно'),
	];

	urgency:selectItem[] = [
		new selectItem('N','Не срочно'),
		new selectItem('U','Срочно'),
	];

	  constructor(
    private inputTaskService: TaskService,
    private interestService: InterestService) { this.load=true; }

	  getInputTasks():void{
	  	this.inputTaskService
	  		.getInputTasks()
	  		.then(tasks => {
	  			this.inputTaskList = tasks;
	  			this.selectedTask = tasks[0];
	  			this.load = false;
	  		})
	  	this.interestService
	  		.getInterests()
	  		.then(interests => {
	  			this.interestList =interests;
	  		})
	  }

	  ngOnInit():void {
	  	this.getInputTasks();
	  }

	  deleteTask():void{
	  	this.inputTaskService.deleteTask(this.selectedTask)
	  	.then(Response => console.log(Response) )
		this.inputTaskList.splice(0,1);
	  	if(this.inputTaskList.length > 1){
		  	this.selectedTask = this.inputTaskList[0];
	  	} 
	  	else{
	  		this.selectedTask=null;
	  	}
	  }

	  toInterest(i:Interest):void {
	  	this.selectedTask.list_key = i.list_key;
	  	this.inputTaskService.saveInputTask(this.selectedTask)
		this.inputTaskList.splice(0,1);
	  	if(this.inputTaskList.length > 1){
		  	this.selectedTask = this.inputTaskList[0];
	  	} 
	  	else{
	  		this.selectedTask=null;
	  	}
	  }


	  saveTask():void {
	  	this.selectedTask.labels=this.urg.concat(this.imp.toString());
	  	this.inputTaskService.saveInputTask(this.selectedTask)
	  	.then(resp => console.log(resp.toString()));
	  	if(this.inputTaskList.length > 1){
		  	this.selectedTask = this.inputTaskList[0];
	  	} 
	  	else{
	  		this.selectedTask=null;
	  	}
	  }
}

export class selectItem{
		constructor (
			value:String,
			name:String
			)
		{
			this.name=name;
			this.value=value;
		}
		value:String;
		name:String;
	};
