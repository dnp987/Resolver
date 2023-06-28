def browser_start(browser,url):
    from selenium import webdriver
    browser = browser.strip() # remove leading and trailing spaces
    browser = str(browser) # ensure that it's character data
    
    if browser == "Chrome":
        #from selenium.webdriver.chrome.options import Options   
        driver = webdriver.Chrome() # Open Chrome
    elif browser == "Firefox":
        driver = webdriver.Firefox()
    else:
        return False
            
    driver.maximize_window() # maximize the browser window
    driver.get(url)
    return driver

def browser_close(driver):
    driver.quit()