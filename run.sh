sudo rm -rf ~/carbond-hackathon
sudo rm -rf /var/carbond
sudo rm -rf /etc/carbond
sudo apt-get install pipx
pipx install poetry
poetry config virtualenvs.in-project true
sudo cp ./carbond /usr/bin/carbond
sudo mkdir /var/carbond
sudo mkdir /etc/carbond
sudo chown peach:peach /var/carbond
sudo chown peach:peach /etc/carbond
mkdir ~/carbond-hackathon
cp -r ./measurements ~/carbond-hackathon
cd ~/carbond-hackathon/measurements
poetry install