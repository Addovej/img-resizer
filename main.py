from pathlib import Path

from resizer import ImageResizer

if __name__ == '__main__':

    try:
        path = Path(input('Inter an absolute path to folder with images: '))
    except Exception as e:
        print(f'An error occurred: {e}')
        raise SystemExit(1)

    try:
        resizer = ImageResizer(path)
    except FileNotFoundError:
        print(f'No such file or directory: {str(path)!r}')
        raise SystemExit(1)

    resizer()
