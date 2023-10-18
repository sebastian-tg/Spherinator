import os
import sys
import torch

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(script_dir, '../external/power_spherical/'))
from power_spherical import PowerSpherical


def test_power_spherical_2d():
    torch.manual_seed(0)
    dist = PowerSpherical(torch.Tensor([0.0, 0.0]), torch.Tensor([1.0]))

    assert dist.has_rsample == True
    sample = dist.rsample()
    assert sample.shape == torch.Size([2])
    assert torch.isclose(sample, torch.Tensor([-0.9971,  0.0766]), rtol = 1e-3).all()
    assert torch.isclose(dist.rsample(), torch.Tensor([-0.5954,  0.8034]), rtol = 1e-3).all()

def test_power_spherical_2d_batch():
    torch.manual_seed(0)
    batch_size = 32
    loc = torch.randn(batch_size, 3)
    scale = torch.ones(batch_size)
    dist = PowerSpherical(loc, scale)

    sample = dist.rsample()
    assert sample.shape == torch.Size([batch_size, 3])
