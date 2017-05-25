import {Component} from "@angular/core";
import { Interest } from "./Interest"


@Component({
    selector: 'complete',
    templateUrl:'ng/app/complete/complete.component.html'
})
export class CompleteComponent{
	InterestList: Interest[]

}
