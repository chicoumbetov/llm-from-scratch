# Phase 2: Makemore Language Models & Tensor Foundations

## Objective
Transition from scalar operations to PyTorch tensor computations by implementing character-level language models (Bigram, MLP Bengio et al., BatchNorm, Backprop Ninja, WaveNet).

## Deliverables
- `02_makemore_bigram/bigram.py`: Count-based matrix and single-layer neural net character predictor.
- `03_makemore_mlp/mlp.py`: Multilayer Perceptron with word/character embeddings.
- `04_makemore_backprop_ninja/manual_backprop.py`: Manual analytical derivative calculation for Cross-Entropy loss and BatchNorm without `.backward()`.
- `05_wavenet/wavenet.py`: Hierarchical dilated convolutional neural network architecture.

## Acceptance Criteria
1. Cross-Entropy loss implementation matches `torch.nn.functional.cross_entropy`.
2. Manual backward pass in `manual_backprop.py` matches PyTorch autograd gradients within `1e-6` tolerance.
3. Training loss curves logged and saved as plots in each module directory.
