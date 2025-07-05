# test_basic.py
import sys
sys.path.append('testmdp')  # Tell Python to look in the testmdp folder

try:
    from _core_test_fun import test, selectOrder
    print("✓ Successfully imported the main functions!")
except ImportError as e:
    print(f"✗ Import failed: {e}")
    print("Make sure all the required files are in the testmdp folder")

# Let's also check what files we have
import os
print("\nFiles in testmdp folder:")
if os.path.exists('testmdp'):
    for file in os.listdir('testmdp'):
        print(f"  - {file}")
else:
    print("  testmdp folder not found!")