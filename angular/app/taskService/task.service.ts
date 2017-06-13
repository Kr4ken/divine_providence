import { Injectable }    from '@angular/core';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Task } from './task';

@Injectable()
export class TaskService {

  private headers = new Headers({'Content-Type': 'application/json'});
  private interestUrl = '/rest/tasks/';  // URL to web api

  constructor(private http: Http) { }

}