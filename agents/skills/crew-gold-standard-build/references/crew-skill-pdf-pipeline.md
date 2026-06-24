# Crew Skill → PDF Pipeline

## When to use
When Jared asks to convert a Crew SKILL.md into a styled, shareable PDF. This pipeline turns any gold-standard skill into a print-ready document with PerformOS brand styling.

## Proven pipeline (24 June 2026)

### Step 1: Convert markdown to styled HTML
Use a Python script that reads the SKILL.md and produces a single self-contained HTML file.

**Styling rules (PerformOS brand):**
- Fonts: Instrument Serif (h1/h2), Inter (body), JetBrains Mono (code)
- Colours: cream `#fafaf7` background, charcoal `#0a0a0a` headings, lime `#d4ff3b` code blocks on ink `#1a1a1a`
- Code blocks: ink background, lime green text
- Page size: A4, 22-25mm margins
- Print media query strips background colour to white, prevents code block breaks

**Conversion logic:**
- Skip YAML frontmatter (`---` to `---`)
- `#` → `<h1>`, `##` → `<h2>`, `###` → `<h3>`
- Fenced code blocks → `<pre><code>` with HTML entity escaping
- `- ` list items → `<li>`
- Numbered list items → `<li>`
- `---` → `<hr>`
- Plain lines → `<p>`

### Step 2: Print to PDF with Chrome headless
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu \
  --print-to-pdf=/path/to/output.pdf \
  --no-margins /tmp/skill.html
```

The `--no-margins` flag lets the CSS `@page` directive control margins. Chrome errors about `TASK_CATEGORY_POLICY` and `TASK_SUPPRESSION_POLICY` are harmless — they're macOS sandbox noise, not PDF failures.

### Step 3: Open
```bash
open /path/to/output.pdf
```

## Pitfalls

- **execute_code sandbox caches read_file results.** If a file was read earlier in the conversation by the `read_file` tool, `execute_code`'s `read_file` will return `"File unchanged since last read"` with no content. Use `terminal` with a Python heredoc that reads the file directly via `open()` instead.
- **WeasyPrint has native library dependencies** (`libgobject-2.0-0`) that may not be installed. Chrome headless is more reliable on macOS.
- **Google Fonts `@import` in the HTML** requires network access during PDF generation. Chrome headless handles this. If offline, fall back to system fonts.
- **71KB skills produce ~290KB PDFs.** Budget accordingly for multi-skill batches.
- **Code blocks with unescaped HTML** (`<div>`, `<App />`) break the layout. Always escape `&`, `<`, `>` inside code blocks during the markdown-to-HTML conversion.
