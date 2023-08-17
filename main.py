import argparse
import importlib.util
from time import sleep

from yzw_dl.DownTask import DownTask
from yzw_dl.tools import parse_config


# 命令行参数解析
def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mldm', help='门类代码', default='zyxw')
    parser.add_argument('--yjxkdm', help='一级学科代码', default='0251')
    parser.add_argument('--xxfs', help='学习方式')
    parser.add_argument('--ssdm', help='省市代码')
    parser.add_argument('--dwmc', help='单位名称')
    parser.add_argument('--zymc', help='专业名称')
    parser.add_argument('--abloc', help='A区或B区')
    # parser.add_argument('--yxjh', help='院校计划，in [211,981,11,100]，211、985、双一流,普通院校')
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

    dl_task = DownTask(param_list=param_list)
    dl_task.start()
    while True:
        sleep(1)
        dl_progress = dl_task.get_dl_progress()
        if dl_progress['finished']:
            print('下载完成', dl_progress['progress'])
            dl_task.stop()
            break
        else:
            print('下载进度', dl_progress['progress'])


if __name__ == '__main__':
    main()
