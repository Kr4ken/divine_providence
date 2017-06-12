import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule }    from '@angular/http';
import { RouterModule, Routes } from '@angular/router' 

import { AppComponent }  from './app.component';
import { CompleteComponent }  from './complete/complete.component';
import { ControlComponent }  from './control/control.component';

import {InterestService} from './interestService/interest.service';
import {ControlService} from './controlService/Control.service';

const appRoutes: Routes = [
  { path: 'interests', component: CompleteComponent},
  { path: 'control', component: ControlComponent},
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
    ControlComponent
   ],
  providers: [
  	InterestService,
    ControlService
    ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
