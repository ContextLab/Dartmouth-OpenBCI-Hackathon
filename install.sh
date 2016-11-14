#!/bin/bash

echo "INSTALLING MAIN PACKAGES"
pip install -e .

echo "INSTALLING HYPER-TOOLS PACKAGES"
cd hyper-tools/python
pip install -e .

cd ../../OpenBCI_Python
echo "INSTALLING OPENBCI_PYTHON PACKAGES"
pip install -r requirements.txt

cd ../

echo "UPGRADING NUMPY TO LATEST VERSION"
pip install numpy --upgrade
