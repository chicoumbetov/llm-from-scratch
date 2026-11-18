# Phase 1: Micrograd Engine & Test Suite

## Objective
Implement a scalar-valued automatic differentiation engine (`Value`) and basic neural network layers (`Neuron`, `Layer`, `MLP`) from scratch on pure Python, verified with unit tests against PyTorch.

## Deliverables
- `01_micrograd/engine.py`: Scalar autograd class with graph visualization capability.
- `01_micrograd/nn.py`: Modular neural network building blocks (`Neuron`, `Layer`, `MLP`).
- `01_micrograd/tests/test_engine.py`: Pytest suite verifying forward and backward passes against PyTorch.
- `01_micrograd/demo.ipynb`: Interactive Jupyter Notebook showing binary classification training.

## Acceptance Criteria
1. `engine.py` supports operations: `+`, `*`, `**`, `tanh`, `relu`, `exp`.
2. Topological sort correctly handles complex DAG (Directed Acyclic Graphs).
3. `pytest 01_micrograd/tests/` passes with 100% accuracy matching `torch.tensor` gradients to `1e-5` precision.
