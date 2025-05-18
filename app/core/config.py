import os
from dotenv import load_dotenv

load_dotenv()

def get_env_or_raise(key: str) -> str:
    """
    Get the value of an environment variable or raise an error if it is not set.
    """
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"{key} environment variable is required")
    return value


GROQ_ACCESS_TOKEN = get_env_or_raise("GROQ_ACCESS_TOKEN")
MODEL = get_env_or_raise("MODEL")
MONGODB_URI = get_env_or_raise("MONGODB_URI")
