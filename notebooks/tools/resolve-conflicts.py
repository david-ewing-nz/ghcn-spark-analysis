import subprocess
import os

def get_conflicted_notebooks():
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=U"],
            stdout=subprocess.PIPE,
            check=True,
            text=True
        )
        files = result.stdout.strip().split("\n")
        return [f for f in files if f.endswith(".ipynb")]
    except subprocess.CalledProcessError:
        print("❌ Failed to detect conflicted notebooks.")
        return []

def resolve_conflict(file):
    print(f"⚠️ Merge conflict in: {file}")
    print("Choose how to resolve:")
    print("[1] Keep YOUR version (local)")
    print("[2] Keep REMOTE version (incoming)")
    print("[3] Skip this file")
    choice = input("Enter choice [1/2/3]: ").strip()

    if choice == "1":
        subprocess.run(["git", "checkout", "--ours", file], check=False)
        subprocess.run(["git", "add", file], check=False)
        print("✅ Kept local version")
    elif choice == "2":
        subprocess.run(["git", "checkout", "--theirs", file], check=False)
        subprocess.run(["git", "add", file], check=False)
        print("✅ Kept remote version")
    else:
        print("⏭️ Skipped")

def main():
    conflicted = get_conflicted_notebooks()
    if not conflicted:
        print("✅ No conflicted notebooks found.")
        return

    for file in conflicted:
        print()
        resolve_conflict(file)

    commit = input("\nDo you want to commit resolved files now? (y/n): ").strip().lower()
    if commit == "y":
        subprocess.run(["git", "commit", "-m", "Resolve notebook conflicts via Python script"], check=False)
        print("✅ Commit complete.")
    else:
        print("📌 Skipped commit. You can commit manually later.")

if __name__ == "__main__":
    main()
