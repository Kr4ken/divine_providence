import { provideRouter, RouterConfig } from '@angular/router';
import {Component1Component} from "./component1.component";
import {Component2Component} from "./component2.component";
import {DjangoComponent} from "./django.component";
import {CompleteComponent} from "./complete/complete.component";


const routes: RouterConfig = [
  {path: '',redirectTo: '/component1',pathMatch: 'full'},
  { path: 'component1', component: Component1Component },
  { path: 'component2', component: Component2Component },
  { path: 'completeComponent', component: CompleteComponent },
  { path: 'djcomponent', component: DjangoComponent },
];

export const appRouterProviders = [
  provideRouter(routes)
];
