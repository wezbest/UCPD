#!/usr/bin/env zsh
# This is for setting up python virtual environment for 3.12

# Install python
sudo apt-get install python3.12
sudo apt-get install python3.12-venv

# Create virtual environment
python3.12 -m venv rape

# Activate virtuenenv
source rape/bin/activate

echo "To exit type - deactivate"