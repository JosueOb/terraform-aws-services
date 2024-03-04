from app.ports import SecretManager

from ._aws import AWSSecretManagerClient


def secret_manager_factory() -> SecretManager:
    """
    A factory function that returns a concrete implementation of the SecretManager port.

    Returns:
        SecretManager: A concrete implementation of the SecretManager port.
    """
    return AWSSecretManagerClient()
