import pytest
import torch
from app.main import ScalarValue


def test_micrograd_vs_pytorch_forward_and_backward():
    """
    Tests whether the forward and backward passes
    of our ScalarValue (Micrograd) and PyTorch autograd produce exactly the same results.
    """
    # -------------------------------------------------------------------------
    # 1. Calculations in Micrograd
    # -------------------------------------------------------------------------
    a_mg = ScalarValue(-4.0)
    b_mg = ScalarValue(2.0)

    # L = (a * b) + (a * 2)
    c_mg = a_mg * b_mg
    d_mg = a_mg * 2.0
    L_mg = c_mg + d_mg

    L_mg.backward()

    # -------------------------------------------------------------------------
    # 2. Calculations in PyTorch
    # -------------------------------------------------------------------------
    a_pt = torch.tensor([-4.0], dtype=torch.float64, requires_grad=True)
    b_pt = torch.tensor([2.0], dtype=torch.float64, requires_grad=True)

    c_pt = a_pt * b_pt
    d_pt = a_pt * 2.0
    L_pt = c_pt + d_pt

    L_pt.backward()

    # -------------------------------------------------------------------------
    # 3. Results match verification
    # -------------------------------------------------------------------------
    # Forward pass match
    assert L_mg.data == pytest.approx(L_pt.item(), abs=1e-6)

    # Backward pass gradients match
    assert a_mg.grad == pytest.approx(a_pt.grad.item(), abs=1e-6)
    assert b_mg.grad == pytest.approx(b_pt.grad.item(), abs=1e-6)


def test_zero_grad_behavior():
    """
    Checks the correctness of repeated computations and whether `zero_grad` is necessary.
    """
    x = ScalarValue(3.0)
    y = x * x
    y.backward()
    grad_first_run = x.grad  # 2 * 3 = 6.0

    assert grad_first_run == pytest.approx(6.0)

    # A repeated backward pass without resetting should accumulate a gradient of (6.0 + 6.0 = 12.0)
    y.backward()
    assert x.grad == pytest.approx(12.0)

    # Manual Reset (zero_grad)
    x.grad = 0.0
    y.backward()
    assert x.grad == pytest.approx(6.0)
