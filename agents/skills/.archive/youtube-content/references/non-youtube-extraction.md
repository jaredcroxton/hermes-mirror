# Non-YouTube Video Transcript Extraction

When the user shares a video link that is NOT YouTube (HBR, Vimeo, Brightcove, etc.), the `fetch_transcript.py` script won't work. Use browser-based extraction instead.

## Brightcove / HBR Videos

HBR uses Brightcove player. Account ID is embedded in the player JS URL on the page.

### Workflow

1. **Navigate** to the video page with `browser_navigate`.
2. **Click play** on the video element (look for a button with "Play" in the accessible name).
3. **Enable captions** — look for a "Enable Captions" or CC button and click it.
4. **Extract text tracks via browser console.** The video is often inside a cross-origin iframe, so query all iframes:

```javascript
(() => {
  const iframes = document.querySelectorAll('iframe');
  let result = [];
  for (let f of iframes) {
    try {
      const vid = f.contentDocument?.querySelector('video');
      if (vid) {
        const tracks = vid.textTracks;
        if (tracks && tracks.length > 0) {
          for (let i = 0; i < tracks.length; i++) {
            tracks[i].mode = 'showing';
            const cues = tracks[i].cues;
            if (cues) {
              for (let j = 0; j < cues.length; j++) {
                result.push(cues[j].startTime + ': ' + cues[j].text);
              }
            }
          }
        }
      }
    } catch(e) {
      result.push('iframe cross-origin: ' + (f.src?.substring(0,80) || 'no src'));
    }
  }
  return result.join('\n');
})()
```

5. **Parse the cues** — they come back as `startTime: text`. Clean and format.

### Pitfalls

- The video element may be inside a **nameless iframe** (src=""), not the obvious Brightcove one. The script above iterates ALL iframes to catch it.
- `firecrawl_scrape` on HBR video pages often fails (credits, paywall). Browser is the reliable path.
- Captions must be manually enabled — they're off by default on HBR.
- Cross-origin iframes will throw — that's expected. The one that succeeds is the one with the video.
