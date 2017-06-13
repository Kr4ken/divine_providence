import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule }    from '@angular/http';
import { RouterModule, Routes } from '@angular/router' 

import { AppComponent }  from './app.component';
import { CompleteComponent }  from './complete/complete.component';
import { ControlComponent }  from './control/control.component';
import { InputTaskComponent }  from './inputTask/inputTask.component';

import {InterestService} from './interestService/interest.service';
import {ControlService} from './controlService/Control.service';
import {TaskService} from './taskService/task.service'


const appRoutes: Routes = [
  { path: 'interests', component: CompleteComponent},
  { path: 'control', component: ControlComponent},
  { path: 'tasks', component: InputTaskComponent },
  { path: '',
    redirectTo: '/interests',
    pathMatch: 'full'
   }
]

@NgModule({
  imports:      [ 
  BrowserModule,
  HttpModule,
  RouterModule.forRoot(appRoutes)

   ],
  declarations: [
    AppComponent,
    CompleteComponent,
    ControlComponent,
    InputTaskComponent
   ],
  providers: [
  	InterestService,
    ControlService,
    TaskService
    ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
