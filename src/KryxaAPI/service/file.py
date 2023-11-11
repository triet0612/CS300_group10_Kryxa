import io

from PIL import Image


# Path for resources is at bin/res, create folder before proceed
class FileManager:
    def __init__(self):
        self.path = "./bin/res/"

    def read_image(self, filepath: str):
        img = Image.open(self.path + filepath)
        img_stream = io.BytesIO()
        sep_filename = filepath.split(".")
        file_format = sep_filename[1]
        if file_format == "jpg":
            img.save(img_stream, format="JPEG")
        elif file_format == "png":
            img.save(img_stream, format="PNG")
        else:
            raise ValueError("Wrong file format")
        return img_stream.getvalue()

    def create_image(self, filepath: str, filestream: bytes):
        img = Image.open(io.BytesIO(filestream))
        img.save(self.path + filepath)


def get_file() -> FileManager:
    return FileManager()
