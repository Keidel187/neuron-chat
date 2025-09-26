from transformers import pipeline
import logging

class AIManager:
    def __init__(self):
        # Testmodel
        try:
            self.generator = pipeline("text-generation", model="distilgpt2")
        except Exception as e:
            logging.error(f"Failed to load text-generation pipeline: {e}")
            raise RuntimeError(f"Failed to initialize AIManager: {e}")

    def generate_text(self, prompt: str) -> str:
        try:
            result = self.generator(prompt, max_length=50, num_return_sequences=1)
            return result[0]["generated_text"]
        except Exception as e:
            logging.error(f"Text generation failed for prompt '{prompt}': {e}")
            raise RuntimeError(f"Text generation failed: {e}")