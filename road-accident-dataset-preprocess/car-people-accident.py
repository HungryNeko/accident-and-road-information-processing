"""
读取车辆，人，事故信息，将id，坐标，等数据结合生成新csv
使用“CRASH_RECORD_ID”字段将车辆信息链接回碰撞数据。由于此数据集是车辆、行人和脚踏自行车手的组合

并加上受伤类型：INJURY_CLASSIFICATION："INCAPACITATING INJURY","NONINCAPACITATING INJURY","NO INDICATION OF INJURY","FATAL","REPORTED, NOT EVIDENT"
AIRBAG_DEPLOYED:
"""
import csv
import os
import sys

import pandas as pd
from tqdm import tqdm


def merge_crash_data(crashes_path, people_path, vehicles_path, output_csv_path):#会清空上次的输出文件！！！
    # 读取车祸数据
    crashes_df = pd.read_csv(crashes_path)
    # 提取 CRASH_RECORD_ID、经纬度和时间
    crashes_df = crashes_df[['CRASH_RECORD_ID', 'LATITUDE', 'LONGITUDE', 'CRASH_DATE']]

    # 读取参与人员和车辆数据
    people_df = pd.read_csv(people_path)
    vehicles_df = pd.read_csv(vehicles_path)

    # 统计每个 CRASH_RECORD_ID 对应的人数和车辆数
    num_people = people_df.groupby('CRASH_RECORD_ID').size()
    num_vehicles = vehicles_df.groupby('CRASH_RECORD_ID').size()

    # 初始化结果字典
    result_data = {
        'CRASH_RECORD_ID': [],
        'LATITUDE': [],
        'LONGITUDE': [],
        'CRASH_DATE': [],
        'NUM_PEOPLE': [],
        'NUM_VEHICLES': [],
        'INJURY_CLASSIFICATION': [],
        'AIRBAG_DEPLOYED': []
    }

    # 合并数据
    total_records = len(crashes_df)
    with tqdm(total=total_records, desc="Processing") as pbar:
        for index, row in crashes_df.iterrows():
            crash_record_id = row['CRASH_RECORD_ID']
            # 如果已经处理过相同的 CRASH_RECORD_ID，则跳过
            if crash_record_id in result_data['CRASH_RECORD_ID']:
                continue

            # 将信息添加到结果字典中
            result_data['CRASH_RECORD_ID'].append(crash_record_id)
            result_data['LATITUDE'].append(row['LATITUDE'])
            result_data['LONGITUDE'].append(row['LONGITUDE'])
            result_data['CRASH_DATE'].append(row['CRASH_DATE'])
            result_data['NUM_PEOPLE'].append(num_people.get(crash_record_id, 0))
            result_data['NUM_VEHICLES'].append(num_vehicles.get(crash_record_id, 0))
            result_data['INJURY_CLASSIFICATION'].append(get_data("../datasets/Traffic_Crashes_-_People.csv",crash_record_id,'INJURY_CLASSIFICATION'))
            result_data['AIRBAG_DEPLOYED'].append(get_data("../datasets/Traffic_Crashes_-_People.csv",crash_record_id,'CRASH_RECORD_ID')),
            pbar.update(1)

    # 清空之前的输出文件
    if os.path.exists(output_csv_path):
        os.remove(output_csv_path)

    # 将结果保存到 CSV 文件中
    result_df = pd.DataFrame(result_data)
    result_df.to_csv(output_csv_path, index=False)

def get_data(file_path, crash_record_id,tag):
    # 初始化列表来存储 'AIRBAG_DEPLOYED' 数据
    data = []

    # 打开 CSV 文件
    # with open(file_path, 'r') as file:
    #     # 创建一个 CSV reader
    #     reader = csv.DictReader(file)

        # 遍历 CSV 中的每一行
    for row in reader:
        # 如果 'CRASH_RECORD_ID' 与提供的 id 匹配
        if row['CRASH_RECORD_ID'] == crash_record_id:
            # 将 'AIRBAG_DEPLOYED' 数据添加到列表中
            data.append(row[tag])

    # 使用 '|' 连接 'AIRBAG_DEPLOYED' 数据并返回结果
    return '|'.join(data)

# 示例用法
if __name__ == "__main__":

        # 创建一个 CSV reader
    reader = csv.DictReader(open("../datasets/Traffic_Crashes_-_People.csv", 'r'))
    merge_crash_data("../datasets/Traffic_Crashes_-_Crashes_20240313.csv",
                     "../datasets/Traffic_Crashes_-_People.csv",
                     "../datasets/Traffic_Crashes_-_Vehicles.csv",
                     "../datasets/output1.csv")
