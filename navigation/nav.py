from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time  
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = r'C:\Program Files (x86)\msedgedriver.exe'
edge_options = webdriver.EdgeOptions()
edge_service = Service(PATH)
driver = webdriver.Edge(service=edge_service, options=edge_options)
driver.get("https://www.egerton.ac.ke")
link = driver.find_element(By.LINK_TEXT, 'Virtual Tour | Gather to learn')
link.click()


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Virtual Tour | Gather to learn'))
    )
    # element.clear()
    element.click()
    element.click()
  
except:
    driver.quit()

