#!/bin/sh

set -eu

SV_BENCHMARKS="https://gitlab.com/sosy-lab/benchmarking/sv-benchmarks.git"

SCRIPT_REL_DIR=$(dirname "$0")
SCRIPT_ABS_DIR=$(readlink -f "$SCRIPT_REL_DIR")

TARGET_DIR="$SCRIPT_ABS_DIR"/../benchmarks
TARGET="$TARGET_DIR"/sv-benchmarks

mkdir -p "$TARGET_DIR"

if [ -d "$TARGET/.git" ]; then
    echo "Updating existing repository in $TARGET"
    git -C "$TARGET" pull --ff-only
else
    git clone --depth 1 "$SV_BENCHMARKS" "$TARGET"
fi
