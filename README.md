# python_ai
Python AI Code


## venv with uv


```bash
curl -LsSf https://astral.sh/uv/install.sh | sh 

uv init
uv venv
uv add -r requirements.txt
uv add openai
uv run main.py
uv run --env-file ../.env simple01.py 


source .venv/bin/activate
python simple01.py
```

## Referencias
https://github.com/openai/openai-agents-python?tab=readme-ov-file