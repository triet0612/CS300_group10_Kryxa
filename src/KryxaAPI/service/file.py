import io
from PIL import Image


# Path for resources is at bin/res, create folder before proceed
class FileManager:
    def __init__(self):
        self.path = "./bin/system/"

    def read_image(self, item_id: int):
        base_width = 224
        img = Image.open(self.path + str(item_id) + ".png")
        wpercent = (base_width / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
        img_stream = io.BytesIO()
        img.save(img_stream, format="PNG")
        return img_stream.getvalue()

    def create_image(self, item_id: id, filestream: bytes):
        img = Image.open(io.BytesIO(filestream))
        img.convert("RGBA")
        img.save(self.path + str(item_id) + ".png")


def get_file() -> FileManager:
    return FileManager()
