from network.properties.OpenAIproperties import OpenAIData
from interfaces.Models import ModelsInterface


class OpenAIModels(ModelsInterface):
    @staticmethod
    def OpenAIStickerModel_dall_e_3(prompt: str) -> OpenAIData:
        prompt = f"""
            a cute design of {prompt} kwaii sticker, white background, simple
            """
        return OpenAIData(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

    @staticmethod
    def OpenAIStickerKwaiiModel_dall_e_2(prompt: str) -> OpenAIData:
        prompt = f"""A cute design of {prompt} kwaii sticker"""
        return OpenAIData(
            model="dall-e-2",
            prompt=prompt,
            size="512x512",
            quality="standard",
            n=1,
        )

    @staticmethod
    def OpenAIStickerRealisticModel_dall_e_3(
        prompt: str,
    ) -> OpenAIData:
        prompt = f"""A cute design of {prompt} realistic sticker"""
        return OpenAIData(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
    
    @staticmethod
    def OpenAIStickerAnimeModel_dall_e_3(
        prompt: str,
    ) -> OpenAIData:
        prompt = f"""A anime design of {prompt} sticker"""
        return OpenAIData(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
    
    @staticmethod
    def OpenAIStickerRealisticModel_dall_e_2(
        prompt: str,
    ) -> OpenAIData:
        prompt = f"""A cute design of {prompt} realistic sticker"""
        return OpenAIData(
            model="dall-e-2",
            prompt=prompt,
            size="512x512",
            quality="standard",
            n=1,
        )
    @staticmethod
    def OpenAIStickerGraffitiModel_dall_e_3(
        prompt: str,
    ) -> OpenAIData:
        prompt = f"""A cute design of {prompt} graffiti sticker"""
        return OpenAIData(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
    
    @staticmethod
    def OpenAI_Image_dall_e_3(
        prompt: str,
    ) -> OpenAIData:
        return OpenAIData(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )