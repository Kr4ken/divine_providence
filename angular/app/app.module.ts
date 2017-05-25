import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent }  from './app.component';
import { CompleteComponent }  from './complete/complete.component';

@NgModule({
  imports:      [ BrowserModule ],
  declarations: [
    AppComponent,
    CompleteComponent
   ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
