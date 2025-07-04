import sys
import argparse
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_scores_service(url="http://localhost:8888", timeout=10):
    driver = None
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options=options)
        driver.get(url)

        score_element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.ID, "score"))
        )

        score_text = score_element.text.strip()
        try:
            score = int(score_text)
        except ValueError:
            print(f"Score value is not an integer: '{score_text}'")
            return False

        return 1 <= score <= 1000

    except Exception as e:
        if driver:
            print("Page source for debugging:")
            print(driver.page_source[:500])  # Print first 500 chars
        print(f"Test failed: {e}")
        traceback.print_exc()
        return False

    finally:
        if driver:
            driver.quit()

def main():
    parser = argparse.ArgumentParser(description="E2E test for scores service")
    parser.add_argument("--url", default="http://localhost:8888", help="URL of the scores service")
    args = parser.parse_args()

    result = test_scores_service(url=args.url)
    if result:
        print("Test Passed")
        sys.exit(0)
    else:
        print("Test Failed")
        sys.exit(-1)

if __name__ == "__main__":
    main()
