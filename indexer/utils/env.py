import os
import typing



# Package env var prefix.
_PREFIX = 'CDF2CIM_INDEXER_'


def get_var(
    name: str,
    default=None,
    convertor: typing.Callable = None
    ) -> str:
    """Returns an environment variable's current value.

    :param name: Environment variable name.
    :param default: Environment variable default value.
    :param convertor: Value conversion function to apply.

    :returns: An environment variable's current value.

    """
    name = get_var_name(name)
    value = os.getenv(name)
    value = value or default

    return value if convertor is None or value is None else convertor(value)


def get_var_name(name: str) -> str:
    """Returns an environment variable's name.

    :param name: Environment variable name.

    :returns: An environment variable's full name.

    """
    return f'{_PREFIX}{name.upper()}'

