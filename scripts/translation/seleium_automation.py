# Doesn't work

from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

options = webdriver.FirefoxOptions()
# options.add_argument("--window-size=1920,1080")  # set window size to native GUI size

driver = webdriver.Firefox(options=options)
driver.get("https://translate.google.com/?sl=kha&tl=en&text=hello&op=translate")

# element = WebDriverWait(driver=driver, timeout=5).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, 'span.ryNqvb'))
# )

print(driver.page_source)
