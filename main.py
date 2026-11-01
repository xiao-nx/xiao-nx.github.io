import os
import markdown
from string import Template
from pathlib import Path

def convert_md_to_html(folder_path, template_file):
    """
    将指定目录下所有的 .md 文件转换为 HTML，并嵌入到模板中。
    
    :param folder_path: 包含 Markdown 文件的目录路径
    :param template_file: HTML 模板文件路径（包含 $content 占位符）
    """
    # 1. 读取 HTML 模板内容
    try:
        with open(template_file, 'r', encoding='utf-8') as f:
            # 使用 string.Template 加载模板
            html_template = Template(f.read())
    except FileNotFoundError:
        print(f"错误：找不到模板文件 {template_file}")
        return

    # 2. 遍历指定目录
    folder = Path(folder_path)
    if not folder.is_dir():
        print(f"错误：{folder_path} 不是一个有效的目录")
        return

    # 获取所有 .md 和 .markdown 文件
    md_files = list(folder.glob('*.md')) + list(folder.glob('*.markdown'))

    for md_path in md_files:
        # 3. 读取 Markdown 内容
        with open(md_path, 'r', encoding='utf-8') as f:
            md_text = f.read()

        # 4. 将 Markdown 转换为 HTML
        # 这里开启了 'tables' (表格) 和 'fenced_code' (代码块) 扩展
        body_html = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])

        # 5. 替换模板中的 $content 键
        # 使用 safe_substitute 防止模板中其他带有 $ 的符号（如 JS 或 CSS）报错
        final_html = html_template.safe_substitute(content=body_html)

        # 6. 写入同名的 HTML 文件
        
        output_path = os.path.basename(md_path.with_suffix(".html"))
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        
        print(f"成功转换: {md_path.name} -> {output_path}")

if __name__ == "__main__":
    convert_md_to_html("markdown", "template.html")
