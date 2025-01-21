import argparse
import os
from concurrent.futures import ThreadPoolExecutor

# 支持的文件格式列表
SUPPORTED_FORMATS = ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', 'm4a']

def ensure_directory_exists(directory):
    """确保目录存在，如果不存在则创建它"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def ensure_file_exists(file_path):
    """确保文件存在，如果不存在则创建一个空文件"""
    if not os.path.isfile(file_path):
        open(file_path, 'w').close()

def rename_file(old_name, new_name, log_file_path, dry_run):
    """重命名单个文件，并处理异常"""
    if dry_run:
        print(f"dry-run: 将重命名 {old_name} 到 {new_name}")
        return

    try:
        # 尝试重命名文件
        os.rename(old_name, new_name)
        print(f"重命名: {old_name} -> {new_name}")
        # 记录成功重命名的文件
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"成功重命名: {old_name} -> {new_name}\n")
    except OSError as e:
        # 如果发生OSError异常，记录错误信息到日志文件
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"无法重命名文件 {old_name} 到 {new_name}: {e}\n")

def rename_music_files(PATH, dry_run=False):
    # 确保重命名目录和日志文件存在
    ensure_directory_exists(PATH)
    log_file_path = os.path.join(PATH, "musicRename.log")
    ensure_file_exists(log_file_path)

    # 初始化一个标志，表示是否进行了重命名
    renamed = False

    # 创建线程池
    with ThreadPoolExecutor() as executor:
        # 遍历指定目录及其子目录
        for root, _, files in os.walk(PATH):
            for file in files:
                # 检查文件格式是否在支持的格式列表中
                if any(file.lower().endswith(ext) for ext in SUPPORTED_FORMATS):
                    old_name = os.path.join(root, file)
                    name, ext = os.path.splitext(file)

                    # 查找第一个“-”的位置
                    dash_index = name.find("-")
                    if dash_index != -1:
                        # 如果找到“-”，生成新的文件名
                        new_name = name[dash_index + 2:] + ext
                    else:
                        # 如果没有找到“-”，查找第一个“_”
                        underscore_index = name.find("_")
                        if underscore_index != -1:
                            # 如果找到“_”，生成新的文件名
                            new_name = name[underscore_index + 1:] + ext
                        else:
                            # 如果既没有找到“-”也没有找到“_”，跳过该文件
                            continue

                    # 构建新的文件路径
                    new_name = os.path.join(root, new_name)
                    # 检查新文件名是否存在
                    if os.path.exists(new_name):
                        with open(log_file_path, "a", encoding="utf-8") as log_file:
                            log_file.write(f"文件名冲突，跳过: {old_name} -> {new_name}\n")
                        continue

                    # 提交线程任务
                    executor.submit(rename_file, old_name, new_name, log_file_path, dry_run)
                    renamed = True

    # 如果没有进行重命名，输出“无需重命名”
    if not renamed:
        print("无需重命名")

if __name__ == "__main__":
    # 使用argparse解析命令行参数
    parser = argparse.ArgumentParser(description="批量重命名支持的音频文件")
    parser.add_argument("PATH", help="需要重命名文件的目录", type=str)
    parser.add_argument("-d", "--dry-run", help="模拟重命名过程，不实际更改文件名", action="store_true")
    args = parser.parse_args()

    # 根据命令行参数调用函数
    rename_music_files(args.PATH, dry_run=args.dry_run)
