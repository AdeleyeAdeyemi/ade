from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import re

def test_scores_service(url="http://localhost:8888"):
    driver = None
    try:
        options = Options()
        options.add_argument('--headless')  # Run Chrome in headless mode
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options=options)
        driver.get(url)

        # Wait up to 10 seconds for the element with id 'score' to appear
        score_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "score"))
        )

        # Extract digits from the score text (e.g. "Score: 100")
        digits = re.findall(r'\d+', score_element.text)
        if not digits:
            raise ValueError(f"No digits found in score text: '{score_element.text}'")
        score = int(digits[0])

        return 1 <= score <= 1000

    except Exception as e:
        if driver:
            print("Page source for debugging:")
            print(driver.page_source[:500])  # Print first 500 characters
        print(f"Test failed: {e}")
        return False

    finally:
        if driver:
            driver.quit()

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
