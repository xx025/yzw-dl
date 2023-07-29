"""
step3:

考试范围下载，下载一个院校指定某个招生专业的考试范围

"""
from requests_enhance import req_bs4soup_by_get
from yzw_dl.utils import remove_whitespace
from .models import zsmlCondition, zsmlResult


def dl_ksfw(id: str):
    """
    考试范围下载

    url如 https://yz.chsi.com.cn/zsml/kskm.jsp?id=1000221115025200001
    上面链接的id 则为 1000221115025200001

    example:
    id=1000321080135100011


    return
    {'id': '1000321080135100011',
            'zsml': zsmlCondition(招生单位='(10003)清华大学',
                                  考试方式='统考', 院系所='(080)美术学院',
                                  专业='(135100)(专业学位)艺术',
                                  学习方式='全日制',
                                  研究方向='(01)美术-绘画',
                                  指导老师='不区分导师',
                                  拟招人数='研究方向：3(不含推免)',
                                  备注='招生人数后续可能调整，请关注清华研招网（http://yz.tsinghua.edu.cn）公布的招生专业目录'),
            'ksfw': [zsmlResult(政治='(101)思想政治理论', 外语='(202)俄语', 业务课一='(621)艺术理论基础',
                                业务课二='(519)造型基础（专业学位）'),
                     zsmlResult(政治='(101)思想政治理论', 外语='(203)日语', 业务课一='(621)艺术理论基础',
                                业务课二='(519)造型基础（专业学位）'),
                     zsmlResult(政治='(101)思想政治理论', 外语='(204)英语（二）', 业务课一='(621)艺术理论基础',
                                业务课二='(519)造型基础（专业学位）'),
                     zsmlResult(政治='(101)思想政治理论', 外语='(241)德语', 业务课一='(621)艺术理论基础',
                                业务课二='(519)造型基础（专业学位）'),
                     zsmlResult(政治='(101)思想政治理论', 外语='(242)法语', 业务课一='(621)艺术理论基础',
                                业务课二='(519)造型基础（专业学位）')]
    }


    """

    url = 'https://yz.chsi.com.cn/zsml/kskm.jsp?id=' + id

    # 发送get请求并返回text
    text_soup = req_bs4soup_by_get(url)

    # 从text中提取院校专业等信息
    texts = [i.text for i in text_soup.select('.zsml-condition tbody tr .zsml-summary')]
    zsml_condition = zsmlCondition(
        id=id,
        招生单位=texts[0],
        考试方式=texts[1],
        院系所=texts[2],
        专业=texts[3],
        学习方式=texts[4],
        研究方向=texts[5],
        指导老师=texts[6],
        拟招人数=texts[7],
        备注=text_soup.select('.zsml-condition tbody tr .zsml-bz')[1].text
    )
    # 从text中提取考试具体科目等信息
    kskm = []
    for i in text_soup.select('.zsml-result .zsml-res-items'):
        kskms = [remove_whitespace(j.contents[0]) for j in i.select('td')]
        kskm.append(zsmlResult(id=id, 政治=kskms[0], 外语=kskms[1], 业务课一=kskms[2], 业务课二=kskms[3]))

    return {'id': id, 'zsml': zsml_condition, 'ksfw': kskm}
