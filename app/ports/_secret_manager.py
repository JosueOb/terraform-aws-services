from abc import ABC, abstractmethod


class SecretManager(ABC):
    """Abstract base class for secret managers."""

    @abstractmethod
    async def get_secret(self, secret_name: str):
        """Retrieve a secret by its name.

        Args:
            secret_name (str): The name of the secret to retrieve.

        Returns:
            The secret value.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
            SecretManagerError: If an error occurs while retrieving the secret.
        """
