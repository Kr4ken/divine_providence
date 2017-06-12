import {Component} from "@angular/core";

import { ControlService } from '../controlService/Control.service'

@Component({
    selector: 'control',
    templateUrl:'ng/app/control/control.component.html'
})

export class ControlComponent{

	syncIdsStatus:String = 'Не выполнялась';
	status:number = 0;
	syncing:boolean = false;

  syncInterestsIdsStatus:String = 'Не выполнялась';
  statusInterests:number = 0;
  syncingInterests:boolean = false;


  syncInputTasksStatus:String = 'Не выполнялась';
  statusInputTasks:number = 0;
  syncingInputTasks:boolean = false;

  constructor(
    private controlService: ControlService) { }

  	SyncIds():void{
  		console.log('Start')
  		this.syncing = true;
  		this.controlService.syncAllIds()
  							.then(status => {
						  		this.syncing = false;
  								this.syncIdsStatus = status;
  								this.status=1;
  							})
  							.catch(err => {
						  		this.syncing = false;
								this.syncIdsStatus = err;
								this.status=2;
  							})
  	}


    SyncInterestsIds():void{
      console.log('Start')
      this.syncingInterests = true;
      this.controlService.syncInterestsIds()
                .then(status => {
                  this.syncingInterests = false;
                  this.syncInterestsIdsStatus = status;
                  this.statusInterests=1;
                })
                .catch(err => {
                  this.syncingInterests = false;
                this.syncInterestsIdsStatus = err;
                this.statusInterests=2;
                })
    }

    SyncInputTasks():void{
      console.log('Start')
      this.syncingInputTasks = true;
      this.controlService.syncInputTasks()
                .then(status => {
                  this.syncingInputTasks = false;
                  this.syncInputTasksStatus = status;
                  this.statusInputTasks=1;
                })
                .catch(err => {
                  this.syncingInputTasks = false;
                  this.syncInputTasksStatus = err;
                  this.statusInputTasks=2;
                })
    }


}
