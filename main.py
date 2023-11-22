from argparse import ArgumentParser
from pathlib import Path

from resizer import ImageResizer

if __name__ == '__main__':
    parser = ArgumentParser(prog='Images Resizer', description='Resize images')
    parser.add_argument(
        'path',
        type=Path,
        help='An absolute path to folder with video or a video'
    )
    args = parser.parse_args()
    if not args.path:
        try:
            path = Path(input('Inter an absolute path to folder with images: '))
        except Exception as e:
            print(f'An error occurred: {e}')
            raise SystemExit(1)
    else:
        path = args.path

    if not path.exists():
        print('The target path doesn\'t exist')
        raise SystemExit(1)

    try:
        resizer = ImageResizer(path)
    except FileNotFoundError:
        print(f'No such file or directory: {str(path)!r}')
        raise SystemExit(1)

    resizer()
