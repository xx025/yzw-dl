import json


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


def output_csvfile(data: dict, file_name: str, title: list):
    """
    输出到 csv 文件
    会从 data 中提取 title 中的字段
    """
    csv_data = []

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

    # 将数据写入 csv 文件
    import csv
    with open(file_name, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, title)
        writer.writeheader()
        for row in csv_data:
            writer.writerow({i: row.get(i) for i in title})
