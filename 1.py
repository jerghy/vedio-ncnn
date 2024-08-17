import os
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 定义可执行文件的路径
executable_path = 'realesrgan/realesrgan-ncnn-vulkan.exe'

# 检查文件是否存在


def isfile(path):
    if os.path.exists(path):
        print(f"文件存在：{path}")
    else:
        print(f"文件不存在：{path}")
isfile(executable_path)


# 定义输入文件列表和输出文件路径
# input_files = [
#     'folder/frame_001.png',
#     'folder/frame_0002.png',
#     'folder/frame_0003.png'
# ]
# output_files = [
#     'output/0001.png',
#     'output/0002.png',
#     'output/0003.png'
# ]

num_files = 3

# 生成 input_files 和 output_files 列表
input_files = [f'folder/frame_{i:04d}.png' for i in range(1, num_files + 1)]
output_files = [f'output/{i:04d}.png' for i in range(1, num_files + 1)]

# 确保输出文件夹存在
os.makedirs(os.path.dirname(output_files[0]), exist_ok=True)

# 依次处理每张图片
for input_path, output_path in zip(input_files, output_files):
    isfile(input_path)
    # isfile(output_path)
    # 定义命令行参数
    command = [
        executable_path,
        '-i', input_path,  # 输入文件
        '-o', output_path,  # 输出文件
        '-n', 'realesrgan-x4fast',  # 模型名称
      
    ]

    # 运行命令
    try:
        subprocess.run(command, check=True)
        print(f'处理完成：{input_path} -> {output_path}')
    except subprocess.CalledProcessError as e:
        print(f'处理失败：{input_path}')
        print(e)

print('所有图片处理完毕。')
