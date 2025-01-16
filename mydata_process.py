# from glob import glob
# import cv2
# import os
#
# FRAME_INTERVAL = 1
# IN_DATA_DIR = r"D:\咸鱼开店\客户信息\杨洋正式拍摄视频样本"
# OUT_DATA_DIR = fr"D:\咸鱼开店\客户信息\frame_{FRAME_INTERVAL}"
# TEXT_DIR = fr"D:\咸鱼开店\客户信息\frame_{FRAME_INTERVAL}\README.txt"
#
#
# video_paths = glob(IN_DATA_DIR+r"\*\*\*.mp4")
#
# for i, video_path in enumerate(video_paths):
#     # 打开视频文件
#     cap = cv2.VideoCapture(video_path)
#
#     # 读取第一帧获取帧数（可能不准确，但对于抽帧来说通常足够）
#     ret, frame = cap.read()
#     if not ret:
#         print("无法打开或找到视频文件")
#         exit()
#
#     # 获取视频的总帧数（可选，但在这里我们不需要它进行抽帧）
#     # total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#
#     # 计数器用于设置输出文件名
#     count = 0
#     video_name = f"{i:06d}"
#
#     out_video_path = OUT_DATA_DIR
#     if not os.path.exists(out_video_path):
#         os.makedirs(out_video_path)
#
#     video_path_write = video_path.split('样本')[-1]
#     with open(TEXT_DIR, 'a') as f:
#         f.write(f"..{video_path_write} -------- {video_name} \n")
#
#     # 循环读取视频帧
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         # 每隔FRAME_INTERVAL帧保存一帧
#         if count % FRAME_INTERVAL == 0:
#             # 构造输出文件名，使用6位数的帧号
#             filename = out_video_path + f"\\{video_name}_{count//FRAME_INTERVAL:06d}.jpg"
#             # 保存帧到文件
#             # cv2.imwrite(filename, frame)  # 路径包含中文这个不起作用
#             cv2.imencode('.jpg', frame)[1].tofile(filename)
#
#         count += 1
#
#     # 释放资源并关闭视频文件
#     cap.release()
#     cv2.destroyAllWindows()
import csv
import os
from glob import glob

import pandas as pd
from sklearn.model_selection import train_test_split

def write_csv(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # writer.writerow(['video_path', 'label'])
        writer.writerows(data)

# 文件夹路径
folders = {'low': 0, 'mid':1, 'high':2}  # 请替换为你的文件夹名称
base_path = r"./videos"  # 请替换为你的基本路径

data = []

# 遍历每个文件夹
for folder, label in folders.items():
    folder_path = os.path.join(base_path, folder)
    print(folder_path)

    # 遍历文件夹中的所有视频文件
    for filename in glob(folder_path+r"/*.mp4"):
        if filename.endswith(('.mp4', '.avi', '.mov')):  # 根据需要添加更多的视频格式
            video_path = os.path.relpath(filename)
            data.append([video_path+" {}".format(label)])

# 创建DataFrame
# df = pd.DataFrame(data, columns=['video_path', 'label'])

# 按照比例分割数据集
train_df, temp_df = train_test_split(data, train_size=0.8, random_state=42)
val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)

# 保存为CSV文件
write_csv('train.csv', train_df)
write_csv('val.csv', val_df)
write_csv('test.csv', test_df)

print("CSV文件生成完毕：train.csv, val.csv, test.csv")





# 保存为CSV文件



# python tools/run_net.py --cfg configs/Kinetics/C2D_8x8_R50.yaml DATA.PATH_TO_DATA_DIR videos  NUM_GPUS 1 TRAIN.BATCH_SIZE 16
# import os
# import csv
# import random
#
# # 文件夹路径
# folders = ['folder1', 'folder2', 'folder3']  # 请替换为你的文件夹名称
# base_path = 'path/to/your/folders'  # 请替换为你的基本路径
#
# data = []
#
# # 遍历每个文件夹
# for folder in folders:
#     folder_path = os.path.join(base_path, folder)
#
#     # 遍历文件夹中的所有视频文件
#     for filename in os.listdir(folder_path):
#         if filename.endswith(('.mp4', '.avi', '.mov')):  # 根据需要添加更多的视频格式
#             video_path = os.path.join(folder, filename)
#             data.append([video_path, folder])
#
# # 按照比例分割数据集
# random.seed(42)
# random.shuffle(data)
# total_len = len(data)
# train_len = int(0.7 * total_len)
# val_len = int(0.15 * total_len)
#
# train_data = data[:train_len]
# val_data = data[train_len:train_len + val_len]
# test_data = data[train_len + val_len:]
#
#
# # 写入CSV文件的函数
# def write_csv(filename, data):
#     with open(filename, mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['video_path', 'label'])
#         writer.writerows(data)
#
#
# # 保存为CSV文件
# write_csv('train.csv', train_data)
# write_csv('val.csv', val_data)
# write_csv('test.csv', test_data)
#
# print("CSV文件生成完毕：train.csv, val.csv, test.csv")
