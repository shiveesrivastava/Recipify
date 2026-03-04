MODEL_TYPE = "pytorch" 
CONFIDENCE_THRESHOLD = 0.65

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("recipify")