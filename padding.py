from PIL import Image
import os

# 输入文件夹和输出文件夹
input_folder = 'right'  # 指定包含图像的文件夹路径
output_folder = 'new_right'  # 指定保存填充后图像的文件夹路径

# 目标填充尺寸
target_width = 1242
target_height = 400

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 获取输入文件夹中的所有图像文件
image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg') or f.endswith('.png')]

for image_file in image_files:
    # 打开图像
    image_path = os.path.join(input_folder, image_file)
    image = Image.open(image_path)

    # 获取图像的当前尺寸
    current_width, current_height = image.size

    # 计算填充后的位置
    left = (target_width - current_width) // 2
    top = (target_height - current_height) // 2

    # 创建一个新的填充后图像，保持原始通道模式
    padded_image = Image.new(image.mode, (target_width, target_height))

    # 将原始图像粘贴到填充后的图像中央
    padded_image.paste(image, (left, top))

    # 保存填充后的图像到输出文件夹
    output_path = os.path.join(output_folder, image_file)
    padded_image.save(output_path)

print(f'已完成填充并保存 到 {output_folder}')

