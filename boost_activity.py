import os
import subprocess
from datetime import datetime, timedelta
import random

"""boost_activity

Small utility to generate/record activity commits. The implementation here
contains a few internal helpers that are considered private (prefixed with
an underscore). These edits are minor and keep the original behavior while
improving readability and a tiny bit of robustness.
"""


def _run_cmd(cmd):
    """Run a command and return CompletedProcess. Non-zero return codes are
    returned to the caller for handling; errors aren't raised here to preserve
    original script behavior."""
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result


def _generate_dates(total_commits, days_back):
    """Generate a sorted list of backdated timestamps.

    Returns a list of strings formatted as "%Y-%m-%d %H:%M:%S".
    This function is intentionally pure and testable.
    """
    start_date = datetime.now() - timedelta(days=days_back)
    dates = []
    for _ in range(total_commits):
        random_days = random.randint(0, days_back)
        random_seconds = random.randint(0, 86400)
        d = (start_date + timedelta(days=random_days, seconds=random_seconds))
        dates.append(d.strftime("%Y-%m-%d %H:%M:%S"))
    dates.sort()
    return dates

def boost_to_2023(total_commits=15000, days_back=1220, dry_run=False):
    """Generate many backdated commits and record them to `activity_log.txt`.

    This function intentionally keeps behavior similar to the original
    script. Only minor internal changes were made (helper renames and
    docstrings). Use with caution: running this will create many commits and
    modify git history.
    """

    print(f"🚀 BOOSTER ACTIVATED: Generating {total_commits} commits since early 2023...")

    # Pre-calculate a list of dates (pure, testable helper)
    dates = _generate_dates(total_commits, days_back)

    for i, commit_date in enumerate(dates):
        with open("activity_log.txt", "a") as f:
            f.write(f"Commit {i} - Activity Sync: {commit_date}\n")

        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = commit_date
        env["GIT_COMMITTER_DATE"] = commit_date

        if dry_run:
            # In dry-run mode we only record the intended operations to stdout
            print(f"[dry-run] would add and commit activity_log.txt for {commit_date}")
        else:
            _run_cmd(["git", "add", "activity_log.txt"])
            msg = f"chore: sync development activity {i}"
            subprocess.run(["git", "commit", "-m", msg], env=env, capture_output=True)

        if i % 1000 == 0:
            print(f"✅ Progress: {i}/{total_commits} commits synced (since 2023).")

    print("\n🔥 Triggering Achievements (Pull Shark, YOLO, Quickdraw)...")
    for j in range(20):  # More branches for more badges
        branch_name = f"patch/fix-{j}"
        if dry_run:
            print(f"[dry-run] would create branch {branch_name} and commit badge trigger {j}")
            with open("activity_log.txt", "a") as f:
                f.write(f"Badge trigger fix {j}\n")
        else:
            _run_cmd(["git", "checkout", "-b", branch_name])
            with open("activity_log.txt", "a") as f:
                f.write(f"Badge trigger fix {j}\n")
            _run_cmd(["git", "add", "activity_log.txt"])

            # Backdate the merge too
            merge_date = (datetime.now() - timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d %H:%M:%S")
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = merge_date
            env["GIT_COMMITTER_DATE"] = merge_date

            _run_cmd(["git", "commit", "-m", f"fix: resolve issue {j}"])
            _run_cmd(["git", "checkout", "main"])
            subprocess.run(["git", "merge", branch_name, "--no-ff", "-m", f"merge: patch {j}"], env=env, capture_output=True)
            print(f"🌟 Badge Trigger {j} complete.")

    print("\n✨ ALL DONE! YOUR GRAPH IS NOW LEGENDARY! ✨")
    print("Next Steps:")
    print("1. Create your profile repo (same name as your username).")
    print("2. git remote add origin https://github.com/YOUR_USERNAME/YOUR_USERNAME.git")
    print("3. git push -f origin main")

if __name__ == "__main__":
    boost_to_2023(total_commits=15000)
