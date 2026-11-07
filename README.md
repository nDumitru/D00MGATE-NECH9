# D00MGATE-NECH9
## Author: Dumitru Nechita | License: D00MGATE-NECH9 Proprietary v1.0

> *"You can see the gate. You cannot dial it without the address."*

Public demonstration layer of the D00MGATE-NECH9 protocol, in **Python** and **Ada**.
Core internals are redacted. See `README_v030.md` for the full architecture description
and `MASTER_COVENANT.md` for concept ownership.

### Files

```
keystub/
  master_key.py            <- Public Master Key stub (Python) - no secret
  master_key.ads / .adb    <- Public Master Key stub (Ada)    - no secret

layer0_asimov.py ... layer9_omega49.py   <- Layers 0-9 (public stubs)
veridex_layer10.py         <- VERIDEX Layer 10
reverse_hydra.py / .ads / .adb           <- ReverseHydra Engine (original concept)
historic_hardening.py / .ads / .adb      <- HistoricHardening (original concept)
veridex.ads / .adb         <- VERIDEX Layer 10 (Ada)
luhn_dynamic.ads / .adb    <- Layer 1: Dynamic Luhn Token (Ada)
genesis.py                 <- OMEGA-49 domain + genesis fingerprint
challenge.py               <- CTF v1.0.0 (levels 1-6, 9)
challenge_demo*.py         <- Earlier CTF versions (v0.1, v0.2)
doomgate_demo.adb          <- Ada main demo (all systems)
index.html                 <- Project website
tests/                     <- Smoke tests (Python)

doomgate.gpr               <- GNAT project file
build.sh                   <- Build script
```

### Master Key

The repository contains **no key**. Without one, everything runs in **DEMO MODE**.

Activate it in one of two ways:

1. **Environment variable** (Python and Ada):
   ```bash
   export D00MGATE_MASTER_KEY="your-key"
   ```
2. **Private files** in `core/`, which are git-ignored and never committed:
   - Python: `core/master_key.py` (same functions as `keystub/master_key.py`); `core/` is searched first.
   - Ada: `core/master_key.ads` + `core/master_key.adb`, then build with `DOOMGATE_KEY_DIR=core ./build.sh`.

### Quick Start - Python

```bash
python3 challenge.py --level 1       # CTF
python3 veridex_layer10.py           # Layer 10 demo
python3 -m unittest discover -s tests
```

`requirements.txt` lists optional extras (for example `colorama` for coloured CTF output). The demos run with the standard library alone.

### Quick Start - Ada

```bash
# Install compiler
sudo apt-get install gnat gprbuild

# Build
./build.sh

# Run demo
./build/doomgate_demo
```

### TODO markers in code

Search for `-- TODO:` across all files for places you should customize:
- `luhn_dynamic.adb` -> Delta Nechita seed integration
- `reverse_hydra.adb` -> Evolution content implementation
- `historic_hardening.adb` -> Hardening logic implementation
- `veridex.adb` -> Silent ops, JunkDNA positions, Gravemind conversion

### Verified Working

Compiled and tested with GNAT 13 on Ubuntu 24.04 and Python 3.11 / 3.13.
All engines run in DEMO MODE. With `D00MGATE_MASTER_KEY` set, the privileged operations
(Ark seal, continuity, approvals) are enabled.

"The gate is open. The address is mine." - Dumitru Nechita, 2026
