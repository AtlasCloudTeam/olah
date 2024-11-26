import re

from typing import Dict, Optional

PATTERN = r"^/([^/]+)/([^/]+)/resolve/([^/]+)/(.+)"


def parse_location(loc: str) -> Optional[dict[str, str]]:
    if loc is None:
        return None

    if not loc.startswith('/'):
        loc = '/' + loc

    match = re.match(PATTERN, loc)
    if match:
        org, repo, commit, filepath = match.groups()
        return {
            'org': org,
            'repo': repo,
            'commit': commit,
            'file_path': filepath,
        }
    else:
        return None


def generate_location(org: str, repo: str, commit: str, filepath: str) -> str:
    return f'/{org}/{repo}/resolve/{commit}/{filepath}'
