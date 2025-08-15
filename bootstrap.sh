#!/bin/bash

# bootstrap.sh

# ==========================================
# ANSIBLE BOOTSTRAP (repo-local)
# ==========================================
#
# Purpose:
#   Create/activate a Python venv, upgrade pip (optional),
#   install Python deps from requirements.txt, and install Ansible Galaxy
#   content from requirements.yml. Safe to run repeatedly.
#
# Usage:
#   ./bootstrap.sh [--no-venv] [--no-galaxy] [--upgrade-pip]
#                  [--venv-path PATH] [--requirements PATH]
#                  [--galaxy-req PATH]
#
# Defaults:
#   VENV_PATH=./venv
#   REQ_PY=requirements.txt
#   REQ_GALAXY=requirements.yml
#
# Env (optional):
#   VENV_PATH, PIP_INDEX_URL, PIP_EXTRA_INDEX_URL
#
# Logs:
#   log/bootstrap-YYYYmmdd-HHMMSS.log  (symlink: log/bootstrap-latest.log)
#
# Exit:
#   Non-zero on failure. Prints a short error with the log path.
# 

set -Eeuo pipefail

# --- Defaults ---
VENV_PATH="${VENV_PATH:-./venv}"
REQ_PY="requirements.txt"
REQ_GALAXY="requirements.yml"
DO_VENV=1
DO_GALAXY=1
DO_UPGRADE_PIP=0

# --- Args ---
while [[ $# -gt 0 ]]; do
  case "$1" in
    --no-venv) DO_VENV=0 ;;
    --no-galaxy) DO_GALAXY=0 ;;
    --upgrade-pip) DO_UPGRADE_PIP=1 ;;
    --venv-path) VENV_PATH="${2:?}"; shift ;;
    --requirements) REQ_PY="${2:?}"; shift ;;
    --galaxy-req) REQ_GALAXY="${2:?}"; shift ;;
    *) echo "Unknown flag: $1" >&2; exit 2 ;;
  esac
  shift
done

# --- Logging setup ---
mkdir -p log
ts="$(date '+%Y%m%d-%H%M%S')"
LOG="log/bootstrap-${ts}.log"
ln -sfn "$LOG" log/bootstrap-latest.log

exec > >(tee -a "$LOG") 2>&1

trap 'echo "ERROR: bootstrap failed. See $LOG" >&2' ERR

echo "==> Bootstrap start: $ts"
echo "Repo: $(pwd)"
echo "VENV_PATH: $VENV_PATH"
echo "Python: $(command -v python3 || true)"
echo

# --- Venv ---
if (( DO_VENV )); then
  if [[ ! -d "$VENV_PATH" ]]; then
    echo "Creating venv at $VENV_PATH ..."
    python3 -m venv "$VENV_PATH"
  fi

  # shellcheck disable=SC1090
  source "${VENV_PATH}/bin/activate"
  echo "Venv activated: ${VENV_PATH}"

  if [[ -z "${VIRTUAL_ENV:-}" ]]; then
    echo "ERROR: not in a venv; refusing to install." >&2
    exit 1
  fi

  # ensure we’re using the venv’s python/pip and allow installs on Debian/Ubuntu with PEP 668
  export PIP_BREAK_SYSTEM_PACKAGES=1
fi

# --- pip upgrade (optional) ---
if (( DO_UPGRADE_PIP )); then
  echo "Upgrading pip..."
  python -m pip install --upgrade pip --disable-pip-version-check
fi

# --- Python deps ---
if [[ -f "$REQ_PY" ]]; then
  echo "Installing Python deps from ${REQ_PY} ..."
  python -m pip install -r "$REQ_PY"
else
  echo "Skipping Python deps: ${REQ_PY} not found."
fi

# --- Ansible Galaxy deps ---
if (( DO_GALAXY )); then
  if command -v ansible-galaxy >/dev/null 2>&1; then
    if [[ -f "$REQ_GALAXY" ]]; then
      echo "Installing Ansible Galaxy deps from ${REQ_GALAXY} ..."
      ansible-galaxy install -r "$REQ_GALAXY" --ignore-errors
    else
      echo "Skipping Galaxy deps: ${REQ_GALAXY} not found."
    fi
  else
    echo "Skipping Galaxy deps: ansible-galaxy not found in PATH."
  fi
fi

echo "==> Bootstrap complete."
