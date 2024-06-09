
1. Install Pi OS via any tool you have such as Rufus(for Windows), Balena Etcher(for Linux), or you can install Raspberry Pi OS at https://www.raspberrypi.com/software/ into the SD card.
2. Run your Pi by any base you have if you don not have monitor you can easyly use your laptop to install VNC Viewer and use as your Pi keyboard and monitor at https://youtu.be/Vl-2Y4kvTRo?si=ovCMe8eTxm7iVz-1.
3. Open Pi terminal by Ctrl + Shift + T and type "sudo apt update && sudo apt upgrade -y".
4. Install apache2 to storage you website as local "sudo apt install apache2 -y".
5. Give permission for /var/www/html to change you web "sudo chmod -R 777 /var/www/html" mean that read, write and excute.
--> now you can change your website in here.
6. Use "ip -br add" in terminal to get your IP this is also the url of the website if you do not set it. 
