修改网页只需要修改 template.html.

修改网页样式（字体、颜色、间距等），在 main.css 修改。

每次修改了 template.html 或 任何 markdown 文件后，运行 python main.py

markdown 目录下每个 .md 文件生成一个 .html，对应网页顶部导航条的一个栏目，例如 about，team，research_overview。

要添加一个新的下拉菜单项目：

1. 在 template.html 中相应的菜单项下面，添加 \<div href="research_overview"\>research overview\</div\> 一样的条目。href 的名字对应它要使用的 markdown 文件的名字，中间是网页中要显示的文字，例如 href="research_overview" 使用 research_overview.md 文件
2. 在 markdown 目录中创建或修改相应的 markdown 文件，例如 research_overview.md
3. 运行 python main.py
