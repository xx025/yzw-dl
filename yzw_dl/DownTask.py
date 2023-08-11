import threading
import time

from tqdm import tqdm

from yzw_dl import dl_zsyx, dl_yxzy, dl_ksfw
from yzw_dl.tools import output_jsonfile, output_csvfile


class DownTask(threading.Thread):

    def __init__(self, param_list, save_json_file=None, save_csv_file=None):
        """
        :param param_list: 参数列表
        :param save_json_file: [是否保存到 json 文件, json 文件名]
        :param save_csv_file:  [是否保存到 csv 文件, csv 文件名, csv 标题]
        """

        super().__init__()
        if save_json_file is None:
            save_json_file = [False, 'dl_data.json']
        if save_csv_file is None:
            save_csv_file = [True, 'dl_data.csv', None]
        self.param_list = param_list
        self.save_json_file = save_json_file
        self.save_csv_file = save_csv_file
        self.save_csv_title = save_csv_file[2]

        self.dl_data = {}  # 下载的数据

        self.dl_progress = {
            '院校信息': 0,
            '专业信息': 0,
            '考试信息': 0,
            'dl_finish': False,
        }
        self._stop_event = threading.Event()
        self._pause_event = threading.Event()

    def get_dl_progress(self):
        # 获取下载进度
        return {
            '院校信息': int(self.dl_progress['院校信息'] / len(self.param_list) * 100),
            '专业信息': int(self.dl_progress['专业信息'] / len(self.dl_data) * 100),
            '考试信息': int(self.dl_progress['考试信息'] / len(self.dl_data) * 100),
            'dl_finish': self.dl_progress['dl_finish'],
        }

    def _update_dl_progress(self, key):
        # 更新下载进度
        self.dl_progress[key] = self.dl_progress[key] + 1

    def stop(self):
        # 停止下载
        self._stop_event.set()

    def run(self):
        """
        开始下载
        """

        param_list = self.param_list
        Dl_Data = self.dl_data

        for param in tqdm(param_list, desc='下载院校信息', unit='item'):
            for sch in dl_zsyx(**param):
                Dl_Data[sch.招生单位] = sch.dict()
            self._update_dl_progress('院校信息')

        for key, value in tqdm(Dl_Data.items(), desc='下载院校招生专业信息', unit='item'):
            param = Dl_Data[key]['dl_params']
            Dl_Data[key]['招生专业'] = {zs.id: zs.dict() for zs in dl_yxzy(**param)}
            self._update_dl_progress('专业信息')

        for key, value in tqdm(Dl_Data.items(), desc='下载院校专业考试范围', unit='item'):
            for zyid in Dl_Data[key]['招生专业'].keys():
                my_dl_ksfw = dl_ksfw(zyid)
                zsml = my_dl_ksfw['zsml'].dict()  # 在详情页面会有一些更详细的信息
                ksfw = [ks_.dict() for ks_ in my_dl_ksfw['ksfw']]  # 考试科目范围
                dict1 = Dl_Data[key]['招生专业'][zyid]
                dict1.update(zsml)  # 更新招生专业信息
                dict1['考试范围'] = ksfw  # 添加考试科目范围
                Dl_Data[key]['招生专业'][zyid] = dict1  # 更新招生专业信息
            self._update_dl_progress('考试信息')

        self.dl_progress['dl_finish'] = True

        if self.save_json_file[0]:
            # json 格式保存下载的信息
            print('保存到文件：', self.save_json_file[1])
            output_jsonfile(data=Dl_Data, file_name=self.save_json_file[1])

        if self.save_csv_file[0]:
            # csv 格式保存下载的信息
            print('保存到文件：', self.save_csv_file[1])
            output_csvfile(data=Dl_Data, file_name=self.save_csv_file[1], title=self.save_csv_title)

        # 进入循环，等待停止信号
        while not self._stop_event.is_set():
            print('下载进度：', self.get_dl_progress())
            time.sleep(1)
