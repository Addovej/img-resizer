from pathlib import Path

from PIL import Image
from tqdm import tqdm


class ImageResizer:
    max_size: int = 1280

    def __init__(self, source_dir: Path) -> None:
        self.source_dir: Path = source_dir
        self.save_dir = self.source_dir / f'{self.source_dir.name} {self.max_size}_RESIZED'
        self.save_dir.mkdir(exist_ok=True)

    def __call__(self) -> None:
        images = sorted(self.source_dir.iterdir())
        print(f'Found {len(images)} images. Start resizing...')

        for img in tqdm(images, total=len(images)):
            if not img.is_file() or img.name.startswith('.'):
                continue

            # PIL resize
            self.thumbnail_pillow(img)

        print(f'Resizing done. Saved to {str(self.save_dir)!r} folder.')

    def thumbnail_pillow(self, img: Path) -> None:
        image = Image.open(str(img))

        image.thumbnail((self.max_size, self.max_size))
        image.save(self.save_dir / f'{img.stem}_thumbnail.png')
