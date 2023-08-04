"""

step1:
招生院校目录下载，当指定某个专业时会筛选出招生院校,获取单个院校筛选出的专业信息
"""

from urllib.parse import urlencode

from requests_enhance import req_bs4soup_by_post

from yzw_dl.utils import parse_query_params
from .models import zsmlZsyxQuery, dlParams
from .yzw_default import table_dl, headers


def _dl_zsyx_one(ssdm='', dwmc='', mldm='', mlmc='', yjxkdm='', zymc='', xxfs='', pageno=1):
    """
    招生院校信息，需要翻页操作， 在一个页面下载招生院校
    """

    data = {'ssdm': ssdm, 'dwmc': dwmc, 'mldm': mldm, 'mlmc': mlmc, 'yjxkdm': yjxkdm, 'zymc': zymc, 'xxfs': xxfs,
            'pageno': pageno
            }

    # 如果pageno 为 1，则删除 pageno 参数
    if pageno == 1:
        data.pop('pageno')

    base_url = 'https://yz.chsi.com.cn/zsml/queryAction.do'
    # 将 data 参数转换为 URL 查询字符串格式 并 拼接 URL 和查询字符串
    url = f'{base_url}?{urlencode(data)}'
    text_soup = req_bs4soup_by_post(url=url, data=data, headers=headers)

    # 从页面中提取招生院校信息

    yxxx = []
    for i in text_soup.select('.zsml-list-box table tbody tr'):
        tds = i.select('td')

        if len(tds) == 0:
            break
        elif len(tds) == 1 and tds[0].text.index('很抱歉，没有找到您要搜索的数据！') > -1:
            break

        yxxx.append(zsmlZsyxQuery(
            招生单位=tds[0].select_one('form a').text,
            所在地=tds[1].text,
            研究生院=tds[2].text == '\ue664',
            自划线院校=tds[3].text == '\ue664',
            博士点=tds[4].text == '\ue664',
            dl_params=dlParams(**parse_query_params(tds[0].select_one('form a').get('href')))
        ))

    return yxxx, text_soup


def dl_zsyx(**kwargs) -> [zsmlZsyxQuery]:
    """
    下载招生单位信息

    在这个https://yz.chsi.com.cn/zsml/queryAction.do 页面，允许选择一些参数来获取院校信息

    这些参数分别包括
    ssdm:  省市代码
    dwmc: 单位名称，如北京大学
    mldm: 门类代码，如，zyxw 表示专业学位
    mlmc: 门类名称，但是好像这个参数没有使用
    yjxkdm: 一级学科代码，如0101表示哲学
    zymc:专业名称，如 国学
    xxfs: 学习方式

    :return:
    """

    return table_dl(_dl_zsyx_one, **kwargs)
