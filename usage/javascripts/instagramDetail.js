const ExecrossAPI = require('./exapi');

const api = new ExecrossAPI();

async function main() {
    try {
        const instagramProfile = { userid: 'this.ang' };
        const instagramDetail = await api.instagramProfileDetails(instagramProfile);
        
        if (instagramDetail.error) {
            console.error('Error:', instagramDetail.error);
        } else {
            console.log('Response: ', instagramDetail.data);
            console.log('Post: ', instagramDetail.data.result.post)
            console.log('highlight: ', instagramDetail.data.result.highlight)
        }
    } catch (error) {
        console.error('Unexpected Error:', error);
    }
}


main();

/*
Response:  {
  creator: 'EXECROSS',
  ip: '45.77.252.122',
  result: {
    highlight: [ [Object], [Object] ],
    post: [ [Object], [Object], [Object], [Object] ],
    profile: {
      account_badges: [],
      account_category: '',
      account_type: 1,
      additional_business_addresses: [],
      adjusted_banners_order: [],
      ads_incentive_expiration_date: null,
      ads_page_id: null,
      ads_page_name: null,
      auto_expand_chaining: null,
      bio_links: [Array],
      biography: "👨‍💻 Coding in the Quiet 🌄 | 📚 Exploring Algorithms | 🌿 Nature Enthusiast | ☕ Coffee Lover | Let's Connect and Code!",
      biography_with_entities: [Object],
      birthday_today_visibility_for_viewer: 'NOT_VISIBLE',
      can_add_fb_group_link_on_profile: false,
      can_hide_category: true,
      can_use_affiliate_partnership_messaging_as_brand: false,
      can_use_affiliate_partnership_messaging_as_creator: false,
      can_use_branded_content_discovery_as_brand: false,
      can_use_branded_content_discovery_as_creator: false,
      can_use_paid_partnership_messaging_as_creator: false,
      category: null,
      chaining_upsell_cards: [],
      creator_shopping_info: [Object],
      current_catalog_id: null,
      displayed_action_button_partner: null,
      displayed_action_button_type: null,
      eligible_for_text_app_activation_badge: false,
      existing_user_age_collection_enabled: true,
      external_lynx_url: 'https://l.instagram.com/?u=http%3A%2F%2Fang.execross.com%2F&e=AT3Eov6Ko05JzUCw4MLZoRZ3pRRRO3C1zVTn8Xoxt-iWzJZGELmcQCHA6KVT5UMosDojWuH1LmtJ27Mf6K8orIU375OWHxgGJhl8Vg',
      external_url: 'http://ang.execross.com',
      fan_club_info: [Object],
      fbid_v2: '17841445628173718',
      feed_post_reshare_disabled: true,
      follow_friction_type: 0,
      follower_count: 6353,
      following_count: 136,
      full_name: 'Asking Ang',
      has_anonymous_profile_picture: false,
      has_chaining: false,
      has_collab_collections: false,
      has_ever_selected_topics: false,
      has_exclusive_feed_content: false,
      has_fan_club_subscriptions: false,
      has_guides: false,
      has_highlight_reels: true,
      has_ig_profile: true,
      has_music_on_profile: false,
      has_private_collections: false,
      has_public_tab_threads: true,
      has_videos: false,
      hd_profile_pic_url_info: [Object],
      hd_profile_pic_versions: [Array],
      highlight_reshare_disabled: false,
      highlights_tray_type: 'DEFAULT',
      id: '45629744939',
      include_direct_blacklist_status: true,
      interop_messaging_user_fbid: '17842490168520940',
      is_bestie: false,
      is_business: false,
      is_call_to_action_enabled: null,
      is_category_tappable: false,
      is_creator_agent_enabled: false,
      is_direct_roll_call_enabled: true,
      is_eligible_for_meta_verified_enhanced_link_sheet: false,
      is_eligible_for_meta_verified_enhanced_link_sheet_consumption: false,
      is_eligible_for_meta_verified_label: true,
      is_eligible_for_meta_verified_links_in_reels: true,
      is_eligible_for_meta_verified_multiple_addresses_consumption: false,
      is_eligible_for_meta_verified_multiple_addresses_creation: false,
      is_eligible_for_meta_verified_related_accounts: false,
      is_eligible_for_request_message: false,
      is_favorite: false,
      is_in_canada: false,
      is_interest_account: true,
      is_memorialized: false,
      is_meta_verified_related_accounts_display_enabled: false,
      is_new_to_instagram: false,
      is_opal_enabled: false,
      is_open_to_collab: false,
      is_oregon_custom_gender_consented: false,
      is_parenting_account: false,
      is_potential_business: false,
      is_private: false,
      is_profile_broadcast_sharing_enabled: true,
      is_profile_picture_expansion_enabled: true,
      is_recon_ad_cta_on_profile_eligible_with_viewer: false,
      is_regulated_c18: false,
      is_regulated_news_in_viewer_location: false,
      is_remix_setting_enabled_for_posts: true,
      is_remix_setting_enabled_for_reels: true,
      is_secondary_account_creation: true,
      is_stories_teaser_muted: false,
      is_supervision_features_enabled: false,
      is_verified: false,
      is_whatsapp_linked: false,
      latest_besties_reel_media: 0,
      latest_reel_media: 1722607909,
      live_subscription_status: 'default',
      media_count: 6,
      meta_verified_related_accounts_count: 0,
      mini_shop_seller_onboarding_status: null,
      mutual_followers_count: 0,
      nametag: {},
      num_of_admined_pages: null,
      open_external_url_with_in_app_browser: true,
      page_id: null,
      page_name: null,
      pinned_channels_info: [Object],
      pk: '45629744939',
      pk_id: '45629744939',
      primary_profile_link_type: 0,
      professional_conversion_suggested_account_type: 3,
      profile_context: '',
      profile_context_facepile_users: [],
      profile_context_links_with_user_ids: [],
      profile_pic_id: '3386020719048734789_45629744939',
      profile_pic_url: 'https://instagram.fjog13-1.fna.fbcdn.net/v/t51.2885-19/448054598_2717759565065970_3110878031122831592_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fjog13-1.fna.fbcdn.net&_nc_cat=106&_nc_ohc=RLYXacCvvfwQ7kNvgFz4wSG&gid=cc1c9746dda24a1aa7ceb2181ac93fdc&edm=AEF8tYYBAAAA&ccb=7-5&oh=00_AYDJkkyUl_BHBJJqujd3bHN1y6yojQTvlfo2hJP03NuTOA&oe=66B35206&_nc_sid=1e20d2',
      profile_pic_url_signature: [Object],
      profile_type: 0,
      pronouns: [],
      recs_from_friends: [Object],
      relevant_news_regulation_locations: [],
      remove_message_entrypoint: false,
      shopping_post_onboard_nux_type: null,
      show_account_transparency_details: true,
      show_fb_link_on_profile: false,
      show_fb_page_link_on_profile: false,
      show_ig_app_switcher_badge: true,
      show_post_insights_entry_point: true,
      show_schools_badge: null,
      show_text_post_app_badge: true,
      show_text_post_app_switcher_badge: true,
      smb_delivery_partner: null,
      smb_support_delivery_partner: null,
      smb_support_partner: null,
      spam_follower_setting_enabled: true,
      strong_id__: '45629744939',
      text_app_last_visited_time: null,
      text_post_app_badge_label: 'this.ang',
      text_post_app_joiner_number: 83175975,
      text_post_app_joiner_number_label: '83,175,975',
      text_post_new_post_count: 0,
      third_party_downloads_enabled: 0,
      threads_profile_glyph_url: 'https://www.threads.net/@this.ang?xmt=AQGzuscKu8_PSKrF5uqhVJ59BWZ-YoTLf81PzbGdLcC_V64',
      total_ar_effects: 0,
      total_igtv_videos: 0,
      transparency_product_enabled: false,
      username: 'this.ang'
    },
    storie: { result: [Array] }
  },
  status: 200
}


# Response Post:

Post:  [
  {
    comments: '\n            0\n        ',
    description: 'SunSet',
    id: '3167695353361664810',
    is_video: false,
    likes: '\n            1k\n        ',
    thumb: 'https://flufi-cdn.com/instagram/U2FsdGVkX1/tsOBtIxVXcuvnFDcm8OnXiWX+9Qw4dPdchti0b8i5HQ2Va+HZAh4vBCKUtmpGDNkXEQOyYotSo4FRHdI1XTIS4cTQCzSg46u072orFjDBemjS4F/z/cvcV+9/Y/qS/VSU6HbCDp6le+p421hNu3Z9IoM4p5nt9h0cTIJWMnmBNIa/MwWGJFXIKvgMRmULLf9psxP8wLQc/sn6XaGJKW6bfngOWXEgpkJzAWDd1W/BqcS7mzdWE/qB4LG9rckCW33hu+PT331PGx2Qqox/4Ph1x+RocYEmaKCGDIV6lqamtniePWgbiXHKqaDfpZG7vSNx8vaFFRlX6Wpx45juvQfhjlAaEjv/RpydYoBSNZQ24vBMn2kzsOxJfbckPud5KP29jzND/4Usqg+szJJSRCkpfoFj6iDkZPLMDr4lCmUQZjB3d4+bPQou/BNvrwRTTmZjaZXKW+3z52vSIiD4UE8APHGLA/2Iv6laSo2OHkq9lHYAo6B54gtSysw7piA7P7ey7n+tlimFLd9WvD3uyWqM/XWTa8sWZ/AjPpjUGIlEU4bu47/EhJen9XFjMepGajaKL5MyQ7ATZ4STTodD4ARXnULwsLimdqoDG2IDZJEFrHnK2P37leFcZ0SNIONGrPp+19UcB46kulkNovqre4g2qM0HZGiVmTATbTCTPJOO7qZDBxpHEpoBOaugQ6X1nSzOSNnOE1pca68puFrOWS+ZTKDOo766Ui8lp9MGypEYFn8y3s83pR4BSG1z9sRnXSMhKAbcJ+bKaeEIqPVWrhIzR90vu55Cq7iojYiA4ZVBcxsyY+pDXZF46NgjMxJBApmFB/mQtfKONA==',
    time: '11 months ago'
  },
  {
    comments: '\n            0\n        ',
    description: '#Bird',
    id: '3167692770140016835',
    is_video: false,
    likes: '\n            1k\n        ',
    thumb: 'https://flufi-cdn.com/instagram/U2FsdGVkX1/ogFrTucorQnciJH2K59saVG8GCob+WFMYBe6Xfb9kQuDFP5f2OziJl9/EwsCPh3XkKUuzMu/cNd2mzzFAQ8uvAY3ukMBDvcnJQ2BUHq6fbw0u5diNwAm9kVrIxuxJ0eUnbzfIQts58DnIWoJ+yX+IPtzHpOUWryzCqq1YuELv/cU5lPhN9jBQ2ORJfJagUaCaWgvccF/xssecgQGr6CDzbmhDNNfKkSBUj8AT5Rm+sd4Eh/SXS7dbPKSUt/e6xE7SbxMHSjc8cUDW9wfhSRX4t+6xaXcBI17Q8iWxRoi7DHrxbpu6oMB/OL3G9c7154eNE3RTaXwPQ6sR4dg0BHFh3e9TBQnL1DpfL/Zh2DTlktvVYwA7gEZsaIar4PWnJ1VZSYPB8rdoHtUvoJPDe8E+es0iK0HyYzo77hqN1/UXsgo6EOYsXMShW77ovPjEDHlsTz2Mi8+8U6AbstYC5GRXb2OxGIuIyxJFo6X2d4COuV9I13WOjP6+YlwUv/bJjeA9feR/4++rLyeQWljH9BLn/UfzucMT84uz0uFiej6XMRDaxuXw9qnTA5flxp0bzsgfcOYbv6xOJUw3c+O3WMtJACS4fQE1tO02oReeUsf1H16HrFMR4DzOG9Wq1TNqKvnGhOWTPhlIGdfB+V5Y8+VN3T6Diave5l7J6+Fj1606V6bCtUT45Duhrlh2yDee+dHWG2+nf9T1L4YM0oiarXc8oVbOFD04dKZ/N9NNBPJD1kLF+C3U/z8q81BfPm08MZpk2/vFZyoUUrnOCiTCVN7yPX8s3wSScecUYp+9cFlAcgn6UQMSqAI8L+MvenO9KJ70QpHWuYmd3w==',
    time: '11 months ago'
  },
  {
    comments: '\n            0\n        ',
    description: 'Hmm',
    id: '2529319547288491459',
    is_video: false,
    likes: '\n            1k\n        ',
    thumb: 'https://flufi-cdn.com/instagram/U2FsdGVkX18DrgE+NMXhrP70isp/WUnB4YqdVgp8vcR2teJFyrTky+BdPckbCPHni8hTvMIVDfd6IcVfPeGB1LwQOUc9NTEKWlCZuu5hALLVLEpP4JzD90en4YQ9NbxDKrzIVPQPgpev0oHVShiN9WUvNybuHZGRS0gBzQkqvBzHwtJudWVSv42Y1/ehPxXX36GpkndxDAH2Rp7uZq19gHRcMmGr+yETZWIV06tyfDs7dzOD01/ysW5rUUM3oQch7TjEHzM6yK+lHz5EcLGdo+3BUeRB2s9z1CMO/AEG7lCobM1NGhMn1CGF9lNvHczkHR8/KjAax3tjDnY6PtznMaJw1RQgq5FNF7Uw1oOBBvy0BcdHj418YutbpuoKejSWCVTsEWjsu7qd/bpkygWVnmpVjdaYzg3LbQNqr2sLev+ofrByhcPwXdoqIAlH7cI6jMsviqxWBGf3i1Bgun8r8WHP3dGG7JIlgVZGNrj7KDQTPHAm8/jw6xjBRF7lypmYYT5GDhQkvbRh5EMFo5IC5Bq6Ie6t7BvuUnrP7+ZyM2An+I8wqzwJc2G1WY95urdSH4w7PLewTR7efeEv6tSYGRMvA/25pU+O5+zsappXnMY6UkbledF157Znx2kNuk+VKl/YqQWrYzM/tN+wfj9/8owFMm691Dohv0O0kbno2b9NVj6b197mOCH2gzDPgvj0n1+oMxD+8fvrldbLucz08SB72rGcCzGNo9ME6KSXvlIkLsLKXq1kMgwZi8o2iubtUwO491gTLWvgmG2mlwsb0rClftSECxpdebVwenOUqIM9wJXcJ1X1BGAdKVwjyX5lJPLjs67/CB+i1ASstF+dqw==',
    time: '3 years ago'
  },
  {
    comments: '\n            0\n        ',
    description: "Unless you don't realize your mistake, you haven't done it. Just like error of code that teaches us something we didn't know before. Full Documentation: https://api.imjustgood.com #apimedia #apiinstagram #imjustgood",
    id: '2521397771152493432',
    is_video: false,
    likes: '\n            2k\n        ',
    thumb: 'https://flufi-cdn.com/instagram/U2FsdGVkX1/eeS0llKU3bo+OIKSomaGTi84be8i+TkGho7mkTgR8sbM08fWVPq5jNGEnv1R8AIQVfp2ml+F6tX+C9qqsKSyyyJ7gBqUzWbZ6JitHgM0w6NLUoe6cms+WmkVA/vzjEfDIufihP7DxijgjYxfYdcQbqRcMVg7HlgJkqQOhSbymP9a5+OFmqMTciB0ARHfXDf8tA5R6gnBXBIpQkDXY1Qh8HHf2bICCgv/2PWAvC42v4YrG/lSk8rvqrmRlrMHO5Z1cXEdFfhRNJVcVq7ecxMBINYaY6rg6QOswDud+4aHlbtoJ8w0qOa7Z1D/FzUrJO76Zzlf9iWMqu86/2QhhSdVUVi2deRV/1SdoU22EMjIUly59RRwxSyFWylJ3O9OHk8bvPoFXha0kQC6qGc4/SoXRdG2ar7nOsZu8VXI+uVw6aueXiv4vtnRLOAD/sC40vUaOuS5zbL+U7YizW1JQDn4LiM+UUfJzn/9VJnh/KfMq/mJwtGLPZJboXZeBfEmNqF+lU5pw57CuZcNtGI8k5Ut6ZwWNb9quzhAMwQbysHpyb5gFpwTgdxFAobWSmZ7Z74L3C8G/xCf2UV+N52IU2x9Tw60YrshcYYulRcRO1g58ggra8ZH6wiIyUWsOfffGHo1rTlTTqgiDNBhuX6fHowSrVSHGIp5KNo4ZPSs4NgrnBBGoU1KNGMif3YU8JpxZ2nHgKrtP8cZuZmxahGU6TkFZzuYya36L3LSs8gnLU0pl8H+xe2f0VyTOWS7TUVNW3HotE469SAHt0rfBuJGHNu7ujejAuztLq9iX4MHcyMNzdku1L+HPgUZ8IYWzsaFHBqlBQUL7j/rlTg==',
    time: '3 years ago'
  }
]

# Response Hightligh:

highlight:  [
  {
    cover_media: { cropped_image_version: [Object] },
    id: 'highlight:17901626525970784',
    title: "Dhiyaa'"
  },
  {
    cover_media: { cropped_image_version: [Object] },
    id: 'highlight:17858299709542615',
    title: 'Rhyme ✍'
  }
]

*/