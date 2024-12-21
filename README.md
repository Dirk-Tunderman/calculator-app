# Simple Calculator

A simple calculator implementation in Python that supports basic arithmetic operations with operation history tracking.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Operation history tracking
- Input validation
- Comprehensive test suite

## Project Structure

The project is organized into the following structure:

```
calculator-app/
├── src/               # Source code
├── tests/            # Test suite
├── README.md         # This file
├── requirements.txt  # Dependencies
└── setup.py         # Package configuration
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Dirk-Tunderman/calculator-app.git
cd calculator-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from src.calculator import Calculator

# Create a calculator instance
calc = Calculator()

# Perform calculations
result = calc.calculate('+', 5, 3)  # Addition: 8
result = calc.calculate('-', 10, 4)  # Subtraction: 6
result = calc.calculate('*', 2, 3)  # Multiplication: 6
result = calc.calculate('/', 8, 2)  # Division: 4

# Get calculation history
history = calc.get_history()
for entry in history:
    print(entry)
```

## Running Tests

To run the test suite:

```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details