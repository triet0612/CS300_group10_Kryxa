import io
from PIL import Image


# Path for resources is at bin/res, create folder before proceed
class FileManager:
    def __init__(self):
        self.path = "./bin/system/"

    def read_image(self, item_id: int):
        img = Image.open(self.path + str(item_id) + ".png")
        img_stream = io.BytesIO()
        img.save(img_stream, format="PNG")
        return img_stream.getvalue()

    def create_image(self, item_id: id, filestream: bytes):
        img = Image.open(io.BytesIO(filestream))
        img.convert("RGBA")
        img.save(self.path + str(item_id))


def get_file() -> FileManager:
    return FileManager()
