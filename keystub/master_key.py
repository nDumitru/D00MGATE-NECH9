"""
D00MGATE-NECH9 - Master Key (PUBLIC STUB)
Author: Dumitru Nechita | License: D00MGATE-NECH9 Proprietary v1.0

This public module contains NO secret. It lets every layer run in DEMO MODE.

To activate the full system, use ONE of:
  1. Environment variable:   export D00MGATE_MASTER_KEY="your-key"
  2. Private module:         core/master_key.py (git-ignored, takes priority
                             over this stub because core/ is first on sys.path)
"""
import hashlib
import hmac
import os

PLACEHOLDER = "MASTER_KEY_HERE"

MASTER_KEY = os.environ.get("D00MGATE_MASTER_KEY", PLACEHOLDER)
OMEGA_49_SEED = os.environ.get("D00MGATE_OMEGA_49_SEED", MASTER_KEY)
ARK_LOCATION = os.environ.get("D00MGATE_ARK_LOCATION", PLACEHOLDER)

_WARN = "[MASTER KEY] Not set - DEMO MODE. Set D00MGATE_MASTER_KEY to activate."
_warned = set()


def ready() -> bool:
    """True when a real Master Key is configured."""
    return bool(MASTER_KEY) and MASTER_KEY != PLACEHOLDER


def warn(context: str = "") -> None:
    """Print the demo-mode warning once per context."""
    if context in _warned:
        return
    _warned.add(context)
    print(_WARN + (" (" + context + ")" if context else ""))


def require(operation: str) -> bool:
    """Gate for privileged operations. Returns False (and warns) in demo mode."""
    if ready():
        return True
    warn(operation)
    return False


def sign(data: str) -> str:
    """HMAC-SHA256 of data with the Master Key (hex, 64 chars)."""
    return hmac.new(MASTER_KEY.encode(), str(data).encode(), hashlib.sha256).hexdigest()
