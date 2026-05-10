# CalculatorPlus Application

## Objective

Implement a Python calculator application using Git branching workflow, feature development, bug fixing, pull requests, and release management.

---

# Features

- Addition
- Subtraction
- Multiplication
- Division
- Square Root

---

# Repository Structure

```text
git_assignment_HeroVired/
│
├── app.py
├── README.md
│
├── branches
│   ├── main
│   ├── dev
│   ├── feature/sqrt
│   
```

---

# Branch Workflow

## main
Production-ready stable code.

## dev
Development branch for testing and integration.

## feature/sqrt
Feature branch for square root implementation.

---

# Initial Calculator Code

```python
import math

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def square_root(self, x):
        return math.sqrt(x)

if __name__ == "__main__":

    calculator = Calculator()

    num1 = 16
    num2 = 4

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    num3 = 25

    print(f"The square root of {num3} = {calculator.square_root(num3)}")
```

---

# Git Workflow Used

## Create dev branch

```bash
git checkout -b dev
```

---

## Create feature branch

```bash
git checkout -b feature/sqrt
```

---

## Merge feature branch into dev

```bash
git checkout dev
git merge feature/sqrt
```

---

## Merge dev into main

```bash
git checkout main
git merge dev
```

---

# Bug Fix Applied

Handled divide-by-zero exception:

```python
def divide(self, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
```

---

# Releases

## Version 1 (v1.0)

- Basic calculator operations
- add
- subtract
- multiply
- divide

---

## Version 2 (v2.0)

- Added square root feature
- Added divide-by-zero bug fix
- Feature branch merge completed

---

# Testing

Run application:

```bash
python app.py
```

Expected Output:

```text
16 + 4 = 20
16 - 4 = 12
16 * 4 = 64
16 / 4 = 4.0
The square root of 25 = 5.0
```

---

# Important Git Commands

| Task | Command |
|------|----------|
| Create branch | git checkout -b branch-name |
| Switch branch | git checkout branch-name |
| Merge branch | git merge branch-name |
| Push branch | git push origin branch-name |
| View branches | git branch |

---

# Outcome

Successfully implemented:

- Git branching strategy
- Feature development
- Bug fixing workflow
- Pull request workflow
- Release management
- Git LFS integration

This project demonstrates a real-world DevOps and collaborative Git workflow.
