apt-get install pipx
pipx install poetry
sudo cp ./carbond /usr/bin/carbond
sudo mkdir /var/carbond
sudo mkdir /etc/carbond
sudo chown peach:peach /var/carbond
sudo chown peach:peach /etc/carbond
mkdir ~/carbond-hackathon
cp -r ./measurements ~/carbond-hackathon
