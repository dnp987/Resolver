def browser_start(url):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options   
    driver = webdriver.Chrome() # Open Chrome
    driver.maximize_window() # maximize the browser window
    driver.get(url)
    return driver

def browser_close(driver):
    driver.quit()