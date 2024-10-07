from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pyautogui

# Setup 
download_dir = r"C:\path\to\directory\Downloaded from CML" 
cdsw_user = 'your_username'
cdsw_pssw = 'your_password'

# Chrome preferences
chrome_options = webdriver.ChromeOptions()                  # chrome driver
chrome_options.add_argument("--start-maximized")            # my preference

# my preferences
prefs = {
    "download.default_directory": download_dir,  
    "download.prompt_for_download": False,       
    "directory_upgrade": True,
    "safebrowsing.enabled": True                 
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("http://your_dsw_address/")

# 1) Login page to load and find 'username' and 'password' fields
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
username_input = driver.find_element(By.NAME, "login")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys(cdsw_user)
password_input.send_keys(cdsw_pssw)

login_button = driver.find_element(By.CLASS_NAME, "cdsw-button")
login_button.click()

# Wait for load speed
time.sleep(5)

# 2) Navigate to the file is stored
# Select 'Project'
folder1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/your_username/your_project_name_on_cdsw']")))
folder1.click()

# 3) Select 'Files' nav
folder2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/your_username/your_project_name_on_cdsw/files/']")))
folder2.click()

# 4) Select desired folder 
folder3 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='http://your_dsw_address/your_username/your_project_name_on_cdsw/files/your_project_folder/']")))
folder3.click()

# 5) Click 'Last Modified' TWICE to sort by ascending order first, then sort by descending.
last_modified_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Last Modified')]")
last_modified_button.click()

last_modified_button_desc = driver.find_element(By.XPATH, "//button[contains(text(), 'Last Modified')]")
last_modified_button_desc.click()

# Checking the descending arrow before move on
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//i[@class='fa fa-angle-down ml5 ng-scope']")) )

# 6) Select the SECOND file (latest one) after sorting -- in this case, not every case.
latest_file_selected = driver.find_element(By.XPATH, "(//a[@class='ng-binding'])[2]")
latest_file_selected.click()

# 7) Click the Download button
download_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@tooltip='Download File']"))
    )
download_link.click()

# wait for download prompt is up
time.sleep(5)

# 8) Coordinates for the "Keep" button -- using pyautogui to find your mouse coordinate. different monitor size, different mouse's coordinates.
keep_button_x = 1203
keep_button_y = 109 

# 9) Click the "Keep" button which shown in Chrome
pyautogui.click(keep_button_x,keep_button_y)
print(f"The file has been downloaded into '{download_dir}'.")

time.sleep(5)

# Close the browser
driver.quit()
