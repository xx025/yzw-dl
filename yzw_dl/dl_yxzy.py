import re
from urllib.parse import urlencode

from requests_enhance import req_bs4soup_by_get

from .models import zsmlYxzy
from .yzw_default import table_dl, headers


def dl_yxzy_one(ssdm='', dwmc='', mldm='', mlmc='', yjxkdm='', xxfs='', zymc='', pageno=1):
    data = {
        'ssdm': ssdm,
        'dwmc': dwmc,
        'mldm': mldm,
        'mlmc': mlmc,
        'yjxkdm': yjxkdm,
        'zymc': zymc,
        'xxfs': xxfs,
        'pageno': pageno
    }

    assert dwmc != '', 'dwmc 单位名称不能为空'

    if pageno == 1:
        data.pop('pageno')

    base_url = 'https://yz.chsi.com.cn/zsml/querySchAction.do'
    url = f'{base_url}?{urlencode(data)}'  # 将参数和url拼接

    text_soup = req_bs4soup_by_get(url=url, data=data, headers=headers)

    pattern = r"cutString\('([^']*)',\d+\)"  # 使用正则表达式匹配参数值

    result = []
    for i in text_soup.select('.zsml-list-box tbody tr'):
        tds = i.select('td')
        href = tds[7].select_one('a').get('href')
        result.append(
            zsmlYxzy(
                id=href.split('=')[-1],
                考试方式=tds[0].text,
                院系所=tds[1].text,
                专业=tds[2].text,
                研究方向=tds[3].text,
                学习方式=tds[4].text,
                指导教师='',
                拟招生人数=re.findall(pattern, tds[6].select_one('script').text)[0],
                考试范围=href,
                备注=re.findall(pattern, tds[8].select_one('script').text)[0],
            )
        )

    return result, text_soup


def dl_yxzy(**kwargs) -> [zsmlYxzy]:
    """

    step2:
        下载指定院校专业目录，当指定某个专业和某个院校，获取这个院校关于这些专业的招生信息
        如页面：https://yz.chsi.com.cn/zsml/querySchAction.do?ssdm=11&dwmc=%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6&mldm=08&mlmc=&yjxkdm=0812&xxfs=1&zymc=1

    :param ssdm: 省市代码,如 11
    :param dwmc: 单位名称,必填，如北京大学
    :param mldm: 门类代码，必填.如08
    :param mlmc: 门类名称
    :param yjxkdm: 一级学科代码 如0812
    :param xxfs: 学习方式
    :param zymc: 专业名称
    :param pageno: 页码
    :return:
    """

    return table_dl(dl_yxzy_one, **kwargs)
