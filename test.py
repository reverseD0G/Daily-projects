import os
import sys
import time

file_dir: str = 'C:\\Users\\Shadow\\Desktop\\TestX\\'  
prev: int = 0  # 当前感染的个数
prev_time = time.time()  # 开始时间
ext_str: str = sys.argv[1]  # 获取输入的后缀
while True:
    file_list: list[str] = os.listdir(file_dir)  # 获取文件夹里的文件
    # 获取以勒索软件感染的文件后缀
    countx: int = len([file for file in file_list if file.endswith(ext_str)])
    current_time: float = time.time()  # 当前程序运行的时间
    exec_time: float = current_time - prev_time  # 获取程序执行花费的时间
    prev_time: float = current_time  # 将当前程序运行的时间保存为上次循环记录的时间
    if countx > prev:  # 文件夹啊中感染的程序数目发生了变化
        prev: int = countx
        print(f'modify file {countx} , execute time {exec_time}')
    time.sleep(0.1)  # 休眠0.1秒，即每次检测的间隔时间