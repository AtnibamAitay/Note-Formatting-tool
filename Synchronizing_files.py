import os
import shutil


def synchronizing_files(note_folder_path, docsify_project_note_absolute_path):
    # 检查目标目录是否为空
    if os.path.exists(docsify_project_note_absolute_path) and os.listdir(docsify_project_note_absolute_path):
        # 如果存在，则删除目标目录及其所有内容
        shutil.rmtree(docsify_project_note_absolute_path)
        print(f"[INFO]{docsify_project_note_absolute_path} 不是空目录，已经将整个文件夹删除了")

    # 复制文件和文件夹
    shutil.copytree(note_folder_path, docsify_project_note_absolute_path)
    print("[INFO]笔记同步完成")