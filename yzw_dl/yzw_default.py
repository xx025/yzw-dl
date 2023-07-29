headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Length": "51",
    "Content-Type": "application/x-www-form-urlencoded",
    "DNT": "1",
    "Host": "yz.chsi.com.cn",
    "Origin": "https://yz.chsi.com.cn",
    "Referer": "https://yz.chsi.com.cn/zsml/queryAction.do",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
}


def table_next_page(text_soup, css_selector):
    # 如果下一页按钮存在，则返回 True，否则返回 False
    # unable 不出现在任何一个类名中，则存在下一页
    class_names = [i.get('class') for i in text_soup.select(css_selector)[1:]]
    next_page = all('unable' not in class_name for class_name in class_names)

    return next_page


def table_dl(one_page_dl, **kwargs):
    result = []  # 保存结果
    pageno = 1  # 页码信息
    while True:
        kwargs['pageno'] = pageno
        one_page_result, text_soup = one_page_dl(**kwargs)
        result.extend(one_page_result)
        if table_next_page(text_soup, '.zsml-page-box .lip'):
            # 存在下一页,页码参数加一
            pageno += 1
        else:
            return result
