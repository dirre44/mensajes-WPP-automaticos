from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.nasa.gov')
#headlines = driver.find_elements_by_css_selector('.hds-submenu-item.usa-nav__submenu-item')
headlines = driver.find_elements_by_class_name("maxw-tablet color-spacesuit-white")
for headline in headlines:
    print(headline.text.strip())
driver.close()