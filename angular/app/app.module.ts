import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule }    from '@angular/http';
import { RouterModule, Routes } from '@angular/router' 
import { FormsModule }   from '@angular/forms';

import { AppComponent }  from './app.component';
import { CompleteComponent }  from './complete/complete.component';
import { ControlComponent }  from './control/control.component';
import { InputTaskComponent }  from './inputTask/inputTask.component';
import { DistributeTaskComponent }  from './distributeTask/distributeTask.component';

import {InterestService} from './interestService/interest.service';
import {ControlService} from './controlService/Control.service';
import {TaskService} from './taskService/task.service'


const appRoutes: Routes = [
  { path: 'interests', component: CompleteComponent},
  { path: 'control', component: ControlComponent},
  { path: 'tasks/input', component: InputTaskComponent },
  { path: 'tasks/distribute', component: DistributeTaskComponent},
  { path: '',
    redirectTo: '/interests',
    pathMatch: 'full'
   }
]

@NgModule({
  imports:      [ 
  BrowserModule,
  HttpModule,
  RouterModule.forRoot(appRoutes),
  FormsModule

   ],
  declarations: [
    AppComponent,
    CompleteComponent,
    ControlComponent,
    InputTaskComponent,
    DistributeTaskComponent
   ],
  providers: [
  	InterestService,
    ControlService,
    TaskService
    ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
