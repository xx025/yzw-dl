"""
这些数据，由手工整理

两个简易的脚本 _dl_shengfendiqu.py,_dl_shuang_yi_liu.py 用于获取数据

"""

chs_985 = ['北京大学', '中国人民大学', '清华大学', '北京航空航天大学', '北京理工大学', '中国农业大学', '北京师范大学',
           '中央民族大学', '南开大学', '天津大学', '大连理工大学', '东北大学', '吉林大学', '哈尔滨工业大学', '复旦大学',
           '同济大学', '上海交通大学', '华东师范大学', '南京大学', '东南大学', '浙江大学', '中国科学技术大学',
           '厦门大学', '山东大学', '中国海洋大学', '武汉大学', '华中科技大学', '湖南大学', '中南大学', '国防科技大学',
           '中山大学', '华南理工大学', '四川大学', '电子科技大学', '重庆大学', '西安交通大学', '西北工业大学',
           '西北农林科技大学', '兰州大学']

chs_211 = ['北京大学', '中国人民大学', '清华大学', '北京交通大学', '北京工业大学', '北京航空航天大学', '北京理工大学',
           '北京科技大学', '北京化工大学', '北京邮电大学', '中国农业大学', '北京林业大学', '北京中医药大学',
           '北京师范大学', '北京外国语大学', '中国传媒大学', '中央财经大学', '对外经济贸易大学', '北京体育大学',
           '中央音乐学院', '中央民族大学', '中国政法大学', '华北电力大学', '华北电力大学(保定)', '南开大学', '天津大学',
           '天津医科大学', '河北工业大学', '太原理工大学', '内蒙古大学', '辽宁大学', '大连理工大学', '东北大学',
           '大连海事大学', '吉林大学', '延边大学', '东北师范大学', '哈尔滨工业大学', '哈尔滨工程大学', '东北农业大学',
           '东北林业大学', '复旦大学', '同济大学', '上海交通大学', '华东理工大学', '东华大学', '华东师范大学',
           '上海外国语大学', '上海财经大学', '上海大学', '海军军医大学', '南京大学', '苏州大学', '东南大学',
           '南京航空航天大学', '南京理工大学', '中国矿业大学', '河海大学', '江南大学', '南京农业大学', '中国药科大学',
           '南京师范大学', '浙江大学', '安徽大学', '中国科学技术大学', '合肥工业大学', '厦门大学', '福州大学',
           '南昌大学', '山东大学', '中国海洋大学', '中国石油大学(北京)', '中国石油大学(华东)', '郑州大学', '武汉大学',
           '华中科技大学', '中国地质大学(武汉)', '中国地质大学(北京)', '武汉理工大学', '华中农业大学', '华中师范大学',
           '中南财经政法大学', '湖南大学', '中南大学', '湖南师范大学', '国防科技大学', '中山大学', '暨南大学',
           '华南理工大学', '华南师范大学', '广西大学', '海南大学', '四川大学', '西南交通大学', '电子科技大学',
           '四川农业大学', '西南财经大学', '重庆大学', '西南大学', '贵州大学', '云南大学', '西藏大学', '西北大学',
           '西安交通大学', '西北工业大学', '西安电子科技大学', '长安大学', '西北农林科技大学', '陕西师范大学',
           '空军军医大学', '兰州大学', '青海大学', '宁夏大学', '新疆大学', '石河子大学']

chs_s11 = ['北京大学', '中国人民大学', '清华大学', '北京交通大学', '北京工业大学', '北京航空航天大学',
           '北京理工大学', '北京科技大学', '北京化工大学', '北京邮电大学', '中国农业大学', '北京林业大学',
           '北京协和医学院', '北京中医药大学', '北京师范大学', '首都师范大学', '北京外国语大学', '中国传媒大学',
           '中央财经大学', '对外经济贸易大学', '外交学院', '中国人民公安大学', '北京体育大学', '中央音乐学院',
           '中国音乐学院', '中央美术学院', '中央戏剧学院', '中央民族大学', '中国政法大学', '华北电力大学',
           '中国矿业大学(北京)', '中国石油大学(北京)', '中国地质大学(北京)', '中国科学院大学', '南开大学',
           '天津大学', '天津工业大学', '天津医科大学', '天津中医药大学', '华北电力大学(保定)', '河北工业大学',
           '山西大学', '太原理工大学', '内蒙古大学', '辽宁大学', '大连理工大学', '东北大学', '大连海事大学',
           '吉林大学', '延边大学', '东北师范大学', '哈尔滨工业大学', '哈尔滨工程大学', '东北农业大学',
           '东北林业大学', '复旦大学', '同济大学', '上海交通大学', '华东理工大学', '东华大学', '上海海洋大学',
           '上海中医药大学', '华东师范大学', '上海外国语大学', '上海财经大学', '上海体育学院', '上海音乐学院',
           '上海大学', '上海科技大学', '海军军医大学', '南京大学', '苏州大学', '东南大学', '南京航空航天大学',
           '南京理工大学', '中国矿业大学', '南京邮电大学', '河海大学', '江南大学', '南京林业大学',
           '南京信息工程大学', '南京农业大学', '南京医科大学', '南京中医药大学', '中国药科大学', '南京师范大学',
           '浙江大学', '中国美术学院', '宁波大学', '安徽大学', '中国科学技术大学', '合肥工业大学', '厦门大学',
           '福州大学', '南昌大学', '山东大学', '中国海洋大学', '中国石油大学(华东)', '郑州大学', '河南大学',
           '武汉大学', '华中科技大学', '中国地质大学(武汉)', '武汉理工大学', '华中农业大学', '华中师范大学',
           '中南财经政法大学', '湘潭大学', '湖南大学', '中南大学', '湖南师范大学', '国防科技大学', '中山大学',
           '暨南大学', '华南理工大学', '华南农业大学', '广州医科大学', '广州中医药大学', '华南师范大学',
           '南方科技大学', '广西大学', '海南大学', '重庆大学', '西南大学', '四川大学', '西南交通大学',
           '电子科技大学', '西南石油大学', '成都理工大学', '四川农业大学', '成都中医药大学', '西南财经大学',
           '贵州大学', '云南大学', '西藏大学', '西北大学', '西安交通大学', '西北工业大学', '西安电子科技大学',
           '长安大学', '西北农林科技大学', '陕西师范大学', '空军军医大学', '兰州大学', '青海大学', '宁夏大学',
           '新疆大学', '石河子大学']

sheng_fen_di_qu = [{'mc': '北京市', 'dm': '11', 'ab': 'a'}, {'mc': '天津市', 'dm': '12', 'ab': 'a'},
                   {'mc': '河北省', 'dm': '13', 'ab': 'a'}, {'mc': '山西省', 'dm': '14', 'ab': 'a'},
                   {'mc': '内蒙古自治区', 'dm': '15', 'ab': 'b'}, {'mc': '辽宁省', 'dm': '21', 'ab': 'a'},
                   {'mc': '吉林省', 'dm': '22', 'ab': 'a'}, {'mc': '黑龙江省', 'dm': '23', 'ab': 'a'},
                   {'mc': '上海市', 'dm': '31', 'ab': 'a'}, {'mc': '江苏省', 'dm': '32', 'ab': 'a'},
                   {'mc': '浙江省', 'dm': '33', 'ab': 'a'}, {'mc': '安徽省', 'dm': '34', 'ab': 'a'},
                   {'mc': '福建省', 'dm': '35', 'ab': 'a'}, {'mc': '江西省', 'dm': '36', 'ab': 'a'},
                   {'mc': '山东省', 'dm': '37', 'ab': 'a'}, {'mc': '河南省', 'dm': '41', 'ab': 'a'},
                   {'mc': '湖北省', 'dm': '42', 'ab': 'a'}, {'mc': '湖南省', 'dm': '43', 'ab': 'a'},
                   {'mc': '广东省', 'dm': '44', 'ab': 'a'}, {'mc': '广西壮族自治区', 'dm': '45', 'ab': 'b'},
                   {'mc': '海南省', 'dm': '46', 'ab': 'b'}, {'mc': '重庆市', 'dm': '50', 'ab': 'a'},
                   {'mc': '四川省', 'dm': '51', 'ab': 'a'}, {'mc': '贵州省', 'dm': '52', 'ab': 'b'},
                   {'mc': '云南省', 'dm': '53', 'ab': 'b'}, {'mc': '西藏自治区', 'dm': '54', 'ab': 'b'},
                   {'mc': '陕西省', 'dm': '61', 'ab': 'a'}, {'mc': '甘肃省', 'dm': '62', 'ab': 'b'},
                   {'mc': '青海省', 'dm': '63', 'ab': 'b'}, {'mc': '宁夏回族自治区', 'dm': '64', 'ab': 'b'},
                   {'mc': '新疆维吾尔自治区', 'dm': '65', 'ab': 'b'}]
