import pytest
from unittest.mock import MagicMock, patch

from ai.base_adapter import BaseAIAdapter
from ai.ai_manager import AIManager


class DummyGenerator:
    def __init__(self):
        self.calls = []

    def __call__(self, prompt, **kwargs):
        self.calls.append((prompt, kwargs))
        return [{"generated_text": f"Echo: {prompt}"}]


def test_generate_text_with_custom_generator():
    dummy = DummyGenerator()
    adapter = BaseAIAdapter(generator=dummy)

    output = adapter.generate_text("Hello", max_length=20, temperature=0.7)

    assert output == "Echo: Hello"
    assert dummy.calls == [("Hello", {"max_length": 20, "num_return_sequences": 1, "temperature": 0.7})]


def test_generate_text_raises_runtime_error_on_failure():
    class FailingGenerator:
        def __call__(self, *_args, **_kwargs):
            raise ValueError("boom")

    adapter = BaseAIAdapter(generator=FailingGenerator())

    with pytest.raises(RuntimeError) as exc:
        adapter.generate_text("Hello")

    assert "Text generation failed" in str(exc.value)


def test_ai_manager_initializes_transformers_pipeline():
    mock_generator = MagicMock()
    mock_generator.return_value = [{"generated_text": "Model output"}]

    with patch("transformers.pipeline", return_value=mock_generator) as pipeline_mock:
        manager = AIManager(model_name="distilgpt2")

    pipeline_mock.assert_called_once_with("text-generation", model="distilgpt2")

    result = manager.generate_text("Prompt")
    assert result == "Model output"

    mock_generator.assert_called_once_with("Prompt", max_length=50, num_return_sequences=1)
