import os
import re


def generate_sidebar(note_folder_path, docsify_project_path, docsify_project_note_relative_path):
    docsify_project_note_absolute_path = docsify_project_path + docsify_project_note_relative_path

    # 判断是否已存在 _sidebar.md 文件
    if os.path.exists(os.path.join(docsify_project_note_absolute_path, "_sidebar.md")):
        print("_sidebar.md 已经存在")
        return
    # 获取文件夹中所有文件名
    file_names = [file.name for file in os.scandir(note_folder_path) if file.is_file() and file.name.endswith('.md')]
    # 按照章节顺序进行排序
    file_names = sorted(file_names,
                        key=lambda x: int(re.search('(?<=第)\d+(?=章)', x).group(0)) if x.startswith("第") else float(
                            'inf'))
    # 将 README.md 文件放到第一位
    if 'README.md' in file_names:
        file_names.remove('README.md')
        file_names.insert(0, 'README.md')
    # 构造文档内容
    content = ""
    for file in file_names:
        file_name = file.replace(".md", "")
        content += f"* [{file_name}](" + docsify_project_note_relative_path + f"{file})\n"
    # 在指定路径下生成 _sidebar.md 文档
    with open(os.path.join(docsify_project_note_absolute_path, "_sidebar.md"), "w", encoding="UTF-8") as f:
        f.write(content)
