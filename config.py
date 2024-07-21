from pydantic import BaseSettings
from logging import WARNING


class GithubInputs(BaseSettings):
    # The offline token to use for the client auth
    input_offline_token: str
    # The domain for the provena deployment
    input_domain: str
    # The auth realm name
    input_realm_name: str
    # The item id to create new version for
    input_item_id: str
    # The reason to provide
    input_version_reason: str
    # The reason to provide
    input_update_reason: str | None
    # The set of attribute updates to apply after versioning, if any
    input_attribute_updates: str | None
    # The log level to display - defaults to WARNING - see https://docs.python.org/3/library/logging.html#levels
    input_log_level: int = WARNING

    # use .env file optionally for local testing
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
