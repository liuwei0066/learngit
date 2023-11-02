import os
import shutil

# 定义两个文件夹的路径
folder1_path = 'data_2023_0823_1/20210223_1421/cam0'
folder2_path = 'new_data_2023_08_23'
output_folder_path = 'data_2023_0823_1_label/20210223_1421'  # 存放另存为文件的文件夹路径

# 创建新的文件夹用于存放文件
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# 获取folder1中的所有文件名
folder1_files = os.listdir(folder1_path)

# 遍历folder1中的文件
for file1 in folder1_files:
    # 遍历folder2中的文件
    for root, dirs, files in os.walk(folder2_path):
        for file2 in files:
            # 检查是否有相同的前缀
            if file1.startswith(os.path.splitext(file2)[0]):
                # 构建文件的完整路径
                file2_path = os.path.join(root, file2)
                output_file_path = os.path.join(output_folder_path, file2)

                # 复制文件到新的文件夹
                shutil.copy(file2_path, output_file_path)
