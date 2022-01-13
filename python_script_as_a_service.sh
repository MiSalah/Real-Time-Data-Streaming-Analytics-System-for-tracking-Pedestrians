sudo apt-get install -y systemd
# Create a python file -service.py.
sudo nano /etc/systemd/system/test.service #(name of the service which is -service in this case)

# change in the below file
[Unit]
Description=My python Service
After=multi-user.target
[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/<username>/service.py  #your python path /your file path
[Install]
WantedBy=multi-user.target

sudo systemctl daemon-reload
sudo systemctl enable service.service

# to start the service
sudo systemctl start test.service

# check status of your service
sudo systemctl status test.service

# restart, stop, status, start