import os

from openai import OpenAI
from dotenv import load_dotenv

from interfaces.Connector import ConnectorInterface
from exceptions.ConnectorException import ConnectorException
from network.properties.OpenAIproperties import OpenAIData

class OpenAIConector(ConnectorInterface):
    def __init__(self):
        self.conn = self.__connect__()

    def __connect__(self):
        def __open_ai_connector():
            api_key = os.getenv("API_KEY")
            try:
                conn = OpenAI(api_key=api_key)
            except OpenAI.OpenAIError as e:
                raise ConnectorException(e)
            return conn

        return __open_ai_connector()

    def send_prompt(self, data_model: OpenAIData):
        self.response = self.conn.images.generate(
            **data_model.__dict__
        )
            
    @property
    def get_response(self):
        return self.response.data[0].url