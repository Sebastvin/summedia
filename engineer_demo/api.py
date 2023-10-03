from abc import ABC, abstractmethod


class APIRequester(ABC):
    """Abstract class to handle API requests."""

    @abstractmethod
    def request_api(self, *args, **kwargs) -> str:
        """Abstract method for making API requests."""
        pass
