tools you need: 
1. 2 Raspberry Pi
2. 1 LCD I2C
3. A website sample running on apache2
Below is the circuit diagram
![image](https://github.com/QuocWhite/reqest/assets/117848153/cddab2fe-43f0-4099-8a72-62cfa004e141)

in thís project I use a Raspberry Pi to run like a local server anf another Raspberry to check the website of the first one by request library to check that state of the url is 200 mean running or not
if the web is running print out on the I2C LCD that the web is running else print out the web is not available
