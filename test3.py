def test3(url):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from time import sleep
    from browser_tools import browser_start, browser_close
    from check_parameters import check_parameters
    
    print ('Running test 3: checking section heading, checking that Option 1 is the default drop down list section.')
    driver = browser_start(url)
    wait = WebDriverWait(driver, 2)
    wait.until(EC.visibility_of_element_located((By.ID, 'test-3-div'))) # wait for the page to load
    heading3 = driver.find_element(By.CSS_SELECTOR, '#test-3-div>h1').text
    expected_test3_heading = 'Test 3'
    check_parameters('Section heading', expected_test3_heading, heading3)
    expected_dropdown_item = 'Option 1'
    dropdown_item = driver.find_elements(By.CSS_SELECTOR, '.dropdown')[0].text
    check_parameters('Option 1', expected_dropdown_item, dropdown_item)
    dropdown = driver.find_elements(By.CSS_SELECTOR, '.dropdown>button.btn')[0]
    dropdown_item_select = driver.find_elements(By.CSS_SELECTOR, '.dropdown-item')[2]
    ActionChains(driver).move_to_element(dropdown).click(dropdown).perform()
    ActionChains(driver).move_to_element(dropdown_item_select).click(dropdown_item_select).perform()
    #sleep(5)
    browser_close(driver)