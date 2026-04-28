#!/bin/bash

if [ "$1" = "--version" ]; then
    infer --version
    exit 0
fi

SELF="$(dirname "$(realpath "$0")")"
MODELS="$SELF"/models.c

source "$SELF"/../../../config.env

$INFER_BIN \
  --pulse-only \
  --pulse-unsafe-malloc \
  --report-suppress-errors=PULSE_UNINITIALIZED_VALUE \
  -- gcc $MODELS $@

