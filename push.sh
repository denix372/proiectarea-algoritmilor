#!/bin/bash


# Check if there are changes OR untracked files
if git diff --quiet && git diff --cached --quiet && [ -z "$(git ls-files --others --exclude-standard)" ]; then
    echo "No changes to commit."
    exit 0
fi


# Stage everything
git add .

# Check if there is at least one commit already
if git rev-parse HEAD >/dev/null 2>&1; then
    echo "Amending last commit..."
    git commit --amend --no-edit
else
    echo "Creating initial commit..."
    git commit -m "Initial commit"
fi

# Push (force-with-lease is safe)
echo "Pushing..."
git push --force-with-lease

echo "Done!"
