import os
import requests
from uuid import uuid4

import logging

from interfaces.Models import ModelsInterface
from interfaces.Connector import ConnectorInterface

from assets.image_editor import ImageEditor

class ImageCreator:
    def __init__(self, data_model: ModelsInterface, connector: ConnectorInterface) -> str:
        self.data_model = data_model
        self.connector = connector
        self.__send_prompt()
        logging.info(f"using connector: {self.connector}")
        logging.info(f"using data model: {self.data_model}")
        
        logging.debug(f"Working on: \033[31m{os.getenv('ENVIRONMENT')}\033[0m")

    def __send_prompt(self):
        logging.info("Sending prompt...")
        try:
            self.connector.send_prompt(self.data_model)
        except Exception as e:
            logging.error(f"Could not send prompt. Error: {e}")

    def get_url(self):
        self.url = self.connector.get_response
        return self.url
    
    def __remove_bg(self):
        editor = ImageEditor(self.image_path)
        editor.remove_background()
        
    def get_image(self):
        self.image_name = uuid4().__str__()

        path = os.getenv("IMG_PATH")
        if not path: path = os.getcwd()

        self.image_path = f"{path}/{self.image_name}.png"

        logging.info(f"generating image with name: {self.image_name}")
        def __request_image():
            self.__image = requests.get(self.get_url())

        def __downlaod_image():
            path = os.getenv("IMG_PATH")
            if not path: path = os.getcwd()

            os.makedirs(path, exist_ok=True)
            with open(self.image_path, "wb") as file:
                logging.info(f"downloading image")
                file.write(self.__image.content)

        __request_image()
        __downlaod_image()
        self.__remove_bg()
        logging.info(f"image saved to: {self.image_path}")