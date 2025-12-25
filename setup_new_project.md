---
title: Setting Up New Display
---
1. On the home computer, download the xml file for the title from [Office of Law Revision
Counsel](https://uscode.house.gov/download/download.shtml).

2. Name the file ```usc{titlenumber}.xml```

3. Create the relevant code dictionary by running ```python create_json_dict.py {titlenumber}```

4. Change ```pull_random.py```.

- Change ```title_number``` at the top of the file.

- Change ```make_greeting()``` to reflect the current
title. Right now it says "through U.S. tax law." whatever you change it to
should have 20 characters; if you need more, add one more thing to the list with
up to 20 characters.

5. Push to repository.

6. Go into ```install_project_files.sh``` and change the first wget command to
reflect the correct dictionary.

7. Flash the new SD drive. This will involve naming the pi.

8. Copy ```install_project_files.sh``` to the rootfs partition. 
   
   cp install_project_files.sh /media/penguin/rootfs/home/PINAMEHERE/

9. Go into .ssh/config and add (you may have to change pi_new to something else
   if you're doing this with a bunch of pis)

Host pi_new
   Hostname 192.168.1.200
   User PINAME
   ForwardX11 yes

10. Turn on the Pi so that it has an IP address.

11. On the home computer, type: hostname -I to get base IP address, then sudo
   nmap -sn BASEIPADDRESS to find the Pi's address, PIADDRESS

12. Remote into the Pi: 

ssh -X PINAME@PIADDRESS

13. On first boot of the pi, on the Pi:

cd ~
chmod +x install_project_files.sh
./install_project_files.sh

14. On the Pi, give the Pi a fixed IP address (below it's 200, same as the other Pi, because
I'm assuming I won't ever run them at the same time)

sudo nmcli connection modify netplan-wlan0-AgentChicken ipv4.addresses 192.168.1.200/24
sudo nmcli connection modify netplan-wlan0-AgentChicken ipv4.gateway 192.168.1.1
sudo nmcli connection modify netplan-wlan0-AgentChicken ipv4.dns "192.168.1.1 8.8.8.8"
sudo nmcli connection modify netplan-wlan0-AgentChicken ipv4.method manual
sudo reboot

15. Back on the home computer, set up the SSH key: 

ssh-keygen -R 192.168.1.200
ssh-copy-id PINAME@192.168.1.200. 

Then, after 30 seconds, reconnect: ssh pi_new

16. The next part sets up to start on boot, so make sure everything is working
by testing it manually first. Then, on home computer, go into hellocode.service and change the name to reflect the
name of the Pi.

17. Copy hellocode.service to the Pi: scp hellocode.service pi_new:~/

18. Go to the Pi and move hellocode.service to /etc/systemd/system/

19. Still on the Pi: 

sudo systemctl daemon-reload
sudo systemctl enable hellocode.service
sudo systemctl start hellocode.service

Check status: sudo systemctl status hellocode.service

