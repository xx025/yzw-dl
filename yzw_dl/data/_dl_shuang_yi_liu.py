from urllib.parse import urlencode

import requests_enhance

from yzw_dl.utils import remove_whitespace
from yzw_dl.yzw_default import table_next_page


def dl_shuang_yi_liu_sch():
    start = 0
    scls = []

    while True:
        url = f"https://yz.chsi.com.cn/sch/search.do?{urlencode({'ylgx': 1, 'start': start})}"

        text_soup = requests_enhance.req_bs4soup_by_get(url=url)

        for i in text_soup.select('.sch-item .sch-title .name'):
            scls.append(remove_whitespace(i.text))

        if not table_next_page(text_soup, css_selector='.ch-page-wrapper .lip'):
            break
        else:
            start += 20

    return scls
