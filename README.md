# Python Main Function and Script Entry Points

This directory contains examples demonstrating how to use the main function pattern in Python scripts and understand script entrypoints.

## Files

- `main_function_demo.py` - Main demonstration script
- `import_demo.py` - Shows how to import and use functions from the main script
- `README.md` - This explanation file

## Understanding Python Script Entry Points

### What is a Script Entry Point?

A **script entry point** is the point where your Python program starts executing when you run it. In Python, this is typically the `main()` function that gets called when `if __name__ == "__main__":` is true.

### The `if __name__ == "__main__":` Pattern

This is the standard Python idiom for making a file both:
1. **Executable as a script** (when run directly)
2. **Importable as a module** (when imported by other scripts)

```python
if __name__ == "__main__":
    main()
```

### How `__name__` Works

- When you run a script directly: `__name__ == "__main__"`
- When you import a script as a module: `__name__ == "module_name"`

## How to Use These Scripts

### 1. Run the Main Demo Script

```bash
# Run with default behavior
python3 main_function_demo.py

# Run with command line arguments
python3 main_function_demo.py "Your Name"
```

### 2. Run the Import Demo Script

```bash
python3 import_demo.py
```

### 3. Import Functions in Python Interactive Mode

```python
# Start Python interactive mode
python3

# Import and use functions
from main_function_demo import greet_user, calculate_sum
print(greet_user("Python User"))
print(calculate_sum(15, 25))
```

## Key Concepts Explained

### 1. Main Function
- Contains the primary logic of your script
- Only runs when the script is executed directly
- Allows for clean organization of code

### 2. Command Line Arguments
- Access via `sys.argv[1:]` (skip `sys.argv[0]` which is the script name)
- Allows scripts to accept parameters when run

### 3. Module vs Script
- **As a script**: Run directly with `python3 filename.py`
- **As a module**: Import functions with `from filename import function_name`

### 4. Shebang Line
```python
#!/usr/bin/env python3
```
- Makes the script executable directly (with `chmod +x`)
- Specifies which Python interpreter to use

## Best Practices

1. **Always use the `if __name__ == "__main__":` pattern** for scripts that might be imported
2. **Put main logic in a `main()` function** for better organization
3. **Use command line arguments** for user input when appropriate
4. **Add docstrings** to explain what your functions do
5. **Handle errors gracefully** in your main function

## Example Usage Scenarios

### Scenario 1: Standalone Script
```bash
python3 main_function_demo.py "Alice"
# Output: Hello, Alice!
```

### Scenario 2: Imported Module
```python
from main_function_demo import calculate_sum
result = calculate_sum(10, 20)  # result = 30
```

### Scenario 3: Making Script Executable
```bash
chmod +x main_function_demo.py
./main_function_demo.py "Bob"
```

This pattern is fundamental to Python development and is used in virtually every Python project!
