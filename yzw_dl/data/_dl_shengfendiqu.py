def dl_sheng_fen_di_qu():
    import json

    from requests_enhance import req_json_by_post
    data = req_json_by_post(url='https://yz.chsi.com.cn/zsml/pages/getSs.jsp')

    loc_A = ['北京', '天津', '河北', '山西', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西',
             '山东', '河南', '湖北', '湖南', '广东', '重庆', '四川', '陕西']
    loc_B = ['内蒙古', '广西', '海南', '贵州', '云南', '西藏', '甘肃', '青海', '宁夏', '新疆']

    for i in data:
        for j in loc_A:
            if j in i['mc']:
                i['ab'] = 'a'
                break
        else:
            for j in loc_B:
                if j in i['mc']:
                    i['ab'] = 'b'
                    break
    with open('shengfendiqu.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return data
