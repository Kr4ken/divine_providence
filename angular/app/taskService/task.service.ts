import { Injectable }    from '@angular/core';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Task } from './task';

@Injectable()
export class TaskService {

  private headers = new Headers({'Content-Type': 'application/json'});
  private taskUrl = '/rest/tasks/';  // URL to web api

  constructor(private http: Http) { }

  getInputTasks(): Promise<Task[]> {
    return this.http.get(this.taskUrl + 'input/')
               .toPromise()
               .then(response => response.json() as Task[])
   }

   saveInputTask(task:Task):Promise<String>{
   	return this.http.post(this.taskUrl + 'input/' + task.key + '/',JSON.stringify(task))
   					.toPromise()
   					.then(response => response.text() as String)
   }

   deleteTask(task:Task):Promise<String> {
   	return this.http.delete(this.taskUrl + 'input/'+ task.key + '/')
   					.toPromise()
   					.then(response => response.text() as String)
   }

}