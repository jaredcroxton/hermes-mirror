# Video Frame Extraction for Vision Analysis

When you have MP4 video files and need to review their content, you cannot feed them directly to `vision_analyze` — it only accepts image files. Use this ffmpeg technique to extract representative frames, then analyze those.

## The technique

```bash
# Extract frames at 25%, 50%, and 75% of video duration
mkdir -p /tmp/reel-frames/"Reel Name"
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "video.mp4")
ffmpeg -y -ss $(echo "$DUR * 0.25" | bc -l) -i "video.mp4" -frames:v 1 -q:v 3 "/tmp/reel-frames/Reel Name/frame_25pct.jpg"
ffmpeg -y -ss $(echo "$DUR * 0.50" | bc -l) -i "video.mp4" -frames:v 1 -q:v 3 "/tmp/reel-frames/Reel Name/frame_50pct.jpg"
ffmpeg -y -ss $(echo "$DUR * 0.75" | bc -l) -i "video.mp4" -frames:v 1 -q:v 3 "/tmp/reel-frames/Reel Name/frame_75pct.jpg"
```

## Batch version (all MP4s in a directory)

```bash
cd "/path/to/videos"
for f in *.mp4; do
  name=$(basename "$f" .mp4)
  mkdir -p "/tmp/reel-frames/$name"
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f" 2>/dev/null)
  echo "$name: ${dur}s"
  for pct in 25 50 75; do
    seek=$(echo "$dur * $pct / 100" | bc -l)
    ffmpeg -y -ss "$seek" -i "$f" -frames:v 1 -q:v 3 "/tmp/reel-frames/$name/frame_${pct}pct.jpg" 2>/dev/null
  done
done
```

## Why 25-50-75

- **25%**: Captures the transition from hook into body. Shows what happens after the opening seconds.
- **50%**: Midpoint. Shows the core message or value proposition phase.
- **75%**: Near-close. Shows the call to action, the payoff, or how the creative resolves.

Three frames per reel is enough to understand the format (talking-head vs motion graphics), the visual style, the text overlay treatment, and the narrative arc — without watching the full video.

## Pitfalls

- `ffprobe` and `ffmpeg` must be installed. On macOS: `brew install ffmpeg`. Already present on most Hermes environments.
- Long videos (3+ minutes) may benefit from more frames (every 15-20% instead of 25-50-75).
- The `2>/dev/null` on ffmpeg suppresses noisy encode progress output. Remove it if debugging extraction failures.
- Frames at exact percentage positions may land on transitions or black frames. If a frame is blank, retry at ±5%.
