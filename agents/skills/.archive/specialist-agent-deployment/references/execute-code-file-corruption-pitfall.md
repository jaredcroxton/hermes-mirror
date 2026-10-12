# execute_code read_file → write_file Corruption

## The bug

`read_file()` in `execute_code` returns content with line-number prefixes:

```
     1|---
     2|title: "..."
     3|...
```

Writing that content back via `write_file()` bakes the prefixes into the file. Every subsequent `read_file()` compounds the corruption (double, triple prefixes).

## Detection

File content shows doubled line numbers:
```
     1|     1|---
     2|     2|title: "..."
```

## Fix

Strip line numbers before any write_file:

```python
import re
content = re.sub(r'^ +\d+\|', '', content, flags=re.MULTILINE)
```

## Prevention

**Prefer `patch()` over `write_file()` for targeted edits on existing files.** Patch operates on the file on disk, not the in-memory read_file output, so it avoids this class of bug entirely.

Only use `write_file()` for new files or when the content is constructed from scratch (not from a `read_file()` call).

## Recovery

If a file is already corrupted:

```python
import re
with open(path) as f:
    content = f.read()
# Strip all layers of line number prefixes
while re.match(r'^ +\d+\|', content):
    content = re.sub(r'^ +\d+\|', '', content, flags=re.MULTILINE)
with open(path, 'w') as f:
    f.write(content)
```
