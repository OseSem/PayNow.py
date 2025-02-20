import logging
from typing import Final

__version__: Final[str] = "0.1.0"

logging.getLogger(__name__).addHandler(logging.NullHandler())