const ExecrossAPI = require('./exapi');

const api = new ExecrossAPI();

async function swapWithURLs() {
    const params = {
        originImageURL: 'https://i.ytimg.com/vi/Sw2NisGoa9c/maxres2.jpg',
        faceImageURL: 'https://gate.execross.com/images/ki-arjuna.webp'
    };
    
    const result = await api.swapFaceWithURLs(params);
    if (result.error) {
        console.error('Error:', result.error);
    } else {
        console.log('Swap Face With URLs Result:', result.data);
    }
}

async function swapWithFiles() {
    const originImagePath = 'utils/superman.webp';
    const faceImagePath = 'utils/narji.jpeg';

    const result = await api.swapFaceWithFiles(originImagePath, faceImagePath);
    if (result.error) {
        console.error('Error:', result.error);
    } else {
        console.log('Swap Face With Files Result:', result.data);
    }
}

swapWithURLs();
swapWithFiles();

/*
Swap Face With URLs Result: {
  creator: 'EXECROSS',
  ip: '182.1.70.14',
  result: {
    data: 'https://gate.execross.com/images/media/V9hT4dVU7fzhL6Ta.jpg'
  },
  status: 200
}
Swap Face With Files Result: {
  creator: 'EXECROSS',
  ip: '182.1.70.14',
  result: {
    data: 'https://gate.execross.com/images/media/7tUtAJc_gdcrAX3a.jpg'
  },
  status: 200
}

*/