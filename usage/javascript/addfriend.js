const ExecrossAPI = require('./exapi');

const api = new ExecrossAPI();

async function main() {
    try {
        const addParams = {
            appName: 'ANDROID\t13.19.1\tANDROID\t12.3.3772',
            authToken: 'uf331c8819d10fa9182db42a6e26:aWF0OiAxMDI5OTM2MTU2MDAK..',  // change with your primary token
            proxy: '',
            mid: 'uca5cbd3fcf6d4344c8ad21ae54c6f9a3',
        }
        const addData = await api.exampleAddFriendPrimary(addParams);
        
        if (addData.error) {
            console.error('Error:', addData.error);
        } else {
            console.log('AddFriend Data:', addData.data);
        }
    } catch (error) {
        console.error('Unexpected Error:', error);
    }
}


main();

/*
Add Friend Data: {
  creator: 'EXECROSS',
  ip: '182.1.100.234',
  proxy: '',
  result: { message: 'success add mrkeceme75 as friend.' },
  status: 200
}
*/