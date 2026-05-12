# Basic Git Commands

# 1. git init - Initialize a new Git repository
# command: git init

# 2. git status - Check the status of the repository
# command: git status
# shows the current state of the repository, including staged, unstaged, and untracked files.

# 3. git add - Add files to the staging area
# command: git add <file_name> - adds the specified file to the staging area, preparing it for a commit.
# git add . - adds all changes in the current directory to the staging area.

# working directory -> staging area -> repository
# staging area ->working directory 

# 4. git commit - Commit changes to the repository
# command: git commit -m "commit message" - commits the staged changes to the repository with a descriptive message.

# 5. git branch <branch_name> - Create a new branch
# command: git branch <branch_name> - creates a new branch with the specified name.

# 6. git checkout <branch_name> - Switch to a different branch
# command: git checkout <branch_name> - switches to the specified branch, allowing you to work on it.

# 7. git merge <branch_name> - Merge a branch into the current branch
# command: git merge <branch_name> - merges the specified branch into the current branch, combining their changes.

# 8. git push - Push changes to a remote repository
# command: git push origin <branch_name> - pushes the committed changes from the local branch 
# to the remote repository on the specified branch.

# 9. git pull - Pull changes from a remote repository
# command: git pull origin <branch_name> - pulls the latest changes from the specified branch of the remote repository and 
# merges them into the current branch.

# 10. git clone - Clone a remote repository
# command: git clone <repository_url> - creates a local copy of the remote repository specified by the URL,
# allowing you to work on it locally.

# 11. git log - View commit history
# command: git log - displays a list of commits in the current branch, showing the commit message, author, and date for each commit.
