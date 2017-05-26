import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule }    from '@angular/http';

import { AppComponent }  from './app.component';
import { CompleteComponent }  from './complete/complete.component';

import {InterestService} from './interestService/interest.service';

@NgModule({
  imports:      [ 
  BrowserModule,
  HttpModule
   ],
  declarations: [
    AppComponent,
    CompleteComponent,
   ],
  providers: [
  	InterestService
    ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
