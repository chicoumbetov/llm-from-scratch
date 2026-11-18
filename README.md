# LLM from Scratch: Neural Networks Laboratory

Educational laboratory implementing foundational deep learning models from first principles, based on Andrej Karpathy's "Neural Networks: Zero to Hero" course.

## Overview
This repository bridges web engineering and deep machine learning:
- Micrograd Engine: Scalar-level automatic differentiation engine.
- Makemore Series: Language models progressing from Bigram to WaveNet.
- NanoGPT & Transformer: Full PyTorch implementation of GPT-2 style model.
- Custom BPE Tokenizer: Byte Pair Encoding tokenizer.
- Interactive API & UI: Production FastAPI backend with Docker deployment.

## Initial Repository Structure
```text
llm-from-scratch/
├── README.md                  # Main overview
├── requirements.txt           # Dependencies
├── Dockerfile                 # Container configuration
├── CLAUDE.md                  # Development instructions
├── 01_micrograd/              # Scalar Autograd Engine & MLP
├── 06_gpt/                    # NanoGPT Architecture
└── app/                       # Production API & Web Interface
```

## Interactive Parameters & Usage
1. Evaluate Autograd Graphs (Micrograd): Inputs a, b, c -> outputs gradient calculations.
2. Run Text Generation (NanoGPT): Inputs prompt, max_new_tokens, temperature, top_k -> outputs generated text stream.


# Project structure
```text
llm-from-scratch/ 
├── README.md # Общий обзор репозитория, стек, цели и результаты 
├── requirements.txt # Зависимости (torch, numpy, matplotlib, graphviz, tiktoken) 
├── .gitignore
│
├── 01_micrograd/ # Урок 1: Скалярный autograd движок 
│   ├── README.md # Краткий конспект теорбазы урока
│   ├── engine.py # Класс Value и математика градиентов
│   ├── nn.py # Neuron, Layer, MLP
│   ├── demo.ipynb # Ноутбук с визуализацией графа и обучением
│   └── tests/ # Unit-тесты (сравнение результатов с PyTorch)
│       └── test_engine.py
│
├── 02_makemore_bigram/ # Урок 2: Bigram модель и матрицы смежности
│   ├── README.md
│   └── bigram.ipynb
│
├── 03_makemore_mlp/ # Урок 3: MLP по архитектуре Bengio et al.
│   ├── README.md
│   └── mlp.py
│
├── 04_makemore_backprop_ninja/# Урок 4 и 5: BatchNorm, активации, manual backprop 
│   ├── README.md
│   └── backprop_ninja.ipynb
│
├── 05_wavenet/ # Урок 6: WaveNet архитектура
│   ├── README.md
│   └── wavenet.py
│
├── 06_gpt/ # Урок 7: NanoGPT с нуля
│   ├── README.md
│   ├── model.py # Self-Attention, Multi-Head Attention, Transformer Block
│   ├── train.py # Скрипт обучения и валидации
│   └── sample.py # Скрипт генерации текста
│
├── 07_tokenizer/ # Урок 8: BPE Tokenizer с нуля
│   ├── README.md
│   └── bpe_tokenizer.py
│
└── app/ # Веб-демо для демонстрации (Fullstack + AI)
    ├── main.py # FastAPI или Streamlit приложение
    └──Dockerfile
```

Добавляем Hugging Face как второй remote-сервер
```git remote add hf https://huggingface.co/spaces/chicoumbetov/llm-from-scratch```
Отправляем код в Hugging Face ```git push hf main --force```

# Make sure the hf CLI is installed
curl -LsSf https://hf.co/cli/install.sh | bash

# Download the Space
hf download chicoumbetov/llm-from-scratch --repo-type=space

git remote set-url hf https://chicoumbetov:HF_TOKEN@huggingface.co/spaces/chicoumbetov/llm-from-scratch
