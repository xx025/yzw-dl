from urllib.parse import parse_qs, unquote


def remove_whitespace(string):
    return string.replace(' ', '').replace('\n', '').replace('\r', '').replace('\t', '')



def parse_query_params(url: str):
    params_dict = parse_qs(url.split('?')[1])
    params_dict = {k: unquote(v[0]) for k, v in params_dict.items()}
    return params_dict