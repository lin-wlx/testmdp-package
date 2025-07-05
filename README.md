# testmdp-package

A Python implementation of statistical tests for the Markov property in sequential decision-making data, based on the research by Shi et al.

## Overview

This package implements Algorithm 1 from the paper **"Does the Markov Decision Process Fit the Data: Testing for the Markov Property in Sequential Decision Making"** (ICML 2020).

## Features

- **Markov Property Testing**: Statistical test to determine if your data follows the Markov assumption
- **Random Forest-Based**: Uses quantile regression forests for robust conditional characteristic function estimation
- **Easy-to-Use Interface**: Simple API for testing your own sequential decision data
- **Cross-Platform**: Compatible with Windows (originally mac?)

## Installation

### Option 1: Using Conda (Recommended)

```bash
# Create environment from the provided file
conda env create --file TestMDP.yml

# Activate the environment
conda activate TestMDP
```

### Option 2: Using pip

```bash
# Install required packages
pip install -r requirements_windows.txt
```

**Required packages:**
- scikit-learn==0.23.1
- scipy==1.2.1
- numpy==1.18.5
- statsmodels==0.11.1
- pandas==1.0.4
- joblib==0.15.1

## Quick Start

```python
import sys
sys.path.append('testmdp')
from _core_test_fun import test
import numpy as np

# Prepare your data as a list of trajectories
# Each trajectory is [X, A] where:
# X = states over time (T x state_dim array)
# A = actions over time (T x action_dim array)

trajectory1 = [
    np.array([[0], [1], [0], [1], [0]]),  # States
    np.array([[1], [0], [1], [0], [1]])   # Actions
]

trajectory2 = [
    np.array([[1], [0], [0], [1], [1]]),  # States
    np.array([[0], [1], [1], [0], [0]])   # Actions
]

data = [trajectory1, trajectory2]

# Test for 1st-order Markov property
p_value = test(data=data, J=1)

print(f"p-value: {p_value}")
if p_value < 0.05:
    print("→ Data does NOT satisfy Markov property (p < 0.05)")
else:
    print("→ Data appears to satisfy Markov property (p ≥ 0.05)")
```

## Data Format

Your data should be organised as:

```python
data = [trajectory1, trajectory2, ..., trajectoryN]
```

Where each trajectory is:
```python
trajectory = [X, A]
# X: numpy array of shape (T, state_dimensions)
# A: numpy array of shape (T, action_dimensions)
# T: number of time steps in the trajectory
```

## Examples

See the `examples/` folder for detailed usage examples:

- `test_data_example.py`: Basic usage with synthetic data
- `test_basic.py`: Simple import and functionality test

Run the basic functionality test:

```bash
python test_basic.py
```

Run the example with synthetic data:

```bash
python examples/test_data_example.py
```

## Project Structure

```
testmdp-package/
├── README.md                 # This file
├── requirements_windows.txt  # Python dependencies
├── TestMDP.yml              # Conda environment specification
├── testmdp/                 # Main package
│   ├── _core_test_fun.py   # Core testing algorithms
│   ├── _QRF.py             # Quantile regression forest implementation
│   ├── _uti_basic.py       # Basic utilities
│   └── _utility.py         # Additional utility functions
├── examples/               # Usage examples
│   └── test_data_example.py
└── test_basic.py          # Basic functionality test
```

## Citation

If you use this package in your research, please cite the original paper:

```bibtex
@inproceedings{shi2020markov,
  title={Does the Markov Decision Process Fit the Data: Testing for the Markov Property in Sequential Decision Making},
  author={Shi, Chengchun and Wan, Runzhe and Song, Rui and Lu, Wenbin and Leng, Ling},
  booktitle={International Conference on Machine Learning},
  pages={8807--8817},
  year={2020},
  organization={PMLR}
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Issues and Support

If you encounter any issues or have questions:

1. Check the examples in the `examples/` folder
2. Ensure you're using the correct package versions (see requirements)
3. Open an issue on GitHub with a detailed description

## Acknowledgments

- Original algorithm and research by Shi, Chengchun et al.
- Random forest implementation adapted from scikit-garden
- Thanks to the scikit-learn and scipy communities

## Version History

- **v1.0.0**: Initial release with working Algorithm 1 implementation
- Compatible with Python 3.6+ and scikit-learn 0.23.1

---

**Note**: This implementation has been tested and verified to work with the specified package versions. For best results, use the provided conda environment or exact package versions listed in requirements.
