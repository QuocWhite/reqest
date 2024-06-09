tools you need: 
1. 2 Raspberry Pi
2. 1 LCD I2C
3. A website sample running on apache2
Wiring diagram in pi2 folder.
in this project I use a Raspberry Pi to run like a local server and another Raspberry to check the website of the first one by request library to check that state of the url is 200 mean running or not
if the web is running print out on the I2C LCD that the web is running else print out the web is not available
