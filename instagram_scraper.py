from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_instagram_follow_data():
    """
    This function opens Instagram, extracts the followers and following count,
    and prints the values.
    """
    # Set up the Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Open the Instagram profile URL
        url = "https://www.instagram.com/guviofficial/"
        driver.get(url)
        
        # Allow time for the page to load
        time.sleep(5)
        
        # Locate and extract the Followers and Following count
        followers_xpath = "//a[contains(@href, '/followers/')]/span"
        following_xpath = "//a[contains(@href, '/following/')]/span"
        
        followers = driver.find_element(By.XPATH, followers_xpath).text
        following = driver.find_element(By.XPATH, following_xpath).text
        
        print(f"Followers: {followers}")
        print(f"Following: {following}")
    
    except Exception as e:
        print("Error:", e)
    
    finally:
        # Close the browser
        driver.quit()

# Execute the function
if __name__ == "__main__":
    get_instagram_follow_data()
