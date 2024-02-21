from contextlib import AsyncExitStack
import asyncio
from aioboto3.session import Session
from types_aiobotocore_secretsmanager.client import SecretsManagerClient


class AWSSecretsManagerError(Exception):
    """
    This exception is thrown when the AWS secrets manager client fails
    """


class AWSSecretManagerClient:
    def __init__(self):
        self._session: Session = Session()
        self._exit_stack: AsyncExitStack = AsyncExitStack()
        self._client_config = {"service_name": "secretsmanager"}

    async def get_secret(self, secret_name: str):
        try:
            async with self._session.client(**self._client_config) as client:
                client: SecretsManagerClient
                response = await client.get_secret_value(SecretId=secret_name)
                return response.get("SecretString")
        except Exception as error:
            raise AWSSecretsManagerError(f"Error in getting a secret: {error}")


async def main():
    client = AWSSecretManagerClient()
    secret_name = "system_credentials"
    secret_value = await client.get_secret(secret_name)
    print(f"SECRET VALUE >>> {secret_value}")


if __name__ == "__main__":
    asyncio.run(main())
