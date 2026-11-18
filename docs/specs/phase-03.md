# Phase 3: NanoGPT Engine & BPE Tokenizer

## Objective
Build a complete GPT-2 / Transformer architecture from scratch in PyTorch, accompanied by a custom Byte Pair Encoding (BPE) Tokenizer.

## Deliverables
- `06_gpt/model.py`: `CausalSelfAttention`, `MultiHeadAttention`, `MLP`, `Block`, and `GPT` modules.
- `06_gpt/train.py`: Training pipeline supporting learning rate decay schedule, gradient accumulation, and evaluation loop.
- `07_tokenizer/bpe_tokenizer.py`: BPE tokenizer implementation (train, encode, decode).

## Acceptance Criteria
1. `model.py` faithfully implements GPT-2 configuration (124M parameters or miniature version).
2. Weight initialization matches GPT-2 standard norms (`std=0.02`, scaled residual projections).
3. `bpe_tokenizer.py` correctly compresses text sequences and decodes back without loss of information.
