import requests
from time import sleep
import Adafruit_CharLCD as LCD

# IP address of the static web page to check
url = '192.168.32.131'

# Initialize the LCD with pin settings
lcd = LCD.Adafruit_CharLCD(pin_rs=26, pin_e=19, pins_db=[13, 6, 5, 11], 
                           cols=16, rows=2, backlight=None, 
                           enable_pwm=False, gpio_mode=LCD.GPIO_MODE_BCM)

# Check if the webpage is available and display the result on the LCD
def check_webpage():
    try:
        response = requests.get(url)
        if response.status_code == 200:
            lcd.clear()
            lcd.message('Web page is\navailable')
        else:
            lcd.clear()
            lcd.message('Web page is\nunavailable')
    except requests.exceptions.RequestException as e:
        lcd.clear()
        lcd.message('Error: {}'.format(e))

# Main program loop
if __name__ == '__main__':
    while True:
        check_webpage()
        sleep(10) # wait for 10 seconds before checking again
