from src.client import get_client
from src.collection import get_or_create_collection, add_collection, find_closest_texts
from src.data import get_data
import logging

logging.basicConfig(
  level=logging.INFO,
  filename='src.log',
  filemode='a',
  format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("Package is initialized")


__version__ = "1.0.0"
__date__ = "22-07-2024"
__email__ = "kivancgordu@hotmail.com"
__status__ = "production"

__all__ = [
  'get_client', 'get_or_create_collection', 'add_collection', 'find_closest_texts', 'get_data'
]
