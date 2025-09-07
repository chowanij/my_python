#!/usr/bin/env python3
"""
Import Demo - Shows how to import and use functions from main_function_demo.py
"""

# Import specific functions from our demo module
from main_function_demo import greet_user, calculate_sum

def main():
    print("Using functions imported from main_function_demo.py:")
    print("-" * 50)
    
    # Use the imported functions
    print(greet_user("Alice"))
    print(greet_user("Bob"))
    
    print(f"\nCalculations using imported function:")
    print(f"100 + 200 = {calculate_sum(100, 200)}")
    print(f"7 + 8 = {calculate_sum(7, 8)}")

if __name__ == "__main__":
    main()


