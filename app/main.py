import asyncio
import logging

from app.adapters import secret_manager_factory


async def main():
    """
    This is the main function of the application.
    It retrieves a secret value from the secret manager and logs it.
    """
    secret_name = "system_credentials"
    secret_manager = secret_manager_factory()
    secret_value = await secret_manager.get_secret(secret_name)
    logging.info("SECRET VALUE: %s", secret_value)


if __name__ == "__main__":
    asyncio.run(main())
