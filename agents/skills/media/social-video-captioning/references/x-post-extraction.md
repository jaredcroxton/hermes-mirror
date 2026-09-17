# X/Twitter post extraction for talking points

Use this when Jared sends an X/Twitter link and asks for talking points, captions, or a strategic take.

## Why

X pages often fail in normal browser or scrape tools. Do not stop at the failed page load. The post may still be available through embed or syndication endpoints.

## Extraction order

1. Try the normal scrape/browser path if available.
2. If the page is blocked or empty, call the public oEmbed endpoint:

```bash
python3 - <<'PY'
import urllib.parse, urllib.request
status_url = 'https://twitter.com/<handle>/status/<id>'
url = 'https://publish.twitter.com/oembed?' + urllib.parse.urlencode({
    'url': status_url,
    'omit_script': 'true',
})
print(urllib.request.urlopen(url, timeout=20).read().decode())
PY
```

3. If oEmbed truncates the post, try a metadata mirror endpoint such as:

```text
https://api.fxtwitter.com/<handle>/status/<id>
```

This can return full text, author, date, metrics, media URLs, and media formats.

4. For attached video, download a low or mid bitrate MP4 for inspection, then create a contact sheet:

```bash
ffprobe -v error -show_entries format=duration -show_entries stream=width,height,codec_name -of default=noprint_wrappers=1 video.mp4
ffmpeg -hide_banner -loglevel error -i video.mp4 -vf "fps=1/5,scale=720:720" -q:v 2 frame_%02d.jpg
```

5. Use the post text plus the visual narrative to draft the output. Do not rely on the text alone when a video is attached.

## Output pattern for Jared

For talking points, default to:

- Core point
- Talking points
- If speaking as Jared
- Relevant business angle
- Watch-outs
- Strongest one-liner

Keep it punchy. Avoid process notes unless the extraction affects confidence.

## Pitfalls

- Do not state that X cannot be accessed after one failed browser scrape.
- Do not treat oEmbed text as complete if it ends with an ellipsis.
- Do not over-index on public metrics. Use them only as context, not as the argument.
- For posts about Hermes Agent or AI tooling, load the relevant Hermes/product skill before adding strategic commentary.
