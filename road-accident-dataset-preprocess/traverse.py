"""
查看文件内某列有多少种标签
"""
import csv

def count_and_print_different_contents(csv_file, tag):
    # 创建一个空集合，用于存储不同的内容
    content_set = set()
    # 创建一个字典，用于存储数字类型的最小值和最大值
    number_range_dict = {}

    # 打开 CSV 文件进行读取
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # 遍历每一行数据
        for row in reader:
            # 获取当前行的 "tag" 列的值
            tag_value = row.get(tag, "")
            # 判断该值是否为空
            if tag_value != "":
                # 判断该值是否为纯数字
                if is_pure_number(tag_value):
                    # 将该值转换为数字类型
                    number = int(tag_value)
                    # 更新数字类型的最小值和最大值
                    if tag not in number_range_dict:
                        number_range_dict[tag] = [number, number]
                    else:
                        number_range_dict[tag][0] = min(number_range_dict[tag][0], number)
                        number_range_dict[tag][1] = max(number_range_dict[tag][1], number)
                else:
                    # 将该值添加到集合中
                    content_set.add(tag_value)

    # 打印出每一种内容
    print(tag)
    for content in content_set:
        print("\""+content+"\",",end="")
    # 打印数字类型的范围
    for tag, number_range in number_range_dict.items():
        print("\""+tag+"范围：["+str(number_range[0])+","+str(number_range[1])+")\",",end="")

    # 返回集合的长度，即不同的内容数量
    return len(content_set) + len(number_range_dict)

# 判断一个字符串是否为纯数字
def is_pure_number(str):
    for s in str:
        if not s.isdigit():
            return False
    return True
# 测试代码
csv_file = "../datasets/Traffic_Crashes_-_People.csv"
tag="AIRBAG_DEPLOYED"
count = count_and_print_different_contents(csv_file,tag)
print("\nnumber：", count)
