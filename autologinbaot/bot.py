# Import necessary libraries
from selenium import webdriver 
import os
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Function to start the bot
def startBot(username, password, url):
    # Path to the chromedriver executable
    path = "C:\\Users\\aryas\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
    
    # Create a service object with the path
    service = Service(path)
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    # Create the webdriver object
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Open the website in Chrome
    print("Opening the login page...")
    driver.get(url)
    
    # Fill in the username (replace with actual selector)
    print("Filling in the username...")
    driver.find_element(By.NAME, "username_field_name").send_keys(username)
    
    # Fill in the password (replace with actual selector)
    print("Filling in the password...")
    driver.find_element(By.NAME, "password_field_name").send_keys(password)
    
    # Click the login button (replace with actual selector)
    print("Clicking the login button...")
    driver.find_element(By.CSS_SELECTOR, "commit_button_css_selector").click()

    # Wait for a while before closing
    print("Login process initiated...")
    time.sleep(5)
    
    # Close the browser
    driver.quit()

# Driver code
if __name__ == "__main__":
    # Enter your login credentials
    username = "aryakp12344"
    password = "arya@123"
    
    # URL of the login page
    url = "https://github.com/login"
    
    # Call the function
    startBot(username, password, url)
