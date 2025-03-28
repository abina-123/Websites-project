from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a new instance of ChromeDriver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://demowebshop.tricentis.com")
time.sleep(2)

# Maximize the window
driver.maximize_window()

# Get the title of the webpage
myTitle = driver.title
print("Title of the webpage:", myTitle)

# Get the current URL
currentUrl = driver.current_url
print("Current URL:", currentUrl)

driver.find_element(By.XPATH, "(//a)[2]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//label[text()='Female']").click()
time.sleep(1)


name_textfield = driver.find_element(By.ID, "FirstName")
name_textfield.send_keys("Abina")
time.sleep(2)

name_textfield = driver.find_element(By.ID, "LastName")
name_textfield.send_keys("A")
time.sleep(2)

driver.find_element(By.ID, "Email").send_keys("aabina1006@gmail.com")
time.sleep(2)

driver.find_element(By.ID, "Password").send_keys("Abi@1000")
time.sleep(2)

driver.find_element(By.ID, "ConfirmPassword").send_keys("Abi@1000")
time.sleep(2)


driver.find_element(By.XPATH, "//input[@name='register-button']").click()
time.sleep(2)

driver.find_element(By.XPATH, "(//a)[6]").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//a)[7]").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//a)[11]").click()
time.sleep(2)

driver.find_element(By.XPATH, "(//a)[14]").click()
time.sleep(2)

driver.find_element(By.XPATH, "(//a)[15]").click()
time.sleep(2)

driver.find_element(By.XPATH, "(//a)[16]").click()
time.sleep(2)

driver.find_element(By.XPATH, "(//a)[17]").click()
time.sleep(2)

# Quit the WebDriver session
driver.quit()
