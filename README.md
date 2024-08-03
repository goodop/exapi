# Exapi

Exapi is an API library designed for Line Messenger and social media interactions. This project includes Python, JavaScript and Golang examples to demonstrate its usage.

## Table of Contents

-  [Installation](README.md#installation)

- [Usage](README.md#usage)
  - [Example 1: Using the Module](https://github.com/goodop/exapi/example)
  - [Example 2: Manual Request](https://github.com/goodop/exapi/usage/python)
- [Contributing](#contributing)
- [License](#license)

## Installation

Clone this repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/exapi.git
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

Here's how to use the module in `example.py` :

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
