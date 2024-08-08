from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    driver.get("https://new.maqraa.sa/student")

    username_input = driver.find_element(By.ID, "email")
    username_input.send_keys("farouk.o.haroun@gmail.com")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("password")

    login_button = driver.find_element(By.CLASS_NAME, "bg-blue")
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".episode.row.justify-between.center-flex.baby-blue-bg.padding-30"))
    )
    print("Login successful, and the page is fully loaded.")

    driver.get("https://new.maqraa.sa/student")

    start_time = time.time()
    max_wait_time = 30 * 60

    while True:
        try:
            link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.row.justify-center.center-flex"))
            )
            link.click()
            print("Link clicked. Checking the result...")

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "expected-element-on-new-page"))
            )
            print("Navigation successful and destination page is loaded.")
            break

        except Exception as e:
            elapsed_time = time.time() - start_time
            if elapsed_time > max_wait_time:
                print("Time limit exceeded. Exiting the script.")
                break
            else:
                print(f"Exception: {e}. Retrying...")
                time.sleep(5)

finally:
    driver.save_screenshot("debug_screenshot.png")
    driver.quit()

