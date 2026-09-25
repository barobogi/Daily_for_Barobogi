# -*- coding: utf-8 -*-
"""
sync_snapshot_to_github.py — GitHub Pages (Daily_for_Barobogi) 3AI 스냅샷 주기적 커밋 & 푸시 유틸리티
- index.lock 자동 감지 및 안전 해제
- git 명령어 returncode 엄격 검증
"""
import os
import sys
import time
import hashlib
import subprocess
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO_DIR = Path(r"D:\AI\Daily_for_Barobogi")
SNAPSHOT_FILE = REPO_DIR / "latest_snapshot.json"
LAST_PUSH_HASH_FILE = REPO_DIR / ".last_snapshot_push_hash"
INDEX_LOCK_FILE = REPO_DIR / ".git" / "index.lock"

def get_file_hash(filepath: Path) -> str:
    if not filepath.exists():
        return ""
    with open(filepath, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def clear_stale_lock():
    """index.lock 파일 존재 시 5초 폴링 대기 후 10초 경과한 stale lock은 안전 삭제"""
    if not INDEX_LOCK_FILE.exists():
        return True
    
    print("[SnapshotSync] index.lock detected. Waiting for unlock...")
    for _ in range(10):
        if not INDEX_LOCK_FILE.exists():
            return True
        time.sleep(0.5)

    if INDEX_LOCK_FILE.exists():
        try:
            mtime = INDEX_LOCK_FILE.stat().st_mtime
            if (time.time() - mtime) > 10.0:
                print("[SnapshotSync WARNING] Removing stale index.lock older than 10s...")
                INDEX_LOCK_FILE.unlink(missing_ok=True)
                return True
        except Exception as e:
            print(f"[SnapshotSync ERROR] Failed to clear lock: {e}")
            return False
    return not INDEX_LOCK_FILE.exists()

def sync_if_changed():
    if not SNAPSHOT_FILE.exists():
        print("[SnapshotSync] latest_snapshot.json does not exist yet.")
        return False

    current_hash = get_file_hash(SNAPSHOT_FILE)
    last_hash = ""
    if LAST_PUSH_HASH_FILE.exists():
        try:
            last_hash = LAST_PUSH_HASH_FILE.read_text(encoding="utf-8").strip()
        except Exception:
            pass

    if current_hash == last_hash:
        print("[SnapshotSync] Snapshot unchanged. Skipping git push.")
        return False

    if not clear_stale_lock():
        print("[SnapshotSync ABORT] Cannot obtain git lock.")
        return False

    print(f"[SnapshotSync] Changes detected in {SNAPSHOT_FILE.name}. Committing and pushing to GitHub Pages...")
    try:
        # Step 1: git add
        res1 = subprocess.run("git add chat.html latest_snapshot.json sync_snapshot_to_github.py", cwd=str(REPO_DIR), shell=True, capture_output=True, text=True)
        if res1.returncode != 0:
            print(f"[SnapshotSync FAIL] git add failed (code {res1.returncode}): {res1.stderr}")
            return False

        # Step 2: git commit
        res2 = subprocess.run('git commit -m "auto: Sync 3AI real-time chat snapshot for GitHub Pages"', cwd=str(REPO_DIR), shell=True, capture_output=True, text=True)
        if res2.returncode != 0 and "nothing to commit" not in res2.stdout and "nothing to commit" not in res2.stderr:
            print(f"[SnapshotSync FAIL] git commit failed (code {res2.returncode}): {res2.stderr}")
            return False

        # Step 3: git push
        res3 = subprocess.run("git push origin main", cwd=str(REPO_DIR), shell=True, capture_output=True, text=True)
        if res3.returncode != 0:
            print(f"[SnapshotSync FAIL] git push failed (code {res3.returncode}): {res3.stderr}")
            return False

        LAST_PUSH_HASH_FILE.write_text(current_hash, encoding="utf-8")
        print("[SnapshotSync SUCCESS] Successfully committed and pushed updated snapshot to GitHub Pages! (exitcode 0)")
        return True
    except Exception as e:
        print(f"[SnapshotSync ERROR] Exception during git sync: {e}")
        return False

if __name__ == "__main__":
    sync_if_changed()
