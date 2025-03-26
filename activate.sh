#!/bin/bash

# Script to install aws_util in development mode on macOS/Linux
# with optional project directory specification.

# Default project directory
PROJECT_DIR="."

# Parse command-line options
while getopts "d:" opt; do
  case "$opt" in
    d)
      PROJECT_DIR="$OPTARG"
      ;;
    \?)
      echo "Usage: $0 [-d <project_dir>]"
      exit 1
      ;;
  esac
done
shift $((OPTIND-1)) # Remove parsed options

# Check if the project directory exists
if [ ! -d "$PROJECT_DIR" ]; then
  echo "Error: Project directory '$PROJECT_DIR' not found."
  exit 1
fi

# Navigate to the project directory
cd "$PROJECT_DIR"

# Create and activate a virtual environment (if it doesn't exist)
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
else
  echo "Virtual environment 'venv' already exists."
fi

echo "Activating virtual environment..."
source venv/bin/activate

# Install the package in development mode
echo "Installing aws_util in editable mode..."
pip install -e .

# Update pip
echo "Updating pip..."
pip install --upgrade pip

# Verify installation
echo "Verifying installation..."
pip list | grep aws_util

echo "Installation complete. You can now run your script."
echo "Example:"
echo "ecs_connect -p your_profile"

# Example of running the script, remove if you don't want to run it.
# python aws_util/aws_util/ecs_utils.py -p your_profile -r your_region

# Instructions on how to deactivate
echo ""
echo "When finished, deactivate the venv using: deactivate"
