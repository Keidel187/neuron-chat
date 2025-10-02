import logging
from typing import Any, Optional, Callable, List, Dict

class BaseAIAdapter:
    """
    Base class that encapsulates the Hugging Face text-generation pipeline.
    Other adapters (chat, embeddings, etc.) can follow the same pattern.
    """
    def __init__(self, *, generator: Optional[Callable[..., List[Dict[str, str]]]] = None, model_name: str = "distilgpt2"):

        if generator is not None:
            self._generator = generator

        else:
            from transformers import pipeline
            try:
                self._generator = pipeline("text-generation", model=model_name)

            except Exception as e:
                logging.error(f"Failed to load model '{model_name}': {e}")
                raise RuntimeError(f"Model initialization failed: {e}")
            
    def generate_text(self, prompt: str, *, max_length: int = 50, num_return_sequences: int = 1, **kwargs) -> str:

        try:
            result = self._generator(
                prompt,
                max_length=max_length,
                num_return_sequences=num_return_sequences,
                **kwargs
            )
            if (
                isinstance(result, list)
                and len(result) > 0
                and isinstance(result[0], dict)
                and "generated_text" in result[0]
            ):
                return result[0]["generated_text"]
            else:
                logging.error(
                    f"Unexpected generator output for prompt '{prompt}': {result}"
                )
                raise RuntimeError(
                    f"Text generation failed: Unexpected generator output: {result}"
                )
        
        except Exception as e:
            logging.error(f"Generation failed for prompt '{prompt}': {e}")
            raise RuntimeError(f"Text generation failed: {e}")