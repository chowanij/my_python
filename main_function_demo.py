#!/usr/bin/env python3
"""
Main Function Demo - Understanding Python Script Entry Points

This script demonstrates how to use the main function pattern in Python
and explains what a script entrypoint is.
"""

import sys
import os


def greet_user(name="World"):
    """A simple function that greets a user."""
    return f"Hello, {name}!"


def calculate_sum(a, b):
    """A function that calculates the sum of two numbers."""
    return a + b


def main():
    """
    Main function - the entry point of our script.
    
    This function contains the main logic that should run when the script
    is executed directly (not when imported as a module).
    """
    print("=" * 50)
    print("Python Main Function Demo")
    print("=" * 50)
    
    # Get command line arguments
    args = sys.argv[1:]  # Skip the script name itself
    
    if args:
        name = args[0]
        print(greet_user(name))
    else:
        print(greet_user())
    
    # Demonstrate some calculations
    print(f"\nSome calculations:")
    print(f"5 + 3 = {calculate_sum(5, 3)}")
    print(f"10 + 20 = {calculate_sum(10, 20)}")
    
    # Show current working directory
    print(f"\nCurrent working directory: {os.getcwd()}")
    print(f"Script location: {os.path.abspath(__file__)}")


if __name__ == "__main__":
    """
    This is the Python script entrypoint pattern.
    
    The special variable __name__ is set by Python:
    - When a script is run directly: __name__ == "__main__"
    - When a script is imported as a module: __name__ == "module_name"
    
    This allows the same file to be used both as:
    1. A standalone script (when run directly)
    2. A module (when imported by other scripts)
    """
    main()


