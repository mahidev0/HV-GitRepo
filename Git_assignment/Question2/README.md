# Question 2: Working with Changes & History

## Objective
Track code changes and manage commit history properly.

---

## Tasks Performed

- Modified app.py with new functionality
- Checked file changes
- Viewed differences
- Staged changes
- Created commits
- Viewed commit history

---

## Commands Used

```bash
git status

git diff

git add app.py

git commit -m "Added add function"

git add .

git commit -m "Added multiply function"

git log

git log --oneline
```

---

## app.py Example

```python
print("Welcome to Git Assignment")

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(add(10, 20))
print(multiply(5, 4))
```

---

## Outcome
-<img width="940" height="367" alt="image" src="https://github.com/user-attachments/assets/dead20b9-37b4-4ccf-b586-b5ce97358304" />
-<img width="940" height="440" alt="image" src="https://github.com/user-attachments/assets/eea42f30-30b5-49f8-824a-017d6c7d2111" />
-<img width="940" height="440" alt="image" src="https://github.com/user-attachments/assets/946661e2-fc7d-43b6-b38a-c9b767352362" />



Successfully tracked file changes and managed commit history using Git.
