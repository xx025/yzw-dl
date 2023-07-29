import argparse
import importlib.util

from tqdm import tqdm

from yzw_dl import dl_zsyx, dl_yxzy, dl_ksfw
from yzw_dl.tools import parse_config, output_jsonfile, output_csvfile


# 命令行参数解析
def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mldm', help='门类代码')
    parser.add_argument('--yjxkdm', help='一级学科代码')
    parser.add_argument('--xxfs', help='学习方式')
    parser.add_argument('--ssdm', help='省市代码')
    parser.add_argument('--dwmc', help='单位名称')
    parser.add_argument('--zymc', help='专业名称')
    parser.add_argument('--abloc', help='A区或B区')
    parser.add_argument('--output_jsonfile', help='是否输出到 json 文件', action='store_true')
    parser.add_argument('--json_file', help='json 文件名')
    parser.add_argument('--output_csvfile', help='是否输出到 csv 文件', action='store_true')
    parser.add_argument('--csv_file', help='csv 文件名')
    parser.add_argument('--csv_title', help='csv 标题')

    # 更多的参数可在 config.py 中定义
    return parser.parse_args()


# 主程序
def main():
    # 解析命令行参数
    args = parse_command_line_args()

    # 加载配置文件
    spec = importlib.util.spec_from_file_location('config', 'config.py')
    config_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config_module)

    # 使用配置文件中的默认值作为基础
    config_values = {}

    # 获取配置文件中定义的变量和对应的值
    for var_name in dir(config_module):
        if not var_name.startswith('__'):
            config_values[var_name] = getattr(config_module, var_name)

    # 使用命令行参数覆盖默认值
    for key, value in args.__dict__.items():
        if value is not None:
            config_values[key] = value

    print('Config Values:', config_values)

    param_list = parse_config(config_values)  # 解析后的参数列表

    Dl_Data = {}
    for param in tqdm(param_list, desc='下载院校信息', unit='item'):
        for sch in dl_zsyx(**param):
            Dl_Data[sch.招生单位] = sch.dict()

    for key, value in tqdm(Dl_Data.items(), desc='下载院校招生专业信息', unit='item'):
        param = Dl_Data[key]['dl_params']
        Dl_Data[key]['招生专业'] = {zs.id: zs.dict() for zs in dl_yxzy(**param)}

    for key, value in tqdm(Dl_Data.items(), desc='下载院校专业考试范围', unit='item'):
        for zyid in Dl_Data[key]['招生专业'].keys():
            my_dl_ksfw = dl_ksfw(zyid)
            zsml = my_dl_ksfw['zsml'].dict()  # 在详情页面会有一些更详细的信息
            ksfw = [ks_.dict() for ks_ in my_dl_ksfw['ksfw']]  # 考试科目范围
            dict1 = Dl_Data[key]['招生专业'][zyid]
            dict1.update(zsml)  # 更新招生专业信息
            dict1['考试范围'] = ksfw  # 添加考试科目范围
            Dl_Data[key]['招生专业'][zyid] = dict1  # 更新招生专业信息

    if config_values['output_jsonfile']:
        # json 格式保存下载的信息
        print('保存到文件：', config_values['json_file'])
        output_jsonfile(data=Dl_Data, file_name=config_values['json_file'])

    if config_values['output_csvfile']:
        # csv 格式保存下载的信息
        print('保存到文件：', config_values['csv_file'])
        output_csvfile(data=Dl_Data, file_name=config_values['csv_file'], title=config_values['csv_title'])

    # csv 格式保存下载的信息


if __name__ == '__main__':
    main()
