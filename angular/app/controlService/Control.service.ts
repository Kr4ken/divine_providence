import { Injectable }    from '@angular/core';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

@Injectable()
export class ControlService {

  private headers = new Headers({'Content-Type': 'application/json'});
  private controlUrl = '/rest/control/';  // URL to web api

  constructor(private http: Http) { }

  syncAllIds():Promise<String>{
    return this.http.post(this.controlUrl+"id/sync/",null)
                    .toPromise()
                    .then(response => response.text() as String)
                    // .catch(this.handleError)
  }

  syncInterestsIds():Promise<String>{
    return this.http.post(this.controlUrl+"int/sync/",null)
                    .toPromise()
                    .then(response => response.text() as String)
                    // .catch(this.handleError)
  }

  syncInputTasks():Promise<String>{
    return this.http.post(this.controlUrl+"input/sync/",null)
                    .toPromise()
                    .then(response => response.text() as String)
                    // .catch(this.handleError)
  }

  syncHabitica():Promise<String>{
    return this.http.post(this.controlUrl+"habitica/sync/",null)
                    .toPromise()
                    .then(response => response.text() as String)
                    // .catch(this.handleError)
  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
}

