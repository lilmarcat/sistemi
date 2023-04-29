from abc import ABC, abstractmethod

class CipherInterface(ABC):
    @abstractmethod
    def encrypt(self, data: str) -> str:
        pass

    @abstractmethod
    def decrypt(self, encrypted_data: str) -> str:
        pass

    @abstractmethod
    def set_key(self, key: str) -> None:
        pass

    @abstractmethod
    def get_key(self) -> str:
        pass