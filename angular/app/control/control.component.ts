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



}
