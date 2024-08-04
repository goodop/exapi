const ExecrossAPI = require('./exapi');

const api = new ExecrossAPI();

async function main() {
    try {
        const fbParams = { url: 'https://www.facebook.com/share/r/aYSqb2vVTUrRqaTG/?mibextid=0VwfS7' };
        const fbData = await api.downloadFacebook(fbParams);
        
        if (fbData.error) {
            console.error('Error:', fbDataData.error);
        } else {
            console.log('FB Data:', fbData.data);
        }
    } catch (error) {
        console.error('Unexpected Error:', error);
    }
}


main();

/*
Result will be:
FB Data: {
  creator: 'EXECROSS',
  ip: '123.1.150.24',
  result: {
    videoHD: 'https://video-lga3-2.xx.fbcdn.net/o1/v/t2/f2/m69/An-JOYMYugvU7WQJkmO8GBjESw5V58kx1QbOFeB4e2Z8-iEP8YNNmoPgKbN6V7ZV2O99LMbIG_-IhY5VkFXFJI7G.mp4?efg=eyJ2ZW5jb2RlX3RhZyI6Im9lcF9oZCJ9&_nc_ht=video-lga3-2.xx.fbcdn.net&_nc_cat=100&strext=1&vs=34e5953ff0b7d50c&_nc_vs=HBksFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HQTE1M0JvX2JzTktlS1liQUVsMGhoZ1p5cTFyYm1kakFBQUYVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dKNkUweHJyQ19kY1lTY0dBS3lHczhGbW9lZFRickZxQUFBRhUCAsgBAEsHiBJwcm9ncmVzc2l2ZV9yZWNpcGUBMQ1zdWJzYW1wbGVfZnBzABB2bWFmX2VuYWJsZV9uc3ViACBtZWFzdXJlX29yaWdpbmFsX3Jlc29sdXRpb25fc3NpbQAoY29tcHV0ZV9zc2ltX29ubHlfYXRfb3JpZ2luYWxfcmVzb2x1dGlvbgAddXNlX2xhbmN6b3NfZm9yX3ZxbV91cHNjYWxpbmcAEWRpc2FibGVfcG9zdF9wdnFzABUAJQAcjBdAAAAAAAAAABERAAAAJsy3vby5zcwBFQIoAkMzGAt2dHNfcHJldmlldxwXQBG%2FfO2RaHMYGWRhc2hfaDI2NC1iYXNpYy1nZW4yXzcyMHASABgYdmlkZW9zLnZ0cy5jYWxsYmFjay5wcm9kOBJWSURFT19WSUVXX1JFUVVFU1QbCogVb2VtX3RhcmdldF9lbmNvZGVfdGFnBm9lcF9oZBNvZW1fcmVxdWVzdF90aW1lX21zATAMb2VtX2NmZ19ydWxlB3VubXV0ZWQTb2VtX3JvaV9yZWFjaF9jb3VudAYzMzY3MDYRb2VtX2lzX2V4cGVyaW1lbnQADG9lbV92aWRlb19pZA84NzUxNjg2NTExMjMzMjcSb2VtX3ZpZGVvX2Fzc2V0X2lkDzgwMjIyODcxNTQyMzkxNBVvZW1fdmlkZW9fcmVzb3VyY2VfaWQPNDQ5OTMxMzA3ODg4MTAyHG9lbV9zb3VyY2VfdmlkZW9fZW5jb2RpbmdfaWQPODQ3NDQ5OTIwNjM4OTI1DnZ0c19yZXF1ZXN0X2lkACUCHAAlvgEbB4gBcwQ1NjA1AmNkCjIwMjQtMDctMDgDcmNiBjMzNjcwMANhcHATRmFjZWJvb2sgZm9yIGlQaG9uZQJjdA5GQl9TSE9SVFNfUE9TVBNvcmlnaW5hbF9kdXJhdGlvbl9zCDQuNDIzMzMzAnRzFXByb2dyZXNzaXZlX2VuY29kaW5ncwA%3D&ccb=9-4&oh=00_AYBN6NXhkBeZPju00qS8i-aL3HBvsKYwSKy_rky3luFmXg&oe=66B0F9BF&_nc_sid=1d576d&_nc_rid=341571376121170&_nc_store_type=1&dl=1',
    videoSD: 'https://video-lga3-2.xx.fbcdn.net/v/t42.1790-2/450386623_1028185725617301_5034010174479634758_n.mp4?_nc_cat=104&ccb=1-7&_nc_sid=55d0d3&efg=eyJ2ZW5jb2RlX3RhZyI6InN2ZV9zZCIsInZpZGVvX2lkIjo4NzUxNjg2NTExMjMzMjd9&_nc_ohc=xtYkp5CdtAYQ7kNvgGRij3N&_nc_ht=video-lga3-2.xx&edm=AGo2L-IEAAAA&oh=00_AYBNcqakSeNltb12yj8QLkWR1C5cID7L0zWWiOaX2ZaRxQ&oe=66B4F0AA&dl=1'
  },
  status: 200
}
 */