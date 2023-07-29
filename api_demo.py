from yzw_dl import dl_yxzy, dl_zsyx, dl_ksfw

print("====step1====")
# 获取招生院校
result1 = dl_zsyx(mldm='zyxw', yjxkdm='0251')
print(result1[0])

print("====step2====")
# 获取指定院校 对应的专业
zsyx1 = result1[0]  # 以上一步下载的第一个为例子
result2 = dl_yxzy(**zsyx1.dl_params.dict())
print(result2[0])

print("====step3====")
# 下载特定专业的考试范围
# 以第二步下载的第一个为例子
ksfw1 = result2[0]
print(dl_ksfw(id=ksfw1.id))