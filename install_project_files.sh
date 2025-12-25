#!/bin/bash
set -e
echo "Installing essential packages"
sudo apt update
sudo apt install -y emacs virtualenvwrapper pandoc evince

# Add virtualenvwrapper to bashrc if not already present
if ! grep -q "virtualenvwrapper.sh" ~/.bashrc; then
    echo 'source /usr/share/virtualenvwrapper/virtualenvwrapper.sh' >> ~/.bashrc
fi

# Source virtualenvwrapper for this session
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh

# atuin
echo "installing atuin"
curl --proto '=https' --tlsv1.2 -LsSf https://setup.atuin.sh | sh

mkdir hello-code

cd hello-code

wget https://raw.githubusercontent.com/slawsk/hello-code/main/Code26Dictionary.py

wget https://raw.githubusercontent.com/slawsk/hello-code/main/pull-random.py

wget https://raw.githubusercontent.com/slawsk/hello-code/main/requirements.txt

mkvirtualenv randomenv
workon randomenv
pip install -r requirements.txt
echo "complete!"
