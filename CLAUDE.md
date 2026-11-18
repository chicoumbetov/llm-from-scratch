# Project Guidelines for Cline / Claude

## System & Tech Stack
- **Language**: Python 3.11+, JavaScript (ES6+ HTML/CSS UI)
- **ML Libraries**: PyTorch, NumPy, Tiktoken
- **Backend**: FastAPI, Uvicorn, Pydantic
- **Testing**: pytest
- **Deployment**: Docker, Hugging Face Spaces / GitHub Actions

## Code Style & Rules
1. **First Principles First**: Do not rely on high-level PyTorch abstractions in `01_micrograd` and initial `makemore` modules. Keep math explicit.
2. **Type Hints & Docstrings**: All public functions and classes must include Python type annotations and short docstrings.
3. **Unit Tests Required**: Every newly created engine component must have a corresponding test file in `tests/` verifying output against PyTorch standard outputs.
4. **No Unrequested Dependencies**: Do not add extra libraries to `requirements.txt` unless explicitly instructed in a Phase document.
5. **Clean Architecture**: Keep ML core engines (`engine.py`, `nn.py`, `model.py`) independent from Web API wrappers (`app/main.py`).

## Workflow Execution
- Read the active phase spec (`phase-XX.md`) before writing code.
- Implement step-by-step; run `pytest` after completing each module.
- Do not skip steps or modify existing phase requirements.
- Write history of executed steps in docs/history.md
