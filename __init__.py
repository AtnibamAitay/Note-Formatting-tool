from Synchronizing_files import synchronizing_files
from create_readme import create_readme
from markdown_img_code_modifier import markdown_img_code_modifier
from rename_note_files_name import rename_note_files_name
from sidebar_generator import generate_sidebar
from update_readme_time import update_readme_time

# note_folder_path = r"A:\始于不足见，终于不可及\学习\编程\4.前端\1.Vue"
# docsify_project_path = r"Z:\Project\Cardinal-Note-Document\docs"
# docsify_project_note_relative_path = "/document/FrontEnd/Vue/"

note_folder_path = r"A:\始于不足见，终于不可及\学习\编程\1.Java\2.Java 开发进阶\6.设计模式"
docsify_project_path = r"Z:\Project\Cardinal-Note-Document\docs"
docsify_project_note_relative_path = "/document/Java/JavaAdvancedTechnology/DesignMode/"

docsify_project_note_absolute_path = docsify_project_path + docsify_project_note_relative_path
commit_info = "提交信息"

# 生成 README.md
create_readme(note_folder_path)

# 更新 README.md 中的最后更新时间
update_readme_time(note_folder_path)

# 将笔记文件名中的中文数字替换为阿拉伯数字，将空格替换为“-”
rename_note_files_name(note_folder_path)

# 格式化笔记中，图片的语法
markdown_img_code_modifier(note_folder_path)

# 将笔记同步到docsify项目路径下
synchronizing_files(note_folder_path, docsify_project_note_absolute_path)

# 生成目录导航文件
generate_sidebar(note_folder_path, docsify_project_path, docsify_project_note_relative_path)

# TODO:自动执行提交推送指令
# TODO:需要将Github上的笔记和本地的同步了
