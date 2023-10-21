import os
import subprocess
from datetime import datetime, timedelta
import random

def run_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result

def boost_to_2023(total_commits=15000, days_back=1220):
    print(f"🚀 BOOSTER ACTIVATED: Generating {total_commits} commits since early 2023...")
    
    start_date = datetime.now() - timedelta(days=days_back)
    
    # Pre-calculate a list of dates to make it faster
    dates = []
    for _ in range(total_commits):
        random_days = random.randint(0, days_back)
        random_seconds = random.randint(0, 86400)
        d = (start_date + timedelta(days=random_days, seconds=random_seconds))
        dates.append(d.strftime("%Y-%m-%d %H:%M:%S"))
    
    # Sort dates to keep the git history somewhat logical
    dates.sort()

    for i, commit_date in enumerate(dates):
        with open("activity_log.txt", "a") as f:
            f.write(f"Commit {i} - Activity Sync: {commit_date}\n")
        
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = commit_date
        env["GIT_COMMITTER_DATE"] = commit_date
        
        run_cmd(["git", "add", "activity_log.txt"])
        msg = f"chore: sync development activity {i}"
        subprocess.run(["git", "commit", "-m", msg], env=env, capture_output=True)
        
        if i % 1000 == 0:
            print(f"✅ Progress: {i}/{total_commits} commits synced (since 2023).")

    print("\n🔥 Triggering Achievements (Pull Shark, YOLO, Quickdraw)...")
    for j in range(20):  # More branches for more badges
        branch_name = f"patch/fix-{j}"
        run_cmd(["git", "checkout", "-b", branch_name])
        with open("activity_log.txt", "a") as f:
            f.write(f"Badge trigger fix {j}\n")
        run_cmd(["git", "add", "activity_log.txt"])
        
        # Backdate the merge too
        merge_date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d %H:%M:%S")
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = merge_date
        env["GIT_COMMITTER_DATE"] = merge_date
        
        run_cmd(["git", "commit", "-m", f"fix: resolve issue {j}"])
        run_cmd(["git", "checkout", "main"])
        subprocess.run(["git", "merge", branch_name, "--no-ff", "-m", f"merge: patch {j}"], env=env, capture_output=True)
        print(f"🌟 Badge Trigger {j} complete.")

    print("\n✨ ALL DONE! YOUR GRAPH IS NOW LEGENDARY! ✨")
    print("Next Steps:")
    print("1. Create your profile repo (same name as your username).")
    print("2. git remote add origin https://github.com/YOUR_USERNAME/YOUR_USERNAME.git")
    print("3. git push -f origin main")

if __name__ == "__main__":
    boost_to_2023(total_commits=15000)
