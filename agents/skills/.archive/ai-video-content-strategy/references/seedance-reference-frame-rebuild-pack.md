# Seedance 2.5 reference-frame rebuild pack

Use when Jared provides a reference video or screen recording and wants to rebuild his own version in Seedance 2.5, especially with Jared as the main person walking through generated scenes.

## Core outcome

Create a practical production folder Jared can hand to Seedance:

```text
Seedance_Rebuild_Walkthrough/
  01_reference_original_frames/
  02_clean_scene_refs_hard_crop_no_ui/
  02_best_scene_refs_selected/
  03_your_photo_drop_here/
  04_seedance_prompts/
  05_generated_clips_from_seedance/
  06_final_stitch/
```

## Extract 50 evenly spaced screenshots

Use midpoint sampling. It avoids grabbing pure start/end transitions.

```bash
VIDEO='/path/to/input.mp4'
OUTDIR='/path/to/seedance_reference_frames_50'
mkdir -p "$OUTDIR"
python3 - <<'PY'
import json, subprocess, csv
from pathlib import Path
video = Path('/path/to/input.mp4')
outdir = Path('/path/to/seedance_reference_frames_50')
duration = float(json.loads(subprocess.check_output([
  'ffprobe','-v','error','-show_entries','format=duration','-of','json',str(video)
], text=True))['format']['duration'])
count = 50
rows = []
for i in range(count):
    t = duration * (i + 0.5) / count
    outfile = outdir / f'frame_{i+1:03d}.png'
    subprocess.run([
      'ffmpeg','-hide_banner','-loglevel','error','-y',
      '-ss', f'{t:.6f}', '-i', str(video),
      '-frames:v','1', str(outfile)
    ], check=True)
    rows.append({'frame': outfile.name, 'timestamp_seconds': f'{t:.3f}'})
with open(outdir/'manifest.csv','w',newline='') as f:
    w = csv.DictWriter(f, fieldnames=['frame','timestamp_seconds'])
    w.writeheader(); w.writerows(rows)
PY
```

## Contact sheet review

```bash
ffmpeg -hide_banner -loglevel error -y -framerate 1 -i "$OUTDIR/frame_%03d.png" \
  -vf "scale=258:-1,tile=10x5:margin=8:padding=4:color=white" \
  "$OUTDIR/contact_sheet_10x5.jpg"
```

Always inspect the contact sheet before saying the pack is ready.

## Remove social/app UI from screen recordings

Do a crop-first cleanup. Do not jump straight to inpainting all frames.

- Crop away phone status bars, bottom playback controls, usernames, likes, comments, app icons, and social UI.
- Keep the output exact 9:16 for Seedance.
- Use inpainting only on the final selected frames if small UI traces remain and cropping would damage the scene.

Example hard crop for a 1290 x 2796 vertical screen recording:

```bash
ffmpeg -hide_banner -loglevel error -y -i "$INPUT" \
  -vf "crop=1125:2000:82:110,scale=1080:1920:flags=lanczos" \
  "$OUTPUT"
```

This removes most top and bottom UI while keeping exact 9:16. Adjust after visual review.

## Select only usable scene references

Do not send every extracted frame to Seedance. Create a selected folder and remove:

- profile pages
- app/control-centre frames
- black or mostly blank frames
- interface/navigation screens
- frames where UI dominates the scene
- duplicates that add no shot value

Keep a `selected_mapping.csv` that maps each selected scene back to the original frame number.

## Jared identity photo guidance

Before building final Seedance prompts, ask Jared for a reference photo:

- clear face
- good light
- no sunglasses
- full body or half body preferred
- standing/front-facing if possible

## Seedance prompt block for Jared walking through scenes

```text
Use the supplied clean reference frame as the scene/background style reference.
Use Jared's supplied photo as the main character identity reference.

Generate a cinematic vertical 9:16 video clip.
The main character is Jared, matching the supplied face and body reference. He begins facing camera so his face is visible, then turns and walks forward through the scene. Keep identity consistent across clips. Natural handheld street-video energy. Realistic motion. Smooth transition-friendly ending. No social media interface, no captions, no usernames, no phone UI, no playback controls, no logos, no text overlays.

Clip guidance:
- Duration: 3 to 5 seconds per frame/scene reference
- Camera: vertical phone-style cinematic, natural handheld movement
- Character action: Jared looks at camera briefly, then starts walking into the environment
- Style: realistic urban street footage, natural light, believable pedestrians and cars
- Negative prompt: Instagram UI, X UI, captions, usernames, likes, comments, icons, watermarks, phone status bar, black playback bar, distorted face, extra limbs, text
```

## Final response pattern

Be direct. Give Jared the folder path, the zip path if created, the best folder to use first, and the contact sheet. Explain UI removal in plain terms:

- crop is the best first pass
- inpainting is cleaner but may smear buildings or faces
- only inpaint final selected frames if needed
