import os
import logging

from dotenv import load_dotenv
from network.OpenAIHandler import OpenAIConector

from src.ImageCreator import ImageCreator
from src.models.OpenAIModel import OpenAIModels


load_dotenv()


def main() -> str:
    prompt = "a black rose"
    logging.basicConfig(
        level=logging.DEBUG
        if os.getenv("ENVIRONMENT") == "dev"
        else logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler()],
    )

    env = os.getenv("ENVIRONMENT")

    conn = OpenAIConector()

    data_model = {
        "dev": OpenAIModels.OpenAIStickerKwaiiModel_dall_e_2(
            prompt=prompt
        ),
        "prod": OpenAIModels.OpenAIStickerGraffitiModel_dall_e_3(
            prompt=prompt
        ),
    }

    creator = ImageCreator(data_model[env], conn)
    creator.get_image()


if __name__ == "__main__":
    main()
