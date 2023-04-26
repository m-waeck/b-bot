from lib2to3.pgen2 import driver import time
from selenium import webdriver from selenium.webdriver.support.ui import WebDriverWait from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_ conditions as EC from selenium.webdriver.chrome.service import Service as ChromeService from webdriver_manager.chrome import ChromeDriverManager from selenium.webdriver.common.keys import Keys from selenium.webdriver.common.action_chains import ActionChains from selenium.webdriver.chrome.options import Options
chrome_options = Options ()
chrome_options.add_experimental_option("detach", True) def main:
This is the badenova bot.
It's opening the badenova pv rechner website and filling in the address and parameters.
try:
### open website
url_pv_rechner = "https: //www.badenova. de/pv-rechner/"
driver = get_driver()
driver.get(url_pv_rechner)
driver.maximize_window()
### reject cookies
WebDriverWait(driver, 10) .until(EC.element_to_be_clickable( (By.ID, 'onetrust-reject-all-handler'))).click()
### enter address
WebDriverWait(driver, 10).untilEC.visibility_of_element_located ( (By. CLASS_NAME, 'mapboxgl-ctrl-geocoder--
input '))).send_keys ("Habsburgerstraße 13a, Freiburg")
### select address from dropdown
WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.CLASS_NAME, 'suggestions')))
driver. find_element (By. XPATH,
"/ul[@class="suggestions"]/li[@class=" active"]').click()
### click search button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable( (By.CLASS_NAME, 'greenventory-search-
button'))).click()
### confirm address
# locate button
WebDriverWait (driver, 30).until(EC.presence_of_element_located ( (By.CLASS _NAME, 'css-1894ib')))
# wait until text is gone
WebDriverwait(driver, 30).untilEC.invisibility_of_element_located ( (By.CLASS_NAME,
'text")))
time.sleep (1)
# wait until
text2 is gone
WebDriverWait (driver, 30).until(EC.invisibility_of_element_located ( (By.CLASS_NAME, 'text2')))
# click button to confirm address
WebDriverWait(driver, 30).until(EC.visibility_of_element_located ( (By.CLASS_NAME, 'css-i894ib'))).click()
### click button to get to questions
WebDriverWait(driver, 10).until(EC.visibility_of_element_located ( (By.CLASS_NAME, 'css-i4qdph'))).click()
### first page
# click tabs to go through questions
time. sleep(1)
actions = ActionChains driver)
actions.send_keys (Keys.TAB * 11)
actions.perform ()
time.sleep (1)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located ((By.CLASS_NAME, 'css-i4qdph'))).click()
### second page
# click tabs to go through questions
time.sleep (1)
actions = ActionChains (driver)
actions.send_keys (Keys.TAB * 18)
actions.perform ()
# click continue button
time.sleep (1)
WebDriverWait(driver, 10) .until(EC.visibility_of_element_located( (By.CLASS_NAME, 'css-i4qdph'))).click()
# TODO: remove focus from url bar
print ("badenova bot done. Enjoy your energy!")
except Exception as e:
print (f"An Expection occured: \n{e}")
def get driver():
return driver
driver = webdriver. Chrome(service=ChromeService(ChromeDriverManager).install()), chrome_options=chrome_options)
return driver
if __name__ == '__main__':
main()