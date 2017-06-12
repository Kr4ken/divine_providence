import { Injectable }    from '@angular/core';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Interest } from './interest';

@Injectable()
export class InterestService {

  private headers = new Headers({'Content-Type': 'application/json'});
  private interestUrl = '/rest/interests/';  // URL to web api

  constructor(private http: Http) { }

   completeInterest(key: String):Promise<Interest>{
    return this.http.delete(this.interestUrl + key + "/")
               .toPromise()
               .then(response =>response.json() as Interest)
               .catch(this.handleError);

   }

   getInterest(key: String):Promise<Interest>{
    return this.http.get(this.interestUrl + key + "/")
               .toPromise()
               .then(response =>response.json() as Interest)
               .catch(this.handleError);

   }

  getInterests(): Promise<Interest[]> {
    return this.http.get(this.interestUrl)
               .toPromise()
               .then(response => response.json() as Interest[])
               .catch(this.handleError);
   }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
}

