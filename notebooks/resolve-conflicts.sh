#!/bin/bash

echo "📘 Resolving Jupyter notebook merge conflicts..."

conflicted_files=$(git diff --name-only --diff-filter=U | grep '\.ipynb')

if [ -z "$conflicted_files" ]; then
    echo "✅ No conflicted notebooks found!"
    exit 0
fi

for file in $conflicted_files; do
    echo ""
    echo "⚠️ Conflict in: $file"
    echo "Choose how to resolve:"
    echo "[1] Keep YOUR version"
    echo "[2] Keep REMOTE version"
    echo "[3] Skip for now"
    read -p "Enter choice [1/2/3]: " choice

    case $choice in
        1)
            echo "✅ Keeping YOUR version of $file"
            git checkout --ours "$file"
            git add "$file"
            ;;
        2)
            echo "✅ Keeping REMOTE version of $file"
            git checkout --theirs "$file"
            git add "$file"
            ;;
        3)
            echo "⏭️  Skipping $file for now"
            ;;
        *)
            echo "❌ Invalid choice. Skipping $file."
            ;;
    esac
done

echo ""
read -p "Do you want to commit resolved files now? (y/n): " commit_confirm
if [ "$commit_confirm" == "y" ]; then
    git commit -m "Resolve notebook conflicts via script"
    echo "✅ Commit complete."
else
    echo "📌 Skipped commit. You can run 'git commit' manually later."
fi
