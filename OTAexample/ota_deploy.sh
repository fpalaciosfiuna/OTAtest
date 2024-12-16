sudo cp test.py /home/nano/Desktop/util/code/ota/
sudo chmod +x /home/nano/Desktop/util/code/ota/test.py

sudo cp otatest.service /etc/systemd/user/
sudo systemctl daemon-reload
sudo systemctl enable --global otatest.service
