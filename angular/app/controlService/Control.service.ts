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

  //  completeInterest(key: String):Promise<Interest>{
  //   return this.http.delete(this.interestUrl + key + "/")
  //              .toPromise()
  //              .then(response =>response.json() as Interest)
  //              .catch(this.handleError);

  //  }

  //  getInterest(key: String):Promise<Interest>{
  //   return this.http.get(this.interestUrl + key + "/")
  //              .toPromise()
  //              .then(response =>response.json() as Interest)
  //              .catch(this.handleError);

  //  }

  // getInterests(): Promise<Interest[]> {
  //   return this.http.get(this.interestUrl)
  //              .toPromise()
  //              .then(response => response.json() as Interest[])
  //              .catch(this.handleError);
  //  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
}

