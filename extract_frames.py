from glob import glob
import cv2
import os

FRAME_INTERVAL = 30
IN_DATA_DIR = r"./videos"
OUT_DATA_DIR = fr"./ava/frame_{int(30/FRAME_INTERVAL)}_2"
TEXT_DIR = fr"./ava/frame_{int(30/FRAME_INTERVAL)}/README.txt"


video_paths = glob(IN_DATA_DIR+r"/*/*.mp4")

for i, video_path in enumerate(video_paths):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 读取第一帧获取帧数（可能不准确，但对于抽帧来说通常足够）
    ret, frame = cap.read()
    if not ret:
        print("无法打开或找到视频文件")
        exit()

    # 获取视频的总帧数（可选，但在这里我们不需要它进行抽帧）
    # total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 计数器用于设置输出文件名
    count = 0
    video_name = f"{i:06d}"

    # out_video_path = os.path.join(OUT_DATA_DIR,video_name)
    out_video_path = os.path.join(OUT_DATA_DIR)
    if not os.path.exists(out_video_path):
        os.makedirs(out_video_path)

    video_path_write = video_path.split('样本')[-1]
    with open(TEXT_DIR, 'a') as f:
        f.write(f"..{video_path_write} -------- {video_name} \n")

    # 循环读取视频帧
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # 每隔FRAME_INTERVAL帧保存一帧
        if count % FRAME_INTERVAL == 0:
            # 构造输出文件名，使用6位数的帧号
            filename = os.path.join(out_video_path, f"{video_name}_{count//FRAME_INTERVAL:06d}.jpg")
            # 保存帧到文件
            # cv2.imwrite(filename, frame)  # 路径包含中文这个不起作用
            cv2.imencode('.jpg', frame)[1].tofile(filename)

        count += 1

    # 释放资源并关闭视频文件
    cap.release()
    cv2.destroyAllWindows()
