#!/bin/bash
# D00MGATE-NECH9 Ada Build Script
# Author: Dumitru Nechita
#
# Requirements:
#   sudo apt-get install gnat gprbuild
#
# Compile:
#   mkdir -p build/obj
#   gprbuild -P doomgate.gpr
#
# Run:
#   ./build/doomgate_demo

set -e
cd "$(dirname "$0")"
mkdir -p build/obj
# Private key: DOOMGATE_KEY_DIR=core ./build.sh  (uses core/master_key.ads/.adb)
gprbuild -P doomgate.gpr -XDOOMGATE_KEY_DIR="${DOOMGATE_KEY_DIR:-keystub}"
echo ""
echo "Run: ./build/doomgate_demo"
