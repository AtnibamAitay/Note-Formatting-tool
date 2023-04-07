from create_readme import create_readme
from rename_note_files_name import rename_note_files_name
from sidebar_generator import generate_sidebar

note_folder_path = r"C:\Users\Atnibam Aitay\Downloads"
docsify_project_path = r"C:/Users/Atnibam Aitay"
docsify_project_note_path = "/document/Java/JavaAdvancedTechnology/Nginx/"


# 生成 README.md
create_readme(note_folder_path)

# 将笔记文件名中的中文数字替换为阿拉伯数字，将空格替换为“-”
rename_note_files_name(note_folder_path)

# TODO:自动将笔记同步到docsify项目路径下

# 生成目录导航文件
generate_sidebar(note_folder_path)