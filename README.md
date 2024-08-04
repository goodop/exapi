# Exapi

Exapi or Execross API is an API library designed for Line Messenger and social media interactions. This project includes Python, JavaScript and Golang examples to demonstrate its usage.

## Table of Contents

-  [Installation](README.md#installation)

- [Usage](README.md#usage)
  - [Example 1: Using the Module](https://github.com/goodop/exapi/blob/main/examples.py)
  - [Example 2: Manual Request](https://github.com/goodop/exapi/tree/main/usage/python)
  - [Example 3: Javascript Request](https://github.com/goodop/exapi/tree/main/usage/javascript)
- [Contributing](README.md#contributing)
- [License](README.md#license)
- [Endpoint](README.md#Endpoints)
## Installation

Clone this repository and install the required dependencies:

```bash
git clone https://github.com/goodop/exapi.git

cd exapi

pip install -r requirements.txt
```

## Usage

### Example 1: Using the Module
Ensure your project directory is structured as follows:

```bash
root/your-project/
├── exapi/
│   ├── __init__.py
│   └── exapi.py
└── example.py

```

Here's how to use the module in example.py :

```python
from exapi.exapi import ExecrossAPI

def main():
    api = ExecrossAPI()

    params = {
        'apikey': api.apikey,
        'appName': 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
        'authToken': "uc23h7f331c8819j90fa9182db42a6e26:aWF0OiAbmkjDI5OTM2MTU2MDAK....",  # Change to your primary token
        'proxy': None,
        'mid': 'ufed869bc1105aedd331665d57cea407d',  # Target mid
    }

    data = api.exampleAddFriendPrimary(params)
    print(data)

if __name__ == "__main__":
    main()


```
More Example: [visit here](https://github.com/goodop/exapi/blob/main/examples.py)

### Example 2: Manual Request

To make a manual request, you can use a single function in a single file. This approach is useful if you prefer not to use the module structure.

Here’s an example:

```python
import requests

def exampleAddFriendSecondary():
    url = 'https://execross.com/api/v3/addfriend'
    
    params = {
        'apikey': 'forexecman',
        'appName': 'DESKTOPMAC\t8.5.2\tMAC\t10.15.7', #Example Desktop win appname: 'DESKTOPWIN\t8.5.0\tWINDOWS\t10.0'
        'authToken': '', #change with authToken V1 or v3
        'proxy': '47.251.70.179',
        'mid': 'ua7dfa3ce0339d1033e83e6059f0419e1'
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f'Error: {response.status_code}')
        print(response.json())


exampleAddFriendSecondary()

```
More example: [visit here](https://github.com/goodop/exapi/tree/main/usage/python)

### Example 3: JavaScript Fetch

To make fetch ExecrossAPI using javascript you must install node on your system. for detail please read the [instruction](https://github.com/goodop/exapi/blob/main/usage/javascript/README.md).

Here’s an example:

```javascript
const ExecrossAPI = require('./exapi');

const api = new ExecrossAPI();

async function main() {
    try {
        const tiktokParams = { url: 'https://vt.tiktok.com/ZSYwxGV9P/' };
        const tiktokVideo = await api.downloadTiktok(tiktokParams);
        
        if (tiktokVideo.error) {
            console.error('Error:', tiktokVideo.error);
        } else {
            console.log('TikTok Video:', tiktokVideo.data);
        }
    } catch (error) {
        console.error('Unexpected Error:', error);
    }
}
```
more example: [visit here](https://github.com/goodop/exapi/tree/main/usage/javascript)

## Contributing
Feel free to [open issues](https://github.com/goodop/exapi/issues) or submit pull requests. Please ensure your code adheres to the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License - see the  [LICENSE](LICENSE) file for details.


## Endpoints

Host:
```bash
https://execross.com/api/v3
```

<div style="overflow-x:auto; white-space: nowrap;">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="text-align: left; padding: 8px; width: 10%;">No.</th>
      <th style="text-align: left; padding: 8px; width: 30%;">Endpoint</th>
      <th style="text-align: left; padding: 8px; width: 60%;">Parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px;">1</td>
      <td style="padding: 8px;">/proxies</td>
      <td style="padding: 8px;">None</td>
    </tr>
    <tr>
      <td style="padding: 8px;">2</td>
      <td style="padding: 8px;">/loginqr</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - certificate<br>
        - proxy
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">3</td>
      <td style="padding: 8px;">/reqpin</td>
      <td style="padding: 8px;">
        - apikey<br>
        - session
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">4</td>
      <td style="padding: 8px;">/reqtoken</td>
      <td style="padding: 8px;">
        - apikey<br>
        - session
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">5</td>
      <td style="padding: 8px;">/loginqrv1</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - certificate<br>
        - proxy
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">6</td>
      <td style="padding: 8px;">/reqpinv1</td>
      <td style="padding: 8px;">
        - apikey<br>
        - session
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">7</td>
      <td style="padding: 8px;">/reqtokenv1</td>
      <td style="padding: 8px;">
        - apikey<br>
        - session
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">8</td>
      <td style="padding: 8px;">/loginemail</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - certificate<br>
        - email<br>
        - password<br>
        - proxy (optional)
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">9</td>
      <td style="padding: 8px;">/reqemailtoken</td>
      <td style="padding: 8px;">
        - apikey
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">10</td>
      <td style="padding: 8px;">/loginemailv1</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - certificate<br>
        - email<br>
        - password<br>
        - proxy (optional)
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">11</td>
      <td style="padding: 8px;">/reqemailtokenv1</td>
      <td style="padding: 8px;">
        - apikey
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">12</td>
      <td style="padding: 8px;">/addfriend</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - authToken<br>
        - proxy (optional)<br>
        - mid
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">13</td>
      <td style="padding: 8px;">/linestory</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - authToken<br>
        - proxy (optional)<br>
        - mid
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">14</td>
      <td style="padding: 8px;">/linepost</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - authToken<br>
        - proxy (optional)<br>
        - mid<br>
        - postId
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">15</td>
      <td style="padding: 8px;">/friendrecomendation</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - authToken<br>
        - proxy (optional)
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">16</td>
      <td style="padding: 8px;">/msgidtourl</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - authToken<br>
        - proxy (optional)<br>
        - messageId
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">17</td>
      <td style="padding: 8px;">/convertparseurl</td>
      <td style="padding: 8px;">
        - apikey<br>
        - parseURL
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">18</td>
      <td style="padding: 8px;">/webp2mp4</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">19</td>
      <td style="padding: 8px;">/mp42gif</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url<br>
        - start<br>
        - end<br>
        - transparent (optional)
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">20</td>
      <td style="padding: 8px;">/video2apng</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url<br>
        - start<br>
        - end
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">21</td>
      <td style="padding: 8px;">/smuledl</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">22</td>
      <td style="padding: 8px;">/instapost</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">23</td>
      <td style="padding: 8px;">/instastory</td>
      <td style="padding: 8px;">
        - apikey<br>
        - userid
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">24</td>
      <td style="padding: 8px;">/instastalker</td>
      <td style="padding: 8px;">
        - apikey<br>
        - userid
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">25</td>
      <td style="padding: 8px;">/instaprofiledetails</td>
      <td style="padding: 8px;">
        - apikey<br>
        - userid
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">26</td>
      <td style="padding: 8px;">/twitterdl</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">27</td>
      <td style="padding: 8px;">/facebookdl</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">28</td>
      <td style="padding: 8px;">/tiktokdl</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url
      </td>
    </tr>
  </tbody>
</table>
</div>
