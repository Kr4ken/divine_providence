import {Component} from "@angular/core";
import { Interest } from "../interestService/interest"
import { InterestService } from "../interestService/interest.service"


@Component({
    selector: 'complete',
    templateUrl:'ng/app/complete/complete.component.html'
})
export class CompleteComponent{
	interestList: Interest[] = [];
	selectedInterest: Interest;

  constructor(
    private interestService: InterestService) { }

  getInterests(): void {
  	// this.interestList = this.interestService.getInterestsTest();
  	this.interestService
  		.getInterests()
   
  		.then(interests =>{this.interestList = interests; this.selectedInterest = this.interestList[0];});
  }

  findInterestIndex(interest:Interest):number {
  	for (var i = this.interestList.length - 1; i >= 0; i--) {
  		if(this.interestList[i] == this.selectedInterest){
  			return i;
  		}
  	}
  	return -1;
  }

  completeInterest():void{
  	this.interestService
  	.completeInterest(this.selectedInterest.key)	
  	.then(interest => {
  		this.interestList[this.findInterestIndex(this.selectedInterest)] = interest;
  		this.selectedInterest = interest});
  }


  ngOnInit(): void {
    this.getInterests();
  }

  onSelect(interest: Interest): void {
    this.selectedInterest = interest;
  }

}
