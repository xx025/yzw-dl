# 下载可选的参数配置

# 必选参数
mldm = 'zyxw'  # 门类代码
yjxkdm = '0251'  # 一级学科代码

# 可选参数，符合研招网的参数
xxfs = ''  # 学习方式
ssdm = ''  # 省市代码
dwmc = ''  # 单位名称，如北京大学
zymc = ''  # 专业名称，如 国学

# 可选参数，会进行处理并且与上面的参数可能冲突
abloc = ''  # A区或B区，如果指定了dwmc或ssdm，则忽略该参数

# TODO: 院校计划
# yxjh = ''  # 院校计划,如果指定了dwmc，则忽略该参数


# output to json file
output_jsonfile = False  # 是否输出到 json 文件
json_file = 'dl-data.json'  # json 文件名

# output to csv file
# 输出到csv 文件本质是将 json层次化展平，最终以 招生专业 id 进行区分单个专业
# 输出到csv 可能 两行的id 相同 但区别于考试科目，这是因为部分招生专业 有多个考试科目组合
output_csvfile = True  # 是否输出到 csv 文件
csv_file = 'dl-data.csv'  # csv 文件名
# # 输出到 csv 文件的标题,可参考 dl-data.json
csv_title = [
    "id",
    "招生单位",
    "所在地",
    "院系所",
    "专业",
    '学习方式',
    "研究方向",
    "拟招人数",
    "政治",
    "外语",
    "业务课一",
    "业务课二",
    "考试方式",
    "指导老师",
    '备注'
]
