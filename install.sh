#!/bin/bash
set -e

COMMANDS_DIR="$HOME/.claude/commands"
SKILLS_DIR="$HOME/.claude/skills"

mkdir -p "$COMMANDS_DIR"
mkdir -p "$SKILLS_DIR"

echo "Installing Claude Code skills..."
cp -r commands/* "$COMMANDS_DIR/"
cp -r skills/* "$SKILLS_DIR/"
echo "Done! Skills installed to:"
echo "  $COMMANDS_DIR"
echo "  $SKILLS_DIR"
