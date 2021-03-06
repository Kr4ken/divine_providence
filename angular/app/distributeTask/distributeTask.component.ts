import {Component} from "@angular/core";
import { FormsModule }   from '@angular/forms';

import { TaskService } from '../taskService/task.service'
import { Task } from '../taskService/task'
import { TaskType } from '../taskService/tasktype'

@Component({
    selector: 'distributeTask',
    templateUrl:'ng/app/distributeTask/distributeTask.component.html'
})

export class DistributeTaskComponent{
	load:Boolean=true;
	distributeTaskList: Task[] =[];
	selectedTask:Task;
	selectedChecklist:checklistItem[];
	newChecklistItem:checklistItem;
	selectedChecklistName:String;
	selectedType:String;
	taskTypes:TaskType[];

	selectedSpecial:special;
	specialDelete:Boolean;

	updateSelectedTask():void{
	  	if(this.distributeTaskList && this.distributeTaskList.length > 0){
		  	this.selectedTask = this.distributeTaskList[0];
		  	let checklist:String[];
		  	console.log(this.selectedTask.checklist);
		  	if(this.selectedTask.checklist != '')
		  	{
			  	checklist = this.selectedTask.checklist.split(';');
			  	this.selectedChecklist = [];
			  	this.selectedChecklistName = checklist[0];
			  	checklist.splice(0,1);
			  	for(let check of checklist) 	  	
			  	{
				  	console.log(check);
				  	let checkName:String;
				  	let checked:Boolean;
				  	checked = check.endsWith(" +")
				  	checkName = checked?check.substring(0,check.length-2):check;
			  		this.selectedChecklist.push(new checklistItem(checked,checkName))
			  	}
		  	}
			this.newChecklistItem = new checklistItem(false,"");

		  	this.selectedSpecial = JSON.parse(this.selectedTask.special.toString());
		  	this.specialDelete = this.selectedSpecial.complete =='delete';
		  } 
	  	else{
	  		this.selectedTask=null;
	  	}
	}


	checkListClear():void{
		if(this.selectedChecklistName=='')
		{
			this.selectedChecklist = []
		}
	}

	checkListDelete(check:checklistItem):void{
		var index = this.selectedChecklist.indexOf(check, 0);
		if (index > -1) {
		   this.selectedChecklist.splice(index, 1);
		}
	}

	onNewCheckListItemChange():void{
		if (this.newChecklistItem.name !=  '')
		{
			this.selectedChecklist.push(this.newChecklistItem);
		  	this.newChecklistItem = new checklistItem(false,"");
		}
	}

	  constructor(private TaskService: TaskService) { this.load=true; }

	  onCheckListClick(item:checklistItem):void{
	  	item.complete = !item.complete;
	  }

	  getDistributeTasks():void{
	  	this.TaskService
	  		.getDistributeTasks()
	  		.then(tasks => {
	  			this.distributeTaskList = tasks;
	  			console.log(tasks)
	  			this.updateSelectedTask();
	  			this.load = false;
	  		})
	  		.catch(err =>
	  			console.log(err))
	  }

	  ngOnInit():void {
	  	this.getDistributeTasks();
	  	this.TaskService
	  		.getTaskTypes()
	  		.then(types => 
	  		{
	  			this.taskTypes = types;
	  			console.log(types);
	  		})
	  }

	  deleteTask():void{
	  	this.TaskService.deleteTask(this.selectedTask)
	  	.then(Response => console.log(Response) )
		this.distributeTaskList.splice(0,1);
	  	this.updateSelectedTask();
	  }

	  fillSelectedTask():void {
	  	this.selectedSpecial.complete = this.specialDelete?'delete':'complete';
	  	this.selectedTask.special = JSON.stringify(this.selectedSpecial);
	  	this.selectedTask.checklist =  this.selectedChecklistName + ';' + this.selectedChecklist.map((v,i) =>  v.name + (v.complete?' +':'')).join(';');
	  	this.selectedTask.list_key = this.selectedType;
	  }

	  saveTask():void {
	  	this.fillSelectedTask();
	  	console.log(this.selectedTask);
	  	this.TaskService.saveDistributeTask(this.selectedTask)
	  	.then(resp => console.log(resp.toString()));
		this.distributeTaskList.splice(0,1);
	  	this.updateSelectedTask();
	  }
}

export class checklistItem{
		constructor (
			complete:Boolean,
			name:String
			)
		{
			this.name=name;
			this.complete=complete;
		}
		complete:Boolean;
		name:String;
	};


export class special{
	complete?:String;
}