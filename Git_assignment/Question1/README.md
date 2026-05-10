# Question 1: Project Initialization & First Push

## Objective
Set up a new Git project and push it to a remote repository.

---

## Tasks Performed

- Created a new project folder
- Initialized Git repository
- Created app.py file
- Checked Git status
- Staged files
- Committed changes
- Added remote repository
- Verified remote configuration
- Pushed code to GitHub

---

## Commands Used

```bash
mkdir Question1
cd Question1

git init

touch app.py

git status

git add .

git commit -m "Initial commit with app.py"

git remote add origin https://github.com/mahidev0/HV-GitRepo.git

git remote -v

git push -u origin master
```

---

## app.py Example

```python
print("Hello Git Project")
```

---

## Outcome

Successfully initialized a Git repository and pushed the project to GitHub.
