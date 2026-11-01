import os
from string import Template
import markdown

# 定义所有可能的模板变量（带 _en 和 _cn 后缀）
VARIABLES = [
    'home', 'publications', 'education', 'projects',
    'talk', 'teaching', 'cv', 'others'
]
SUFFIXES = ['_en', '_cn']

def read_markdown_to_html(filename):
    """读取 Markdown 文件并转换为 HTML，文件不存在时返回空字符串"""
    if not os.path.exists(filename):
        return ""
    
    with open(filename, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    return markdown.markdown(md_content)

def process_template():
    # 读取模板文件
    with open('index-template.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # 准备替换数据
    substitutions = {}
    
    for var in VARIABLES:
        for suffix in SUFFIXES:
            # 构造变量名（如 'home_en'）
            var_name = f"{var}{suffix}"
            
            # 构造对应的 Markdown 文件名（如 'home_en.md'）
            md_filename = f"{var_name}.md"
            
            # 读取并转换 Markdown 为 HTML
            html_content = read_markdown_to_html(md_filename)
            
            # 添加到替换字典
            substitutions[var_name] = html_content
    
    # 使用 string.Template 进行替换
    template = Template(template_content)
    result = template.safe_substitute(**substitutions)
    
    # 将结果写入 index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(result)

if __name__ == '__main__':
    process_template()
    print("模板处理完成，结果已保存到 index.html")