/*****************************************************************
 * Author: Miguel Rosales
 * Description: Get Refresh Token before access ressource
 *****************************************************************/

import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CredentialsService } from '../authentication/credentials.service'

@Injectable()
export class HttpServiceRefreshedAccessToken {

    constructor(
      private credentialService: CredentialsService,
      private http: HttpClient) {}

    private apiUrl(): string {
        //return environment.apiUrl;
        return 'http://localhost:8000';
    }

    private get_refresh_token_ls() {
      try {
        // return JSON.parse(JSON.parse((localStorage.getItem('auth_app_token'))).value).refresh_token;
        let cred = this.credentialService.credentials;
         return cred.refresh;

      }
      catch (expr1) {
        return '';
      }
    }

    get_access_token(): Observable<any> {
        const data = { refresh: this.get_refresh_token_ls() };
        return this.post('api/token/refresh/', data);
    }

    private post(endpoint: string, data:any, options?:any): Observable<any> {
        return this.http.post(`${this.apiUrl()}/${endpoint}`, data, options);
    }
}
