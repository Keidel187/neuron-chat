from transformers import pipeline
import logging
from .base_adapter import BaseAIAdapter

class AIManager(BaseAIAdapter):
    def __init__(self, model_name: str = "distilgpt2"):
        try:
            super().__init__(model_name=model_name)
        
        except Exception as e:
            logging.error(f"Failed to initialize AIManager: {e}")
            raise RuntimeError(f"Failed to initialize AIManager: {e}")