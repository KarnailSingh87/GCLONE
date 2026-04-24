import os
import subprocess
from datetime import datetime, timedelta
import random

def run_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {' '.join(cmd)}: {result.stderr}")
    return result

def boost_with_backdating(total_commits=5000, days_back=365):
    print(f"🚀 Starting advanced activity boost: {total_commits} commits over {days_back} days...")
    
    start_date = datetime.now() - timedelta(days=days_back)
    
    for i in range(1, total_commits + 1):
        # Calculate a random date in the past
        random_days = random.randint(0, days_back)
        random_seconds = random.randint(0, 86400)
        commit_date = (start_date + timedelta(days=random_days, seconds=random_seconds)).strftime("%Y-%m-%d %H:%M:%S")
        
        # Ensure a change exists
        with open("activity_log.txt", "a") as f:
            f.write(f"Refactor increment {i}: {commit_date}\n")
        
        # Set environment variables for backdating
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = commit_date
        env["GIT_COMMITTER_DATE"] = commit_date
        
        # Add and Commit
        run_cmd(["git", "add", "activity_log.txt"])
        
        msg = f"refactor: optimization pass {i}"
        subprocess.run(["git", "commit", "-m", msg], env=env, capture_output=True)
        
        if i % 250 == 0:
            print(f"✅ Progress: {i}/{total_commits} commits backdated.")

    # Achievement Logic: Create a branch and merge it (Simulates Pull Shark / YOLO)
    print("\n🔥 Triggering Badge Simulations...")
    for j in range(5):
        branch_name = f"feature/improvement-{j}"
        run_cmd(["git", "checkout", "-b", branch_name])
        with open("activity_log.txt", "a") as f:
            f.write(f"Badge trigger {j}\n")
        run_cmd(["git", "add", "activity_log.txt"])
        run_cmd(["git", "commit", "-m", f"feat: add badge trigger {j}"])
        run_cmd(["git", "checkout", "main"])
        run_cmd(["git", "merge", branch_name, "--no-ff", "-m", f"merge: pull shark trigger {j}"])
        print(f"🌟 Branch {j} merged (Badge simulation complete)")

    print("\n✨ ALL DONE! ✨")
    print("1. Go to GitHub and create a new repository called 'harsh'.")
    print("2. Connect it: git remote add origin https://github.com/YOUR_USERNAME/harsh.git")
    print("3. Push: git push -u origin main")
    print("\nYour profile will turn DARK GREEN instantly across the whole year!")

if __name__ == "__main__":
    # I set this to 5000 as it's the perfect balance for a dark green graph.
    # You can increase it to 100000 if you really want, but 5000 looks cleaner.
    boost_with_backdating(total_commits=5000)
