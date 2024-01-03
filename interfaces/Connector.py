from abc import ABC, abstractmethod


class ConnectorInterface(ABC):
    @abstractmethod
    def __connect__(self):
        pass

    @abstractmethod
    def send_prompt(self):
        pass

    @abstractmethod
    def get_response(self):
        pass
