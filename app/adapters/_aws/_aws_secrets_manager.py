from contextlib import AsyncExitStack

from aioboto3.session import Session

from app.exceptions import SecretManagerError
from app.ports import SecretManager


class AWSSecretManagerClient(SecretManager):
    """
    A class that represents an AWS Secrets Manager client.

    This class provides methods to interact with AWS Secrets Manager service.
    """

    def __init__(self):
        self._session: Session = Session()
        self._exit_stack: AsyncExitStack = AsyncExitStack()
        self._client_config = {"service_name": "secretsmanager"}

    async def get_secret(self, secret_name: str):
        """
        Retrieves the value of a secret from AWS Secrets Manager.

        Args:
            secret_name (str): The name of the secret.

        Returns:
            str: The value of the secret.

        Raises:
            SecretManagerError: If there is an error in getting the secret.
        """
        try:
            async with self._session.client(**self._client_config) as client:
                response = await client.get_secret_value(SecretId=secret_name)
                return response.get("SecretString")
        except Exception as error:
            raise SecretManagerError(f"Error in getting a secret: {error}") from error
