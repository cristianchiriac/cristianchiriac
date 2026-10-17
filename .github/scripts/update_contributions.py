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
import re

USERNAME = "cristianchiriac"
README = Path("README.md")
START = "<!-- BEGIN AUTO-GENERATED CONTRIBUTIONS -->"
END = "<!-- END AUTO-GENERATED CONTRIBUTIONS -->"
SEARCH_URL = "https://api.github.com/search/issues"
HISTORY_URL = (
    "https://github.com/search?q=author%3Acristianchiriac+is%3Apr+is%3Amerged"
    "&type=pullrequests"
)


def fetch_merged_prs() -> list[dict]:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN is required")

    merged = []
    total = None
    for page in range(1, 11):
        query = urlencode({
            "q": f"author:{USERNAME} is:pr is:merged",
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


def parse_prs(items: list[dict]) -> dict[str, list[dict]]:
    repos: dict[str, list[dict]] = defaultdict(list)
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
        repos[repo].append({
            "url": url,
            "number": int(parts[3]),
            "title": item.get("title", ""),
            "merged_at": merged_at,
        })

    for prs in repos.values():
        prs.sort(key=lambda p: p["merged_at"], reverse=True)
    return repos


def safe_table_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).replace("|", r"\|").replace("<", "&lt;").replace(">", "&gt;")


def render(items: list[dict]) -> str:
    repos = parse_prs(items)
    ordered = sorted(
        repos.items(),
        key=lambda pair: (
            -len(pair[1]),
            -datetime.fromisoformat(pair[1][0]["merged_at"].replace("Z", "+00:00")).timestamp(),
            pair[0].lower(),
        ),
    )
    count = sum(len(prs) for _, prs in ordered)
    latest = max((p["merged_at"] for _, prs in ordered for p in prs), default=None)
    if not latest:
        raise RuntimeError("No external merged PRs: refusing to replace existing profile")

    lines = [
        f"**{count} accepted pull requests** across **{len(ordered)} independent upstream repositories**.",
        "",
        "Every PR below is merged into the upstream project, not merely submitted from a fork.",
        "",
        "<details>",
        f"<summary><strong>Explore the complete contribution log</strong> — {count} merged PRs / {len(ordered)} repositories</summary>",
        "",
        "| Upstream | Latest merged change | Accepted PRs |",
        "|:--|:--|:--|",
    ]
    for repo, prs in ordered:
        links = " · ".join(f"[#{p['number']}]({p['url']})" for p in prs)
        lines.append(
            f"| [{repo}](https://github.com/{repo}) | "
            f"{safe_table_text(prs[0]['title'])} | {links} |"
        )
    lines += [
        "",
        "</details>",
        "",
        f"<sub>Maintained automatically from verified GitHub merges. Latest: {latest[:10]} (UTC). Open and closed-unmerged PRs are excluded.</sub>",
        "",
        f"[**View the complete upstream history ↗**]({HISTORY_URL})",
    ]
    return "\n".join(lines)


def main() -> None:
    original = README.read_text(encoding="utf-8")
    if original.count(START) != 1 or original.count(END) != 1:
        raise RuntimeError("README generation markers must exist exactly once")
    prefix, rest = original.split(START, 1)
    _, suffix = rest.split(END, 1)
    updated = prefix + START + "\n" + render(fetch_merged_prs()) + "\n" + END + suffix
    if updated == original:
        print("Profile already up to date; no commit required.")
        return
    README.write_text(updated, encoding="utf-8")
    print("Updated README.md from verified merged GitHub pull requests.")


if __name__ == "__main__":
    main()
