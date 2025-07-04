from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import sys

def test_scores_service(url="http://localhost:8888"):
    try:
        options = Options()
        options.add_argument('--headless')  # Run Chrome in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(2)  # Let page load

        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)

        driver.quit()
        return 1 <= score <= 1000

    except Exception as e:
        print(f"Test failed: {e}")
        return False

def main():
    result = test_scores_service()
    if result:
        print("Test Passed")
        sys.exit(0)
    else:
        print("Test Failed")
        sys.exit(-1)

if __name__ == "__main__":
    main()
