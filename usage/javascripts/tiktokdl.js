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


main();

/*
Result will be:

TikTok Video: {
  creator: 'EXECROSS',
  ip: '45.77.252.122',
  result: {
    ai_dynamic_cover: 'https://p16-sign-va.tiktokcdn.com/obj/tos-maliva-p-0068/2e21a623eea44d4e8a86beacbfa29eb6_1715479326?lk3s=d05b14bd&nonce=33591&refresh_token=c4a806c2fb64cf59b0d04c2d87356d4a&x-expires=1722740400&x-signature=G51piVByeC6tOEUfCzlnRB8U4xQ%3D&s=AWEME_DETAIL&se=false&sh=&sc=dynamic_cover&l=20240803032233A454819825B12952F57D&shp=d05b14bd&shcp=-',
    anchors: null,
    anchors_extras: '',
    author: {
      avatar: 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/2cbdfc7d16623c36b90207431d183c56~c5_300x300.jpeg?lk3s=45126217&nonce=30027&refresh_token=d47f8ff78d982e5b62f9be30638ce907&x-expires=1722740400&x-signature=e3jN53CW9Eg5Anxm9AKCGGCXiO4%3D&shp=45126217&shcp=-',
      id: '6744619110091867138',
      nickname: '𝑨𝒔𝒉𝒂𝒃𝒖𝒍 𝑲𝒂𝒉𝒇𝒊',
      unique_id: 'islamicvibes1445'
    },
    collect_count: 5380,
    comment_count: 71,
    commerce_info: {
      adv_promotable: false,
      auction_ad_invited: false,
      branded_content_type: 0,
      with_comment_filter_words: false
    },
    commercial_video_info: '',
    cover: 'https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/oEzoA48UjxQIBiAjokAhE6viSI6ZB9ZAsAbEA~c5_300x400.jpeg?lk3s=d05b14bd&nonce=48541&refresh_token=b761af97e7db77ec315ec188e294e36c&x-expires=1722740400&x-signature=2nNtb%2FhxSYmyszsok8OmvAojkJ4%3D&s=AWEME_DETAIL&se=false&sh=&sc=cover&l=20240803032233A454819825B12952F57D&shp=d05b14bd&shcp=-',
    create_time: 1715479322,
    digg_count: 24309,
    download_count: 3564,
    duration: 13,
    id: '7367927569280240901',
    is_ad: false,
    item_comment_settings: 0,
    music: 'https://sf16-ies-music-sg.tiktokcdn.com/obj/tiktok-obj/7213421030067440386.mp3',
    music_info: {
      album: '',
      author: 'scars',
      cover: 'https://p16-sign-va.tiktokcdn.com/musically-maliva-obj/1594805258216454~c5_1080x1080.jpeg?lk3s=45126217&nonce=15043&refresh_token=fe242363280f2b1a00eda7dc6b03444b&x-expires=1722740400&x-signature=lYNLvJNVWXjO%2FsS4BwXn0rseiik%3D&shp=45126217&shcp=-',
      duration: 44,
      id: '7213421053140339457',
      original: true,
      play: 'https://sf16-ies-music-sg.tiktokcdn.com/obj/tiktok-obj/7213421030067440386.mp3',
      title: 'Everything Works Out in the end instrumental'
    },
    origin_cover: 'https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/f027a1f92ccf4574a141c57980866df5_1715479324~tplv-tiktokx-360p.image?lk3s=d05b14bd&nonce=96988&refresh_token=8cb0c46262519494266b15ff4b4a99a6&x-expires=1722740400&x-signature=ZwNzennOV2I8sn%2BMDzN883wtISA%3D&s=AWEME_DETAIL&se=false&sh=&sc=feed_cover&l=20240803032233A454819825B12952F57D&shp=d05b14bd&shcp=-',
    play: 'https://v16m-default.akamaized.net/72ab090b88092b5f14aff9aea35cdc6f/66adf6e7/video/tos/useast2a/tos-useast2a-ve-0068c001/okE8A6xivhj09AQJpSCEIzB9BIhAUAjAUqikZ/?a=0&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=208&bt=104&cs=0&ds=6&ft=XE5bCqT0majPD12F5X573wUOx5EcMeF~O5&mime_type=video_mp4&qs=0&rc=NzM8NDs2M2U1NDUzNTM8aUBpM206O3Y5cjM1czMzNzczM0BeNS82X2E2XmExYS0xXl4tYSNxb3AtMmRrMy1gLS1kMTZzcw%3D%3D&vvpl=1&l=20240803032233A454819825B12952F57D&btag=e00088000&shp=6da16bae&shcp=-',
    play_count: 391655,
    region: 'ID',
    share_count: 2634,
    size: 174610,
    title: 'Besok adalah Mystery✨#quotes #quotesislam ',
    wm_size: 161417,
    wmplay: 'https://v16m-default.akamaized.net/4d4fe68c9da4f46bf26b3ea89599f600/66adf6e7/video/tos/useast2a/tos-useast2a-pve-0068/ocmRJPABCBnQCAFR4B7IHZNE7QEDQffKZMXDE0/?a=0&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=192&bt=96&cs=0&ds=6&ft=XE5bCqT0majPD12F5X573wUOx5EcMeF~O5&mime_type=video_mp4&qs=11&rc=PDRnNDQ6ZDxkN2RkZDNlZEBpM206O3Y5cjM1czMzNzczM0AwLy9jYmAyXzExMzNgNjUtYSNxb3AtMmRrMy1gLS1kMTZzcw%3D%3D&vvpl=1&l=20240803032233A454819825B12952F57D&btag=e00088000'
  },
  status: 200
}

*/