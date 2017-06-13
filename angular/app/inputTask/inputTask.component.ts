import {Component} from "@angular/core";

import { TaskService } from '../taskService/task.service'

@Component({
    selector: 'inputTask',
    templateUrl:'ng/app/inputTask/inputTask.component.html'
})

export class InputTaskComponent{
	  constructor(
    private inputTaskService: TaskService) { }
}