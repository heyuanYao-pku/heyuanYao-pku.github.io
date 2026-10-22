"""Regenerate browser-friendly animations and posters with FFmpeg.

Usage: python3 scripts/optimize-media.py --ffmpeg /path/to/ffmpeg
The original media is preserved. FFmpeg is only needed when regenerating assets.
"""

import argparse
from pathlib import Path
import subprocess


ASSETS = Path(__file__).resolve().parents[1] / 'src' / 'assets'
GIFS = ['motion_matching', 'world_model', 'dance', 'moconvq', 'skill']
VIDEOS = {
    'lumine-combat': 'lumine/combat.mp4',
    'lumine-npc': 'lumine/npc.mp4',
    'lumine-defeat': 'lumine/defeat.mp4',
    'lumine-clear': 'lumine/clear.mp4',
    'lumine-wind': 'lumine/Wind.mp4',
    'obstacle': 'obstacle.mp4',
    'indoors': 'indoors.mp4',
    'genshin-demo': 'genshin_main_demo_540p.mp4',
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ffmpeg', default='ffmpeg')
    args = parser.parse_args()
    output = ASSETS / 'optimized'
    output.mkdir(exist_ok=True)

    def run(*options):
        subprocess.run([args.ffmpeg, '-hide_banner', '-loglevel', 'error', '-y', *map(str, options)], check=True)

    for name in GIFS:
        source = ASSETS / (name + '.gif')
        target = output / (name + '.mp4')
        run('-i', source, '-an', '-vf', "fps=24,scale='trunc(min(960,iw)/2)*2':-2",
            '-c:v', 'libx264', '-preset', 'medium', '-crf', '25', '-pix_fmt', 'yuv420p',
            '-movflags', '+faststart', target)
        run('-i', target, '-frames:v', '1', '-vf', 'scale=480:-2', '-q:v', '4', output / (name + '.jpg'))
        print(f'{name}: {source.stat().st_size / 1024:.0f} KiB -> {target.stat().st_size / 1024:.0f} KiB', flush=True)

    for name, path in VIDEOS.items():
        run('-ss', '0.2', '-i', ASSETS / path, '-frames:v', '1', '-vf', 'scale=480:-2',
            '-q:v', '4', output / (name + '.jpg'))
    print('All video posters generated.', flush=True)


if __name__ == '__main__':
    main()
