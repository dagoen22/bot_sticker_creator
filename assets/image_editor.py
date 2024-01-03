import logging

from rembg import remove

class ImageEditor():
    def __init__(self, image_path):
        self.image = image_path
    
    def remove_background(self):
        def __load_image():
            logging.info("Loading image to remove background...")
            with open(self.image, 'rb') as i:
                return i.read()

        def __remove_background(input):
            logging.info("Removing background...")
            return remove(input)

        def __save_image(output):
            logging.info("Saving image without background")
            with open(self.image, 'wb') as o:
                o.write(output)
                logging.info(f"Image saved to: {self.image}")

        def __load_and_remove_background():
            input_image = __load_image()
            output = __remove_background(input_image)
            __save_image(output)

        __load_and_remove_background()