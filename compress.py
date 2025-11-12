import os
import subprocess

# 设置你的视频目录
input_dir = r"D:\Code\heyuanYao-pku.github.io\src\assets\lumine"
output_dir = os.path.join(input_dir, "compressed")  # 输出目录

os.makedirs(output_dir, exist_ok=True)

def compress_to_540p(input_file, output_file):
    cmd = [
        "ffmpeg", "-y",
        "-i", input_file,
        "-vf", "scale=-1:540",  # 高度设为540，宽度按比例自适应
        "-c:v", "libx264", "-preset", "fast", "-crf", "28",  # 压缩质量
        "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart",  # 网页播放优化
        output_file
    ]
    print(f"▶ 压缩: {input_file} -> {output_file}")
    subprocess.run(cmd, check=True)

for file in os.listdir(input_dir):
    if file.lower().endswith(".mp4"):
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, file)
        compress_to_540p(input_path, output_path)

print("✅ 所有 MP4 已压缩到 540p 完成！")