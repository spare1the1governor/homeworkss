from PIL import Image
import os

class JPEGCompressor:
    def __init__(self, quality = 100):
     self.image = None
     self.quality= quality

    def load(self, filepath):
        if os.path.exists(filepath) is True:
            with Image.open(filepath) as img:
                if img.format == "JPEG":
                    self.image=img.copy()
                else:
                    raise TypeError()
        else:
            raise FileNotFoundError()

    def compress(self, quality):
        if self.image is None:
            raise FileNotFoundError
        elif 0<=quality<=95:
            self.quality = quality
        else:
            raise ValueError

    def save(self, filepath):
       try:
         self.image.save(filepath, format="JPEG", quality = self.quality, optimize=True)
       except Exception:
           raise FileNotFoundError