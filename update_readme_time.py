import os
from datetime import datetime


def update_readme_time(note_folder_path):

    # 获取当前日期
    now = datetime.now().strftime('%Y-%m-%d')

    # 拼接文件路径
    note_file_path = os.path.join(note_folder_path, 'README.md')

    # 读取文件内容
    with open(note_file_path, 'r', encoding='utf-8') as f:
        content = f.readlines()

    # 找到需要修改的行数
    target_line = None
    for i in range(len(content)):
        if '## 5、最后更新时间' in content[i]:
            target_line = i + 2  # 下下行的行数
            break

    # 修改目标行内容
    if target_line is not None:
        content[target_line] = now + '\n'

        # 写入文件
        with open(note_file_path, 'w', encoding='utf-8') as f:
            f.writelines(content)

        print('[INFO]README.md日期更新成功！')
    else:
        print('[ERROR]README.md日期更新失败，未找到需要修改的行！')