from llama_cpp import Llama
from .base_adapter import BaseAdapter

class LlamaCppAdapter(BaseAdapter):
    def __init__(self, model_path: str = "./models/llama-7b.gguf"):
        # Modell laden
        self.llm = Llama(
            model_path=model_path,
            n_ctx=2048, # Context length (token)
            n_threads=8, # CPU-Threads
            n_gpu_layers=0 # Deactivate GPU usage
        )

    def send_message(self, prompt: str):
        """
        Inputs a prompt (string) and sends it to the model.
        """

        stream = self.llm(prompt, stream=True) # stream=True -> Token-by-Token Output

        for token in stream:
            text = token['choices'][0]['text']
            yield text