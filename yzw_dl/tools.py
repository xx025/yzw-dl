import csv
import json
import os

def parse_config(config_values: dict):
    # 解析参数
    # 将参数解析为下载任务列表

    zsdw_list = []

    params = {
        'ssdm': config_values['ssdm'],
        'dwmc': config_values['dwmc'],
        'mldm': config_values['mldm'],
        'mlmc': '',
        'yjxkdm': config_values['yjxkdm'],
        'zymc': config_values['zymc'],
        'xxfs': config_values['xxfs'],
    }

    if not config_values.get('ssdm'):
        # 没指定省市代码，检查是否指定了A区或B区
        if config_values.get('abloc'):
            # 指定了A区或B区，下载对应区域
            # 排除掉不符合的省市代码
            from yzw_dl.data import sheng_fen_di_qu
            abloc = config_values['abloc'].lower()  # 获取abloc的小写
            ssdms = [i['dm'] for i in sheng_fen_di_qu if i['ab'] == abloc]
            for ssdm in ssdms:
                params['ssdm'] = ssdm
                zsdw_list.append(params.copy())
        else:
            # 没指定A区或B区，下载所有省市代码
            from yzw_dl.data import sheng_fen_di_qu
            for i in sheng_fen_di_qu:
                params['ssdm'] = i['dm']
                zsdw_list.append(params.copy())
    else:
        # 指定了省市代码，下载指定省市代码的
        zsdw_list.append(params)

    return zsdw_list


def output_jsonfile(data: dict, file_name: str):
    # 输出到 json 文件
    # data: list, json 数据
    # json_file: str, json 文件名
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def json_data_to_list_data(json_data):
    csv_data = []
    data = json_data

    for csh_name, sch_val in data.items():
        ch1 = sch_val.copy()
        ch1.pop('招生专业')
        ch1.pop('dl_params')
        for zszy_id, zszy_val in sch_val['招生专业'].items():
            ch2 = ch1.copy()
            ch2.update(zszy_val)
            ch2.pop('考试范围')
            for kskm in zszy_val['考试范围']:
                ch4 = ch2.copy()
                ch4.update(kskm)
                csv_data.append(ch4)
    return csv_data


def json_file_to_list_data(json_file: str):
    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    csv_data = json_data_to_list_data(json_data)
    return csv_data


def csv_data_output(csv_data: list, csv_path: str, csv_title: list = None):
    # 将数据写入 csv 文件

    def deduplicate_list_of_dicts(input_list):
        # 列表去重
        unique_set = set(tuple(sorted(d.items())) for d in input_list)
        deduplicated_list = [dict(item) for item in unique_set]
        return deduplicated_list

    csv_data = deduplicate_list_of_dicts(csv_data)

    if not csv_title:
        # 如果没有指定 title，则使用默认值
        csv_title = ["id", "招生单位", "所在地", "院系所", "专业", '学习方式', "研究方向", "拟招人数", "政治",
                     "外语", "业务课一", "业务课二", "考试方式", "指导老师", '备注']
    # 获取 csv_path 父路径

    csv_dir = os.path.dirname(csv_path)
    if not os.path.exists(csv_dir):
        # 如果目录不存在，则创建目录
        os.makedirs(csv_dir)
    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, csv_title)
        writer.writeheader()
        for row in csv_data:
            writer.writerow({i: row.get(i) for i in csv_title})


def json_file_scv_output(json_file: str, csv_path: str, csv_title: list = None):
    # 将 json 文件转换为 csv 文件
    csv_data = json_file_to_list_data(json_file)
    csv_data_output(csv_data, csv_path, csv_title)


def output_csvfile(data: dict, file_name: str, title: list = None):
    """
    输出到 csv 文件
    会从 data 中提取 title 中的字段
    """
    csv_data = json_data_to_list_data(data)
    csv_data_output(csv_data, file_name, title)
