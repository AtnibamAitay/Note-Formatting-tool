import os
from datetime import datetime


def create_readme(path):
    # 指定要创建README.md的路径
    path = path + r'\README.md'

    # 检查README.md文件是否存在
    if os.path.exists(path):
        print('[WARNING]README.md已经存在！')
    else:
        # 获取当前时间，用于更新时间
        now = datetime.now().strftime('%Y-%m-%d')

        # 设置README.md的内容
        content = '''# README
    
## 1、作者

AtnibamAitay

## 2、网课

无

## 3、官网及文档

无

## 4、参考资料

无

## 5、最后更新时间

{}

## 6、备注

无

## 7、跳过的课

无
    '''.format(now)

        # 创建README.md文件并写入内容
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

        print('[INFO]README.md文件创建成功！')