# test_data_example.py
import numpy as np
import sys
import os


def setup_import():
    """Fix the import path issue"""
    # Check if we can find the testmdp directory
    if os.path.exists('./testmdp'):
        sys.path.insert(0, './testmdp')
        print("Added testmdp to Python path")
        return True
    elif os.path.exists('../testmdp'):
        sys.path.insert(0, '../testmdp')
        print("Added ../testmdp to Python path")
        return True
    else:
        print("Could not find testmdp directory")
        print("Current directory:", os.getcwd())
        print("Available directories:", [d for d in os.listdir('.') if os.path.isdir(d)])
        return False


def create_simple_test_data():
    np.random.seed(42)

    trajectory1 = [
        np.random.randint(0, 3, size=(20, 1)).astype(float),
        np.random.randint(0, 2, size=(20, 1)).astype(float)
    ]

    trajectory2 = [
        np.random.randint(0, 3, size=(20, 1)).astype(float),
        np.random.randint(0, 2, size=(20, 1)).astype(float)
    ]

    trajectory3 = [
        np.random.randint(0, 3, size=(20, 1)).astype(float),
        np.random.randint(0, 2, size=(20, 1)).astype(float)
    ]

    trajectory4 = [
        np.random.randint(0, 3, size=(20, 1)).astype(float),
        np.random.randint(0, 2, size=(20, 1)).astype(float)
    ]

    trajectory5 = [
        np.random.randint(0, 3, size=(20, 1)).astype(float),
        np.random.randint(0, 2, size=(20, 1)).astype(float)
    ]

    data = [trajectory1, trajectory2, trajectory3, trajectory4, trajectory5]
    return data


def test_algorithm_1():


    # Fix the import issue first
    if not setup_import():
        return

    # Now try to import
    try:
        from _core_test_fun import test
        print("Successfully imported test function")
    except ImportError as e:
        print(f"Import still failed: {e}")
        print("Files in testmdp directory:",
              os.listdir('./testmdp') if os.path.exists('./testmdp') else "Directory not found")
        return


    data = create_simple_test_data()
    print(f"✓ Created {len(data)} test trajectories")

    print("\nData structure:")
    for i, traj in enumerate(data):
        print(f"  Trajectory {i + 1}:")
        print(f"    States (X): {traj[0].flatten()}")
        print(f"    Actions (A): {traj[1].flatten()}")

    print("\n--- Running Algorithm 1 to test 1st order Markov ---")
    try:
        result = test(data=data, J=1)
        print(f"Algorithm completed!")
        print(f"p-value: {result}")

        if result < 0.05:
            print("Data does NOT satisfy Markov property (p < 0.05)")
        else:
            print("Data appears to satisfy Markov property (p ≥ 0.05)")

    except Exception as e:
        print(f"Algorithm failed: {e}")
        import traceback
        traceback.print_exc()  # This will show the full error


if __name__ == "__main__":
    test_algorithm_1()
