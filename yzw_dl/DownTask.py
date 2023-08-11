import threading
import time

from yzw_dl import dl_zsyx, dl_yxzy, dl_ksfw
from yzw_dl.tools import output_jsonfile, output_csvfile


class DownTask(threading.Thread):

    def __init__(self, param_list, save_json_file=None, save_csv_file=None):
        """
        :param param_list: 参数列表
        :param save_json_file: [是否保存到 json 文件, json 文件名]
        :param save_csv_file:  [是否保存到 csv 文件, csv 文件名, csv 标题]

        下载完成后下载线程不会自动结束，需要手动调用 stop() 方法
        """

        super().__init__()
        if save_json_file is None:
            save_json_file = [True, 'dl_data.json']
        if save_csv_file is None:
            save_csv_file = [True, 'dl_data.csv', None]
        self.param_list = param_list
        self.save_json_file = save_json_file
        self.save_csv_file = save_csv_file

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

        re_dic = {
            "progress": {
                '院校信息': self.dl_progress['院校信息'] / len(self.param_list),
                '专业信息': self.dl_progress['专业信息'] / len(self.dl_data) if len(self.dl_data) else 0,
                '考试信息': self.dl_progress['考试信息'] / len(self.dl_data) if len(self.dl_data) else 0,
            },
            'finished': self.dl_progress['dl_finish'],
        }

        for _ in re_dic.get("progress").keys():
            re_dic['progress'][_] *= 100
        return re_dic

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

        _param_list = self.param_list
        _dl_data = self.dl_data

        for param in _param_list:
            for sch in dl_zsyx(**param):
                _dl_data[sch.招生单位] = sch.dict()
            self._update_dl_progress('院校信息')

        for key, value in _dl_data.items():
            param = _dl_data[key]['dl_params']
            _dl_data[key]['招生专业'] = {zs.id: zs.dict() for zs in dl_yxzy(**param)}
            self._update_dl_progress('专业信息')

        for key, value in _dl_data.items():
            for zyid in _dl_data[key]['招生专业'].keys():
                my_dl_ksfw = dl_ksfw(zyid)
                zsml = my_dl_ksfw['zsml'].dict()  # 在详情页面会有一些更详细的信息
                ksfw = [ks_.dict() for ks_ in my_dl_ksfw['ksfw']]  # 考试科目范围
                dict1 = _dl_data[key]['招生专业'][zyid]
                dict1.update(zsml)  # 更新招生专业信息
                dict1['考试范围'] = ksfw  # 添加考试科目范围
                _dl_data[key]['招生专业'][zyid] = dict1  # 更新招生专业信息
            self._update_dl_progress('考试信息')

        self.dl_progress['dl_finish'] = True

        if self.save_json_file[0]:
            # json 格式保存下载的信息
            print('保存到文件：', self.save_json_file[1])
            output_jsonfile(data=_dl_data, file_name=self.save_json_file[1])

        if self.save_csv_file[0]:
            # csv 格式保存下载的信息
            print('保存到文件：', self.save_csv_file[1])
            output_csvfile(data=_dl_data, file_name=self.save_csv_file[1], title=self.save_csv_file[2])

        # 进入循环，等待停止信号
        while not self._stop_event.is_set():
            time.sleep(1)
