from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class InstagramScraper:
    """
    A class to scrape Instagram followers and following count.
    """
    def __init__(self):
        """
        Initializes the WebDriver.
        """
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def get_follow_data(self):
        """
        Opens Instagram and extracts the followers and following count.
        """
        try:
            url = "https://www.instagram.com/guviofficial/"
            self.driver.get(url)
            
            time.sleep(5)  # Allow time for the page to load
            
            followers_xpath = "//a[contains(@href, '/followers/')]/span"
            following_xpath = "//a[contains(@href, '/following/')]/span"
            
            followers_element = self.driver.find_element(By.XPATH, followers_xpath)
            following_element = self.driver.find_element(By.XPATH, following_xpath)
            
            followers = followers_element.get_attribute("innerText")
            following = following_element.get_attribute("innerText")
            
            print(f"Followers: {followers}")
            print(f"Following: {following}")
        
        except Exception as e:
            print("Error:", e)
        
        finally:
            self.driver.quit()

# Instructions to Run the Script
if __name__ == "__main__":
    print("Starting Instagram Follower Scraper...")
    print("Ensure you have Chrome and chromedriver installed.")
    print("Install dependencies using: pip install selenium webdriver-manager")
    print("Run the script using: python script_name.py")
    
    scraper = InstagramScraper()
    scraper.get_follow_data()
