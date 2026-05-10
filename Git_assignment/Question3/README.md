# Question 3: Branching & Feature Development

## Objective
Work with branches and manage feature development.

---

## Tasks Performed

- Created feature branch
- Switched branches
- Added new feature code
- Committed changes
- Merged feature branch into main branch
- Verified merge
- Deleted branches safely
- Performed force delete on dummy branch

---

## Commands Used

```bash
git branch feature-update

git checkout feature-update

git add .

git commit -m "Added login feature"

git checkout master

git merge feature-update

git branch -d feature-update

git branch dummy-branch

git branch -D dummy-branch
```

---

## app.py Example

```python
print("Feature branch update")

def login(username):
    return f"Welcome {username}"

print(login("Mahi"))
```

---

## Outcome

Successfully worked with Git branches and merged feature development into the main branch.