# Project structure

llm-from-scratch/ 
├── README.md # Общий обзор репозитория, стек, цели и результаты 
├── requirements.txt # Зависимости (torch, numpy, matplotlib, graphviz, tiktoken) 
├── .gitignore
│
├── 01\_micrograd/ # Урок 1: Скалярный autograd движок 
│   ├── README.md # Краткий конспект теорбазы урока
│   ├── engine.py # Класс Value и математика градиентов
│   ├── nn.py # Neuron, Layer, MLP
│   ├── demo.ipynb # Ноутбук с визуализацией графа и обучением
│   └── tests/ # Unit-тесты (сравнение результатов с PyTorch)
│       └── test\_engine.py
│
├── 02\_makemore\_bigram/ # Урок 2: Bigram модель и матрицы смежности
│   ├── README.md
│   └── bigram.ipynb
│
├── 03\_makemore\_mlp/ # Урок 3: MLP по архитектуре Bengio et al.
│   ├── README.md
│   └── mlp.py
│
├── 04\_makemore\_backprop\_ninja/# Урок 4 и 5: BatchNorm, активации, manual backprop 
│   ├── README.md
│   └── backprop\_ninja.ipynb
│
├── 05\_wavenet/ # Урок 6: WaveNet архитектура
│   ├── README.md
│   └── wavenet.py
│
├── 06\_gpt/ # Урок 7: NanoGPT с нуля
│   ├── README.md
│   ├── model.py # Self-Attention, Multi-Head Attention, Transformer Block
│   ├── train.py # Скрипт обучения и валидации
│   └── sample.py # Скрипт генерации текста
│
├── 07\_tokenizer/ # Урок 8: BPE Tokenizer с нуля
│   ├── README.md
│   └── bpe\_tokenizer.py
│
└── app/ # Веб-демо для демонстрации (Fullstack + AI)
    ├── main.py # FastAPI или Streamlit приложение
    └──Dockerfile