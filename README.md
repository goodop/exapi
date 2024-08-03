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

### Example 3: JavaSript Fetch

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
