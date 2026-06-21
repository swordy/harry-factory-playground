"""Domain model for the running version.

Pure value object — no IO, no side-effects.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Version:
    sha: str
