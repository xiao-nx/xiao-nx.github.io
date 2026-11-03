
# Website Maintenance Guide

This website is generated from Markdown files using a Python script and a shared HTML template.

## File Structure

- `template.html` — Defines the website layout and navigation menu.
- `main.css` — Controls the website appearance, including fonts, colors, and spacing.
- `main.py` — Generates HTML pages from Markdown files.
- `markdown/` — Contains the Markdown source files for individual pages.

## Editing the Website

- **Content:** Edit the corresponding `.md` file in the `markdown/` directory.
- **Layout and navigation:** Edit `template.html`.
- **Styling:** Edit `main.css` to adjust fonts, colors, spacing, and other visual elements.

After modifying `template.html` or any Markdown file, regenerate the website by running:

```bash
python main.py
```

Each `.md` file in the `markdown/` directory generates a corresponding `.html` page. These pages can be linked from the website's navigation menu, such as `about`, `team`, or `research_overview`.

## Adding a New Dropdown Menu Item

1. **Update the navigation menu** in `template.html`.

   Add a new entry under the appropriate dropdown menu:

   ```html
   <div href="research_overview">Research Overview</div>
   ```

   The `href` value must match the Markdown filename without the `.md` extension. For example, `research_overview` corresponds to `research_overview.md`. The text between the tags is the label displayed in the navigation menu.

2. **Create the corresponding Markdown file** in the `markdown/` directory:

   ```text
   markdown/research_overview.md
   ```

   Add or update the page content in this file.

3. **Regenerate the website** by running:

   ```bash
   python main.py
   ```

The new page will be generated and accessible through the dropdown menu.
