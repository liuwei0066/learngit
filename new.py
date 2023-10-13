import cv2
import numpy as np
import os

# 输入文件夹和输出文件夹
input_folder = 'disp'  # 指定包含图像的文件夹路径
output_folder = 'new_disp'  # 指定保存填充后图像的文件夹路径

# 目标填充尺寸
target_width = 120
target_height = 120

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取输入文件夹中的所有图像文件
image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg') or f.endswith('.png')]

for image_file in image_files:
    # 打开图像
    image_path = os.path.join(input_folder, image_file)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # 以灰度模式打开图像

    # 获取图像的当前尺寸
    current_height, current_width = image.shape

    # 计算填充后的位置
    top = (target_height - current_height) // 2
    bottom = (target_height - current_height) - top
    left = (target_width - current_width) // 2
    right = (target_width - current_width) - left

    # 使用Numpy进行填充
    padded_image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=255)  # 255 表示白色填充

    # 保存填充后的图像到输出文件夹
    output_path = os.path.join(output_folder, image_file)
    cv2.imwrite(output_path, padded_image)

print(f'已完成填充并保存到 {output_folder}')
