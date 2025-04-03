import os
import shutil
import subprocess

# Set paths
notebooks_dir = os.path.abspath("..")  # assume running from 'notebooks/tools'
backup_dir = os.path.join(notebooks_dir, "backup")

print("📘 Restoring all notebooks from /backup to notebooks directory...\n")

# Check backup folder exists
if not os.path.exists(backup_dir):
    print("❌ Backup directory not found.")
    exit(1)

# Track which files were replaced
replaced = []

# Copy each .ipynb file from backup to notebooks_dir
for file_name in os.listdir(backup_dir):
    if file_name.endswith(".ipynb"):
        src = os.path.join(backup_dir, file_name)
        dst = os.path.join(notebooks_dir, file_name)
        shutil.copy2(src, dst)
        replaced.append(file_name)
        print(f"✅ Restored: {file_name}")

# Stage and push changes using Git
try:
    subprocess.run(["git", "-C", notebooks_dir, "add", "*.ipynb"], check=True, shell=True)
    subprocess.run(["git", "-C", notebooks_dir, "commit", "-m", "Restore notebooks from backup using Python script"], check=True)
    subprocess.run(["git", "-C", notebooks_dir, "push"], check=True)
    print("\n🚀 Notebooks pushed to remote.")
except subprocess.CalledProcessError as e:
    print(f"\n⚠️ Git command failed: {e}")

print("\n🧹 Done. You can now remove the backup folder if it's no longer needed.")
