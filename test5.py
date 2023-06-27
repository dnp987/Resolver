def test5(url):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    import re
    from time import sleep
    from browser_tools import browser_start, browser_close
    from check_parameters import check_parameters

    print ('Running test 5: checking section heading, wait for button to be displayed, click it, and then check that is is disabled after clicking.')    
    driver = browser_start(url)
    wait = WebDriverWait(driver, 2)
    wait.until(EC.visibility_of_element_located((By.ID, 'test-5-div'))) # wait for the page to load
    expected_test5_heading = 'Test 5'
    heading5 = driver.find_element(By.CSS_SELECTOR, '#test-5-div>h1').text
    check_parameters('Section heading', expected_test5_heading, heading5)
    button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'test5-button')))
    button = driver.find_element(By.ID, 'test5-button')
    print (button.is_enabled())
    ActionChains(driver).move_to_element(button).click(button).perform()
    test5_alert = driver.find_elements(By.CSS_SELECTOR, '.alert')[0].text
    page_src = driver.page_source
    message_found = re.search(test5_alert, page_src)
    if (message_found != None):
        print ('Message found:',test5_alert)
    button = driver.find_element(By.ID, 'test5-button')
    if button.is_enabled:
        print ('Button is enabled')
    else:
        print ('Button is disabled')
    browser_close(driver)