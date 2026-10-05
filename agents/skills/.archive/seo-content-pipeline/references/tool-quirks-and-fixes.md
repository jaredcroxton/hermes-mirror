# Tool Quirks and Fixes for SEO Content Production

## execute_code read_file → write_file corruption

**Symptom:** After using `read_file` in `execute_code` and writing the result back via `write_file`, the file shows doubled line numbers. Every line reads like `     1|     1|content` or `    88|    88|content`.

**Root cause:** The `read_file` function in `execute_code` returns content WITH line number prefixes (format: `     1|content`). The `write_file` function writes the string verbatim, baking those prefixes into the file.

**Fix:**
```python
import re
path = "/path/to/corrupted/file.md"
with open(path) as f:
    content = f.read()

# Strip line number prefixes: leading spaces + digits + pipe
cleaned = re.sub(r'^ +\d+\|', '', content, flags=re.MULTILINE)

with open(path, 'w') as f:
    f.write(cleaned)
```

**Prevention:** When using `execute_code` to read and rewrite files, either:
- Use the standalone `patch` tool for targeted text replacements (preferred)
- Strip line numbers from read_file output before writing
- Use `terminal` with Python directly instead of `read_file`/`write_file`

## Patch matching too broadly in HTML

**Symptom:** A patch that targets one FAQ Q&A block removes multiple adjacent Q&A blocks, or replaces more content than intended.

**Root cause:** HTML with repetitive structures (like `.faq-item` divs) has sections that look similar. If `old_string` matches only a generic button or span, it may match 20+ occurrences.

**Fix:** When constructing `old_string` for HTML patches, include unique surrounding elements:
- Start the match string at a unique parent element
- Include the full Q&A block with both the question AND the answer
- Use the adjacent sibling element as an end anchor
- For catalogue sections, include the instrument name in the match context

**Example of good old_string (includes unique instrument name + sibling anchor):**
```
### [Pulse Check 360](/pulse-check-360)
...full content...
### [Performlytics](/performlytics)
```

**Example of bad old_string (too generic, matches everywhere):**
```
<div class="faq-item">
```

## Line number artefacts in read_file

**Symptom:** `read_file` output from `execute_code` appears to have line numbers embedded in the content.

**Details:** The `read_file` tool in `execute_code` returns content in format `LINE_NUM|CONTENT`. When this content is stored in a Python variable and manipulated, the line number prefix is part of the string. String operations like `.replace()` must account for the prefix or be run against a cleaned version of the content.

**Workaround:** Use `terminal` with Python's native `open().read()` to get raw file content without prefixes, or use the standalone `patch` tool which operates directly on files.

**Two-pass corruption pitfall:** If the file has been corrupted TWICE (write_file baked in line numbers, then a second write_file baked them in again creating doubled numbers like `     1|     1|content`), a single regex pass with `r'^ +\d+\|'` only strips the FIRST set. The doubled pattern requires `r'^ +\d+\| +\d+\|'` or two passes. Always verify after cleaning — if lines still show `    88|content`, run the regex again.
