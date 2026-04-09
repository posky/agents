#!/usr/bin/env python3
"""Summarize the current git worktree for commit planning."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from typing import Any

NOISE_NAMES = {".DS_Store", "Thumbs.db"}


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.rstrip("\n")


def parse_status_line(line: str) -> dict[str, str]:
    return {
        "staged": line[:1],
        "unstaged": line[1:2],
        "path": line[3:],
    }


def build_report() -> dict[str, Any]:
    status_output = run_git(["status", "--porcelain=v1", "--untracked-files=all"])
    status_entries = [
        parse_status_line(line)
        for line in status_output.splitlines()
        if line.strip()
    ]
    untracked_files = [
        entry["path"]
        for entry in status_entries
        if entry["staged"] == "?" and entry["unstaged"] == "?"
    ]

    report = {
        "branch": run_git(["branch", "--show-current"]),
        "status": status_entries,
        "untracked_files": untracked_files,
        "unstaged_name_status": run_git(["diff", "--name-status"]).splitlines(),
        "staged_name_status": run_git(["diff", "--cached", "--name-status"]).splitlines(),
        "unstaged_diff_stat": run_git(["diff", "--stat"]).splitlines(),
        "staged_diff_stat": run_git(["diff", "--cached", "--stat"]).splitlines(),
        "likely_noise": sorted(
            {
                entry["path"]
                for entry in status_entries
                if entry["path"].rsplit("/", 1)[-1] in NOISE_NAMES
            }
        ),
    }
    return report


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"Branch: `{report['branch'] or '(detached)'}`",
        "",
        "Status:",
    ]

    if report["status"]:
        for entry in report["status"]:
            lines.append(f"- `{entry['staged']}{entry['unstaged']}` `{entry['path']}`")
    else:
        lines.append("- Clean working tree")

    lines.extend(["", "Untracked files:"])
    if report["untracked_files"]:
        lines.extend(f"- `{path}`" for path in report["untracked_files"])
    else:
        lines.append("- None")

    lines.extend(["", "Unstaged diff stat:"])
    if report["unstaged_diff_stat"]:
        lines.extend(f"- {line}" for line in report["unstaged_diff_stat"])
    else:
        lines.append("- None")

    lines.extend(["", "Staged diff stat:"])
    if report["staged_diff_stat"]:
        lines.extend(f"- {line}" for line in report["staged_diff_stat"])
    else:
        lines.append("- None")

    lines.extend(["", "Unstaged name-status:"])
    if report["unstaged_name_status"]:
        lines.extend(f"- {line}" for line in report["unstaged_name_status"])
    else:
        lines.append("- None")

    lines.extend(["", "Staged name-status:"])
    if report["staged_name_status"]:
        lines.extend(f"- {line}" for line in report["staged_name_status"])
    else:
        lines.append("- None")

    lines.extend(["", "Likely noise files:"])
    if report["likely_noise"]:
        lines.extend(f"- `{path}`" for path in report["likely_noise"])
    else:
        lines.append("- None")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Summarize current git changes for commit planning.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    args = parser.parse_args()

    try:
        report = build_report()
    except subprocess.CalledProcessError as exc:
        sys.stderr.write(exc.stderr or str(exc))
        return exc.returncode

    if args.format == "json":
        json.dump(report, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        sys.stdout.write(render_markdown(report))
        sys.stdout.write("\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
