# API Request Examples

This examples in both Python and JavaScript for making HTTP requests to an API using the provided URL and endpoint. Whether you're working with Python's requests library or JavaScript's fetch or axios, these examples will help you get started quickly.

## Python Example
In the Python example, we use the requests library to send a GET request to the API. The example demonstrates how to structure the request with the necessary headers and parameters.

### Usage:

```python
import requests

# Define the API endpoint and headers
endpoint = 'https://execross.com/api/v3/smuleprofile'
headers = {
    'apikey': 'forexecman'
}
params = {
    "userId": "SusPended404_",
    "fullpage": False
}
response = requests.get(endpoint, params=params, headers=headers)
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.content)

```

## JavaScript Example
In the JavaScript example, we show how to perform the same API request using both the native fetch API and the popular axios library. These examples are ideal for making requests from a web application or a Node.js environment.

### Fetch Example:

```js
const endpoint = 'https://execross.com/api/v3/smuleprofile';
const headers = {
    'apikey': 'forexecman'
};
const params = new URLSearchParams({
    "userId": "SusPended404_",
    "fullpage": false
});
fetch(`${endpoint}?${params}`, {
    method: 'GET',
    headers: headers
})
.then(response => response.json())
.then(data => console.log('Response:', data))
.catch(error => console.error('Error:', error));
```

### Axios Example:

```javascript
const axios = require('axios');

const endpoint = 'https://execross.com/api/v3/smuleprofile';
const headers = {
    'apikey': 'forexecman'
};
const params = {
    "userId": "SusPended404_",
    "fullpage": false
};

axios.get(endpoint, { headers: headers, params: params })
    .then(response => {
        console.log('Response:', response.data);
    })
    .catch(error => {
        console.error('Error:', error);
    });

```