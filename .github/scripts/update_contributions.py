#!/usr/bin/env python3
"""Refresh verified merged upstream PRs in the GitHub profile README.

Only replaces content between the generated contributions markers.
Requires GITHUB_TOKEN; fails closed on incomplete GitHub search results.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen
import json
import os

USERNAME = "cristianchiriac"
README = Path("README.md")
START = "<!-- BEGIN AUTO-GENERATED CONTRIBUTIONS -->"
END = "<!-- END AUTO-GENERATED CONTRIBUTIONS -->"
SEARCH_URL = "https://api.github.com/search/issues"
QUERY = f"author:{USERNAME} is:pr is:merged is:public -user:{USERNAME}"
HISTORY_URL = "https://github.com/search?" + urlencode({"q": QUERY, "type": "pullrequests"})
HEAD_START = "<!-- BEGIN UPSTREAM TOTAL -->"
HEAD_END = "<!-- END UPSTREAM TOTAL -->"


def fetch_merged_prs() -> list[dict]:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN is required")

    merged = []
    total = None
    for page in range(1, 11):
        query = urlencode({
            "q": QUERY,
            "per_page": 100,
            "page": page,
            "sort": "updated",
            "order": "desc",
        })
        request = Request(
            f"{SEARCH_URL}?{query}",
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "User-Agent": "github-profile-contributions-updater",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
        with urlopen(request, timeout=30) as response:
            data = json.load(response)

        if data.get("incomplete_results") or not isinstance(data.get("total_count"), int):
            raise RuntimeError("GitHub returned incomplete search results")
        if total is None:
            total = data["total_count"]
            if total > 1000:
                raise RuntimeError("GitHub search has a 1000-result cap")
        if data["total_count"] != total:
            raise RuntimeError("GitHub search result count changed during pagination")
        batch = data.get("items", [])
        if not batch and len(merged) < total:
            raise RuntimeError("GitHub search ended before all results were returned")
        merged.extend(batch)
        if len(merged) >= total:
            break

    if len(merged) != total:
        raise RuntimeError("GitHub search pagination did not return all PRs")
    return merged


def count_prs_by_repo(items: list[dict]) -> dict[str, int]:
    repos: dict[str, int] = defaultdict(int)
    for item in items:
        url = item.get("html_url", "")
        path = urlsplit(url)
        parts = path.path.strip("/").split("/")
        merged_at = (item.get("pull_request") or {}).get("merged_at")
        if path.scheme != "https" or path.netloc != "github.com":
            raise ValueError(f"Invalid GitHub PR URL: {url}")
        if len(parts) != 4 or parts[2] != "pull" or not parts[3].isdigit():
            raise ValueError(f"Unexpected GitHub PR URL: {url}")
        if not merged_at:
            raise ValueError(f"Unverified merge time for {url}")
        if parts[0].lower() == USERNAME.lower():
            continue  # Own repository merges are not external upstream acceptance.
        repo = f"{parts[0]}/{parts[1]}"
        repos[repo] += 1

    return repos


def replace_block(text: str, start: str, end: str, body: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise RuntimeError("README generation markers must exist exactly once")
    prefix, rest = text.split(start, 1)
    _, suffix = rest.split(end, 1)
    return f"{prefix}{start}\n{body}\n{end}{suffix}"


def update_profile(original: str, items: list[dict], updated_on: str) -> str:
    repos = count_prs_by_repo(items)
    if not repos:
        raise RuntimeError("No external merged PRs: refusing to replace existing profile")
    total = sum(repos.values())
    repeat = sum(number >= 2 for number in repos.values())
    headline = f"**{total} merged upstream pull requests.**"
    summary = (
        f"Of the {len(repos)} upstream repositories I contributed to, "
        f"{repeat} merged two or more of my pull requests.\n\n"
        f"[Browse my merged upstream PRs]({HISTORY_URL}) · Updated {updated_on} (UTC)."
    )
    text = replace_block(original, HEAD_START, HEAD_END, headline)
    return replace_block(text, START, END, summary)


def main() -> None:
    original = README.read_text(encoding="utf-8")
    items = fetch_merged_prs()
    updated = update_profile(original, items, datetime.now(timezone.utc).strftime("%d %b %Y"))
    if updated == original:
        print("Profile already up to date; no commit required.")
        return
    README.write_text(updated, encoding="utf-8")
    print("Updated README.md from verified merged GitHub pull requests.")


if __name__ == "__main__":
    main()
