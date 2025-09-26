from transformers import pipeline

class AIManager:
    def __init__(self):
        # Test model
        self.generator = pipeline("text-generation", model="distilgpt2")

    def generate_text(self, prompt: str) -> str:
        result = self.generator(prompt, max_length=50, num_return_sequences=1)

        return result[0]["generated_text"]