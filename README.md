This is my attempt at creating the famous ROCK, PAPER, SCISSORS game.


# Development Workflow

This part of the document outlines the workflow for contributing to the project.

## Branching Strategy

1. **Create a "development" branch:**
   - Developers should create a new branch named "development" from the "master" branch.
     ```bash
     git checkout -b development
     ```

2. **Pull the main project to the "development" branch:**
   - Developers should pull the latest changes from the "master" branch into their "development" branch before starting their work.
     ```bash
     git pull origin master
     ```

## Development Process

1. **Develop and make changes:**
   - Developers can make their changes, commits, and improvements on the "development" branch.

2. **Push changes to the "development" branch:**
   - After completing their work, developers should push their changes to the "development" branch on the remote repository.
     ```bash
     git push origin development
     ```

## Review and Testing

1. **Code review and testing:**
   - Reviewers conduct code reviews on the changes pushed to the "development" branch.
   - Automated and manual testing is performed on the "development" branch to ensure the changes are functional and meet requirements.

## Integration into Master

1. **Merge into "master" branch:**
   - Once the changes are approved and tested, they are merged into the "master" branch.
   - First, ensure the "development" branch is up to date with the latest changes from "master":
     ```bash
     git checkout development
     git pull origin master
     ```
   - Then, merge the changes from "development" into "master":
     ```bash
     git checkout master
     git merge development
     git push origin master
     ```

By following this workflow, we ensure that development work is isolated, reviewed, and tested before integration into the main codebase.

