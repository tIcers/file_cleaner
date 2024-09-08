import os
import time

from send2trash import send2trash

downloads_folder = os.path.expanduser("~/Downloads/")

image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", "webp"}


def delete_images():
    now = time.time()

    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        if os.path.isfile(file_path):
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                try:
                    send2trash(file_path)
                    print(
                        f"{now}: Deleting {file_path}... You can find them in your trash"
                    )
                except Exception as e:
                    print(f"Failed to move {file_path} to trash. Reason {e}")


if __name__ == "__main__":
    print("the function is called... ")
    delete_images()
