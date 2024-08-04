const fetch = require('node-fetch')

class ExecrossAPI {
    constructor(base_url, apikey) {
        this.base_url = 'https://execross.com/api/v3';
        this.apikey = 'forexecman';

    }

    async makeRequest(url, params = {}) {
        try {
            const queryString = new URLSearchParams(params).toString();
            const fullUrl = `${this.base_url}${url}?${queryString}`;
            const response = await fetch(fullUrl, {
                method: 'GET',
                headers: {
                    'apikey': this.apikey,
                    'Content-Type': 'application/json'
                }
            });
            if (!response.ok) {
                const errorData = await response.json().catch(() => ({ message: 'Unknown error' }));
                return {
                    status: response.status,
                    data: null,
                    error: errorData
                };
            }
            const data = await response.json();
            return {
                status: response.status,
                data: data,
                error: null
            };
        } catch (error) {
            return {
                status: 500,
                data: null,
                error: { message: 'Network error', details: error.message }
            };
        }
    }

    async getProxies() {
        const endpoint = '/proxies';
        const result = await this.makeRequest(endpoint);
        if (result.status === 200 && result.data.status === 200) {
            const proxies = result.data.result.proxies;
            return {
                status: 200,
                data: _.sample(proxies).split(':')[0],
                error: null
            };
        }
        return result;
    }

    async getQR(params) {
        const url = '/loginqr';
        const url2 = '/reqpin';
        const url3 = '/reqtoken';
        const response = await this.makeRequest(url, params);
        if (response.status === 200 && response.data.status === 200) {
            const params2 = {
                apikey: this.apikey,
                session: response.data.result.session
            };
            const response2 = await this.makeRequest(url2, params2);
            if (response2.status === 200 && response2.data.result.authToken) {
                return response2;
            } else {
                return await this.makeRequest(url3, params2);
            }
        }
        return response;
    }

    async getQRV1(params) {
        const url = '/loginqrv1';
        const url2 = '/reqpinv1';
        const url3 = '/reqtokenv1';
        const response = await this.makeRequest(url, params);
        if (response.status === 200 && response.data.status === 200) {
            const params2 = {
                apikey: this.apikey,
                session: response.data.result.session
            };
            const response2 = await this.makeRequest(url2, params2);
            if (response2.status === 200 && response2.data.result.authToken) {
                return response2;
            } else {
                return await this.makeRequest(url3, params2);
            }
        }
        return response;
    }

    async getEmail(params) {
        const url = '/loginemail';
        const url2 = '/reqemailtoken';
        const response = await this.makeRequest(url, params);
        if (response.status === 200 && response.data.result.pincode) {
            return await this.makeRequest(url2, { apikey: this.apikey });
        }
        return response;
    }

    async getEmailV1(params) {
        const url = '/loginemailv1';
        const url2 = '/reqemailtokenv1';
        const response = await this.makeRequest(url, params);
        if (response.status === 200 && response.data.result.pincode) {
            return await this.makeRequest(url2, { apikey: this.apikey });
        }
        return response;
    }

    async exampleAddFriendPrimary(params) {
        return await this.makeRequest('/addfriend', params);
    }

    async exampleAddFriendSecondary(params) {
        return await this.makeRequest('/addfriend', params);
    }

    async getStory(params) {
        return await this.makeRequest('/linestory', params);
    }

    async getPost(params) {
        return await this.makeRequest('/linepost', params);
    }

    async friendRecomendation(params) {
        return await this.makeRequest('/friendrecommendation', params);
    }

    async messageIdToURL(params) {
        return await this.makeRequest('/msgidtourl', params);
    }

    async convertParseUrlToExtension(params) {
        return await this.makeRequest('/convertparseurl', params);
    }

    async webp2mp4(params) {
        return await this.makeRequest('/webp2mp4', params);
    }

    async mp42gif(params) {
        return await this.makeRequest('/mp42gif', params);
    }

    async vid2Apng(params) {
        return await this.makeRequest('/video2apng', params);
    }

    async downloadSmule(params) {
        return await this.makeRequest('/smuledl', params);
    }

    async instagramPost(params) {
        return await this.makeRequest('/instapost', params);
    }

    async instaStory(params) {
        return await this.makeRequest('/instastory', params);
    }

    async instaStalker(params) {
        return await this.makeRequest('/instastalker', params);
    }

    async instagramProfileDetails(params) {
        return await this.makeRequest('/instaprofiledetails', params);
    }

    async downloadXpost(params) {
        return await this.makeRequest('/twitterdl', params);
    }

    async downloadFacebook(params) {
        return await this.makeRequest('/facebookdl', params);
    }

    async downloadTiktok(params) {
        return await this.makeRequest('/tiktokdl', params);
    }
}

module.exports = ExecrossAPI;
