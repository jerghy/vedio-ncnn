import os
import subprocess

# 定义可执行文件的路径
executable_path = 'realesrgan/realesrgan-ncnn-vulkan.exe'

# 定义输入文件列表和输出文件路径
input_files = [
    'folder/frame_0001.png',
    'folder/frame_0002.png',
    'folder/frame_0003.png'
]
output_files = [
    'output/0001.png',
    'output/0002.png',
    'output/0003.png'
]

# 确保输出文件夹存在
os.makedirs(os.path.dirname(output_files[0]), exist_ok=True)

# 依次处理每张图片
for input_path, output_path in zip(input_files, output_files):
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
