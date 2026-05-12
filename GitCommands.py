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

# 12. git diff - Show changes between commits, branches, or the working directory
# command: git diff - shows the differences between the working directory and the staging area.
# git diff <branch1> <branch2> - shows the differences between two branches.

# 13. git reset - Unstage changes or revert commits
# command: git reset <file_name> - unstages the specified file, moving it back to the working directory.
# git reset --hard <commit_hash> - resets the current branch to the specified commit, discarding all changes after that commit.

# 14. git restore --staged <file_name> - Unstage a file
# command: git restore --staged <file_name> - unstages the specified file, moving it back to the working directory without discarding changes.

# 15. git stash - Temporarily save changes that are not ready to be committed
# command: git stash - saves the current changes in a temporary area, allowing you to switch branches or work on 
# something else without committing the changes.

# 16. git stash apply - Apply stashed changes
# command: git stash apply - applies the most recently stashed changes to the current working directory, allowing you to continue working on them.

# 17. git remote - Manage remote repositories
# command: git remote add <remote_name> <repository_url> - adds a new remote repository with the specified name and URL.
# git remote -v - lists the configured remote repositories and their URLs.

# 18. git fetch - Fetch changes from a remote repository
# command: git fetch origin - retrieves the latest changes from the remote repository without merging them into the current branch.

# 19. git tag - Create and manage tags
# command: git tag <tag_name> - creates a new tag with the specified name, 
# which can be used to mark specific points in the commit history, such as releases or milestones.

# 20 git blame <file_name> - Show who made changes to a file
# command: git blame <file_name> - shows the commit history for each line of the specified file, indicating who made changes to each line and when they were made. This can be useful 
# for tracking down the origin of specific changes or understanding the history of a file.

# 21. git reflog - View the history of branch changes
# command: git reflog - shows a log of all the changes made to the branches in the repository, including commits, merges, and resets. This can be useful for recovering lost commits or

# 22. git rm - Remove files from the repository
# command: git rm <file_name> - removes the specified file from the staging area and the working directory, effectively deleting it from the repository. If you want to keep the file in the