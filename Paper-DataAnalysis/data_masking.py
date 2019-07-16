# @时间 : 2019-6-26 9:59 
# @作者 : 孙会想
# @文件 : data_masking.py 
# @工具: PyCharm


sourcefilepath = "d:/DataSet/CRM/client.txt"

replace_key = '******'

# 首先读取文件
with open(sourcefilepath, 'r', encoding='utf-8') as f:
    contents = f.readlines()

# 特殊字段分割 脱敏指定列字符，如脱敏第2列
column_num = 2
for line in contents:
    temp = line.split("/")
    org_str = temp[column_num - 1]
    replace_str = org_str[0:3] + replace_key + org_str[5:]

    target_line = ""
    for i in range(len(temp)):
        if i == column_num - 1:
            target_line = target_line + "|" + replace_str
        elif i == len(temp) - 1:
            target_line = target_line + temp[i]
        else:
            target_line = target_line + temp[i] + "|"

    print(target_line)

# 定长文件 脱敏指定列字符
for line in contents:
    replace_str = line[0:3] + replace_key + line[5:]
    print(replace_str)