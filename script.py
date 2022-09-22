from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as soup
from selenium.webdriver.support import expected_conditions as EC

wd = webdriver.Chrome(ChromeDriverManager().install())

URL = ''

wd.get(URL)

try:
    wait = WebDriverWait(wd,20)
    element = wait.until(EC.visibility_of_element_located(By.CLASS_NAME, "raw-html"))

    html_page = wd.page_source
    wd.quit()

    page = soup(html_page,'html.parser')

    # find elements, varies by page
    elems = wd.find_elements_by_tag_name('a')
    for elem in elems:
        href = elem.get_attribute('href')
        print(href)
finally:
    wd.quit()
