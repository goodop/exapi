# Installation Instructions

## 1. Install Node.js

### For Debian-based Systems (Ubuntu, etc.)

If Node.js is not already installed, you can install it using `apt`:

```bash
# Update package index
sudo apt update

# Install Node.js and npm (Node Package Manager)
sudo apt install -y nodejs npm

```

### Using wget for install nodejs

```bash
# Download the Node.js setup script
wget -qO- https://deb.nodesource.com/setup_18.x | sudo -E bash -

# Install Node.js and npm
sudo apt-get install -y nodejs

```

### Verify NPM
Ensure Node.js and npm are installed correctly

```bas
node -v

#or

npm -v
```

## 2. Git clone repository.

```bash
git clone https://github.com/goodop/exapi.git
```


### Navigate to the Project Directory

Change to the directory where the exapiJs is located:


```bash

cd exapi/usage/javascripts

```

## 3. Install Dependencies

Install the project's dependencies with npm:

```bash

npm i 

#or 

npm install
```


After done installation you can call the function from file.

example:


```bash

node tiktokDownload.js

```

## 4. ENDPOINT AVAILABLE

You can follow from python endpoint and paramater usage [here](https://github.com/goodop/exapi/blob/main/examples.py)
