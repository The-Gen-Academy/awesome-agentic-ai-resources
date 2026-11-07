# YouTube notebooks

## LangChain-LangGraph-101

[Open the illustrated notebook](./LangChain-LangGraph-101.ipynb).

A walkthrough of prompt templates, chat models, LCEL chains, structured output,
tool calling, LangGraph workflows, and agents with in-memory conversation state.
The notebook includes nine explanatory diagrams and the two original illustrations.

### Run locally

From `YT-notebooks`, with [uv](https://docs.astral.sh/uv/) installed:

```bash
uv sync --locked
cp .env.example .env
```

Set `OPENAI_API_KEY` in `.env`, then launch:

```bash
uv run jupyter lab LangChain-LangGraph-101.ipynb
```

Select the project Python environment and run cells in order. Keep `prompts.py`
and `notebook_images` beside the notebook. Model calls use your OpenAI account
and may incur charges. `.env` is ignored by Git; do not commit your key.

`OPENAI_MODEL` optionally overrides the notebook's default model. Agent memory
uses `InMemorySaver` and is lost when the Python process restarts.

The original 12 code cells are unchanged. See [LICENSE](./LICENSE).
