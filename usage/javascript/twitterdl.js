const ExecrossAPI = require('./exapi');

const api = new ExecrossAPI();

async function main() {
    try {
        const XParams = { url: 'https://x.com/NASA/status/1816862466816496101?t=VAW_bUjPQgCKbxqrovVa6A&s=19' };
        const XData = await api.downloadXpost(XParams);

        if (XData.error) {
            console.error('Error:', XData.error);
        } else {
            console.log('X Data:',XData.data)
            if (Array.isArray(XData.data.result) && XData.data.result.length > 0) {
                const videoData = XData.data.result[0];
                console.log('Cover Image:', videoData.cover);
                console.log('Duration:', videoData.duration);
                console.log('Expanded URL:', videoData.expandedUrl);
                console.log('Text:', videoData.text);

                if (Array.isArray(videoData.videos) && videoData.videos.length > 0) {
                    console.log('\nList of Videos:');
                    videoData.videos.forEach((video, index) => {
                        console.log(`Video ${index + 1}:`);
                        console.log(`  URL: ${video.url}`);
                        console.log(`  Quality: ${video.quality}`);
                    });
                } else {
                    console.log('No videos found.');
                }
            } else {
                console.log('No result data found.');
            }
        }
    } catch (error) {
        console.error('Unexpected Error:', error);
    }
}

main();

/*
X Data: {
  creator: 'EXECROSS',
  ip: '182.1.100.234',
  result: [
    {
      cover: 'https://pbs.twimg.com/media/GTbKx_BXEAAp3_N.jpg',
      duration: '2:13',
      expandedUrl: 'https://twitter.com/NASA/status/1816862466816496101/video/1',
      text: 'Let the games begin!\n' +
        '\n' +
        'Athletes from across the world are gathering today to kick off the 2024 #Olympics – pushing boundaries and inspiring generations. If you were an Olympic athlete, which sport would you play? https://t.co/mnFC3vpvly',
      type: 'video',
      videos: [Array]
    }
  ],
  status: 200
}


Cover Image: https://pbs.twimg.com/media/GTbKx_BXEAAp3_N.jpg
Duration: 2:13
Expanded URL: https://twitter.com/NASA/status/1816862466816496101/video/1
Text: Let the games begin!
Athletes from across the world are gathering today to kick off the 2024 #Olympics – pushing boundaries and inspiring generations. If you were an Olympic athlete, which sport would you play? https://t.co/mnFC3vpvly

List of Videos:
Video 1:
  URL: https://video.twimg.com/amplify_video/1816862298276806656/vid/avc1/480x270/sQaanl62YwMvVLXn.mp4?tag=16
  Quality: 480x270
Video 2:
  URL: https://video.twimg.com/amplify_video/1816862298276806656/vid/avc1/640x360/tlQrNVxJNIvVtmnV.mp4?tag=16
  Quality: 640x360
Video 3:
  URL: https://video.twimg.com/amplify_video/1816862298276806656/vid/avc1/1280x720/X6-mUypEiYZkx4nb.mp4?tag=16
  Quality: 1280x720
Video 4:
  URL: https://video.twimg.com/amplify_video/1816862298276806656/vid/avc1/1920x1080/oK8_XCGVEC35PlUf.mp4?tag=16
  Quality: 1920x1080
*/
