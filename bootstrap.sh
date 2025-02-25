#!/bin/bash
echo "Setting up Ansible and Molecule..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
ansible-galaxy install -r requirements.yml
echo "Ansible is ready to use!"
