# test_data_example.py
# Simple test data to learn Algorithm 1

import numpy as np
import sys
sys.path.append('testmdp')

# Create simple synthetic data
def create_simple_test_data():
    """
    Create simple test data that follows the format expected by Dr. Shi's algorithm
    Returns: list of trajectories, each trajectory is [X, A]
    where X = states, A = actions
    """
    
    # Example 1: Longer trajectories for more stable results
    np.random.seed(42)  # For reproducible results
    
    # Create longer trajectories (20 time steps each)
    trajectory1 = [
        np.random.randint(0, 3, size=(20, 1)).astype(float),  # X: 3 possible states
        np.random.randint(0, 2, size=(20, 1)).astype(float)   # A: 2 possible actions
    ]
    
    trajectory2 = [
        np.random.randint(0, 3, size=(20, 1)).astype(float),  # X: states over time  
        np.random.randint(0, 2, size=(20, 1)).astype(float)   # A: actions over time
    ]
    
    trajectory3 = [
        np.random.randint(0, 3, size=(20, 1)).astype(float),  # X: states over time
        np.random.randint(0, 2, size=(20, 1)).astype(float)   # A: actions over time
    ]
    
    trajectory4 = [
        np.random.randint(0, 3, size=(20, 1)).astype(float),
        np.random.randint(0, 2, size=(20, 1)).astype(float)
    ]
    
    trajectory5 = [
        np.random.randint(0, 3, size=(20, 1)).astype(float),
        np.random.randint(0, 2, size=(20, 1)).astype(float)
    ]
    
    # Return list of trajectories
    data = [trajectory1, trajectory2, trajectory3, trajectory4, trajectory5]
    return data

# Test the algorithm
def test_algorithm_1():
    """Test Algorithm 1 with our simple data"""
    
    # Import the testing function
    try:
        from _core_test_fun import test
        print("✓ Successfully imported test function")
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return
    
    # Create test data
    data = create_simple_test_data()
    print(f"✓ Created {len(data)} test trajectories")
    
    # Print data structure to understand format
    print("\nData structure:")
    for i, traj in enumerate(data):
        print(f"  Trajectory {i+1}:")
        print(f"    States (X): {traj[0].flatten()}")  # flatten for easy reading
        print(f"    Actions (A): {traj[1].flatten()}")
    
    # Run Algorithm 1
    print("\n--- Running Algorithm 1 ---")
    try:
        result = test(data=data, J=1)  # J=1 means test for 1st order Markov property
        print(f"✓ Algorithm completed!")
        print(f"p-value: {result}")
        
        # Interpret result
        if result < 0.05:
            print("→ Data does NOT satisfy Markov property (p < 0.05)")
        else:
            print("→ Data appears to satisfy Markov property (p ≥ 0.05)")
            
    except Exception as e:
        print(f"✗ Algorithm failed: {e}")

if __name__ == "__main__":
    test_algorithm_1()