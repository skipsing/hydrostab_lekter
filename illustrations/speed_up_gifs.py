from pathlib import Path
from PIL import Image

SPEED_FACTOR = 1.35  # >1 means faster playback
REPO_ROOT = Path(__file__).resolve().parents[1]
src_dir = REPO_ROOT / "media/videos/main/480p15"
out_dir = REPO_ROOT / "exports"
out_dir.mkdir(exist_ok=True)

def speed_up_gif(src: Path, dst: Path, factor: float) -> None:
    with Image.open(src) as im:
        frames = []
        durations = []

        for i in range(im.n_frames):
            im.seek(i)
            frame = im.convert("P")
            # GIF duration is milliseconds per frame.
            original = im.info.get("duration", 67)
            new_duration = max(20, int(round(original / factor)))
            frames.append(frame.copy())
            durations.append(new_duration)

        frames[0].save(
            dst,
            save_all=True,
            append_images=frames[1:],
            duration=durations,
            loop=0,
            optimize=False,
            disposal=2,
        )


gifs = sorted(src_dir.glob("*.gif"))
if not gifs:
    print("No GIF files found in media/videos/main/480p15")
else:
    for gif in gifs:
        out_name = gif.stem + "_fast.gif"
        out_path = out_dir / out_name
        speed_up_gif(gif, out_path, SPEED_FACTOR)
        print(f"Created: {out_name}")

    print(f"Done. Created {len(gifs)} fast GIFs in exports/")
