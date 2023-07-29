from pydantic import BaseModel


class zsmlResult(BaseModel):
    id: str
    政治: str = ''
    外语: str = ''
    业务课一: str = ''
    业务课二: str = ''


class zsmlZsyx(BaseModel):
    招生单位: str
    所在地: str
    研究生院: str
    自划线院校: str
    博士点: str


class dlParams(BaseModel):
    ssdm = ''
    dwmc = ''
    mldm = ''
    mlmc = ''
    yjxkdm = ''
    xxfs = ''
    zymc = ''


class zsmlZsyxQuery(zsmlZsyx):
    dl_params: dlParams


class zsmlYxzy(BaseModel):
    id: str
    考试方式: str
    院系所: str
    专业: str
    研究方向: str
    学习方式: str
    指导教师: str
    拟招生人数: str
    考试范围: str
    备注: str


class zsmlCondition(BaseModel):
    id: str
    招生单位: str
    考试方式: str
    院系所: str
    专业: str
    学习方式: str
    研究方向: str
    指导老师: str = ''
    拟招人数: str
    备注: str = ''
