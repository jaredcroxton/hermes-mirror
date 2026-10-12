# HyperFrames capability install and demo pattern for specialist profiles

Use this when Jared asks to make sure a specialist agent, especially Bob, has a newly discovered tool/skill and can prove it with a demo artifact.

## Durable pattern

1. Treat this as a profile capability deployment, not a local-only install.
2. Verify the base runtime first:
   - `node -v`
   - `npm -v`
   - `ffmpeg -version`
   - `claude --version` if the workflow depends on Claude Code.
3. Install or copy the capability into the specialist profile's skill library, not only the working project.
4. Probe the specialist profile brain directly:
   - `hermes --profile <profile> chat -q "reply with <marker>" --quiet`
5. Ask the specialist to produce a small real artifact, not a verbal claim.
6. Independently verify the output exists and has expected media properties.
7. Deliver the artifact in-chat via `MEDIA:<absolute-path>`.

## Bob + HyperFrames specifics

Bob's profile is `bobbuilder`. For a HyperFrames proof, the useful chain is:

```text
Brock routes → Bob builds → HyperFrames renders MP4
```

Expected prerequisites:

- Node.js 22+
- npm / npx
- FFmpeg installed and on PATH
- Claude Code authenticated if Bob is using Claude Code as the builder lane
- HyperFrames available via `npx hyperframes`

A good proof is a 10 to 20 second branded MP4, rendered from HTML/CSS and verified with `ffprobe` or equivalent. Do not stop at a project scaffold or a claim that the command should work.

## Pitfalls

- Project-local `.agents/skills` does not prove the specialist profile has the skill. Check or install into the profile-level skill library as well.
- A successful local HyperFrames command does not prove Bob can use it. Probe Bob's profile and have Bob produce the demo.
- Do not report a file path only. Jared expects the artifact delivered into chat as MEDIA.
- Do not overbuild the demo. The point is capability proof, not a full campaign asset.
