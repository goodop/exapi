const ExecrossAPI = require('./exapi');

const api = new ExecrossAPI();

async function main() {
    try {
        const smuleParams = { url: 'https://www.smule.com/recording/wali-baik-baik-sayang/2396057299_4904621977' };
        const smuleData = await api.downloadSmule(smuleParams);
        
        if (smuleData.error) {
            console.error('Error:', smuleData.error);
        } else {
            console.log('Smule Data:', smuleData.data);
        }
    } catch (error) {
        console.error('Unexpected Error:', error);
    }
}


main();

/**
 Result will be:
 Smule Data: {
  creator: 'EXECROSS',
  ip: '123.1.150.24',
  result: {
    audio: 'https://c-fa.cdn.smule.com/smule-gg-uw1-r-5/sing_google/performance/rendered/43/33/d2cb06e3-a72b-439c-88be-0f2a6b27bf51.m4a',   
    thumbnail: 'https://c-fa.cdn.smule.com/smule-gg-uw1-s-5/sing_google/performance/cover/d0/28/6afe733b-cbcd-4dda-b0eb-c0fd2b7dae71.jpg',  
    title: 'Baik Baik Sayang',
    video: 'https://c-fa.cdn.smule.com/smule-gg-uw1-r-6/sing_google/performance/renvideo/8b/2b/6496b24a-b177-4987-bcc1-790ea874d25f.mp4'    
  },
  status: 200
}
 */