from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from elements import *
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

Stage_supplant_me = driver.get("https://stage.supplant.me")


# Find the site and wait until it stabilizes
# wait = webdriver(driver, timeout=30)
# element = wait.until(EC.element_to_be_selected(locator = (By.ID, "email")))



# Enter the username and password and log in to the main page
driver.find_element(By.ID, "email").send_keys("yedidya@supplant.me")
driver.find_element(By.ID, "password").send_keys("1q2w3e4r")

Submit = driver.find_element(By.ID, "submit-login-btn").click()

sleep(5)

driver.find_element(By.CSS_SELECTOR,'.MuiTreeItem-root GrowerItemStyled-gTCWDe kFJNvr').click()
sleep(5)
# driver.find_element(By.XPATH, "//div[contains(text(), 'RAIN - DO NOT TOUCH Yedidya Grower QA')]").click()
# //div[contains(text(), "RAIN - DO NOT TOUCH Yedidya Grower QA")]



driver.quit()