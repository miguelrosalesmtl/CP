import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs'
import { mergeMap } from 'rxjs/operators';
import { CredentialsService } from '../authentication/credentials.service'
import { HttpServiceRefreshedAccessToken } from './http.service.refreshed-access-token'

export class HttpSecuredService {

    constructor(
        private _credentialService:CredentialsService,
        private _tokenService: HttpServiceRefreshedAccessToken,
        private _http:HttpClient) {}

        apiUrl(): string {
            return 'http://localhost:8000';
        }
    
        get(endpoint: string, query_params: string = '', options?:any): Observable<any> {
            return this._tokenService.get_access_token().pipe(
                mergeMap(token => {
                    options = { observe: 'response', headers: {'Authorization': `Bearer ${ token.access}`}};
                    return this._http.get(`${this.apiUrl()}/${endpoint}?${query_params}`, options);
                }));
        }
    
        post(endpoint: string, query_params: string = '', data:any, options?:any): Observable<any> {
            return this._tokenService.get_access_token().pipe(
                mergeMap(token => {
                    options = { observe: 'response', headers: {'Authorization': `Bearer ${ token.access}`}};
                    return this._http.post(`${this.apiUrl()}/${endpoint}?${query_params}`, data, options);
                }));
        }
    
        put(endpoint: string, query_params: string = '', data:any, options?:any): Observable<any> {
            return this._tokenService.get_access_token().pipe(
                mergeMap(token => {
                    options = { observe: 'response', headers: {'Authorization': `Bearer ${ token.access}`}};
                    return this._http.put(`${this.apiUrl()}/${endpoint}?${query_params}`, data, options);
                }));
        }
    
        delete(endpoint: string, query_params: string = '', options?:any): Observable<any> {
            return this._tokenService.get_access_token().pipe(
                mergeMap(token => {
                    options = { observe: 'response', headers: {'Authorization': `Bearer ${ token.access}`}};
                    return this._http.delete(`${this.apiUrl()}/${endpoint}?${query_params}`, options);
                }));
        }
}
