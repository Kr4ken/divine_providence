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
    private interestService: InterestService) { }

	  getInputTasks():void{
	  	this.inputTaskService
	  		.getInputTasks()
	  		.then(tasks => {
	  			this.inputTaskList = tasks;
	  			this.selectedTask = tasks[0];
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


	  saveTask():void {

	  	this.selectedTask.labels=this.urg.concat(this.imp);
	  	if(this.inputTaskList.length > 1){
		  	this.inputTaskList.splice(0,1);
		  	this.selectedTask = this.inputTaskList[0];
	  	} 
	  	else {
	  		console.log('Нет элементов')
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
