from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time  

PATH = r'C:\Program Files (x86)\msedgedriver.exe'

edge_options = webdriver.EdgeOptions()

edge_service = Service(PATH)
driver = webdriver.Edge(service=edge_service, options=edge_options)

driver.get("https://www.jumia.co.ke")
link = driver.find_element_by_link_text("Fashion")