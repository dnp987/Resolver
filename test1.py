def test1(url):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from time import sleep
    from browser_tools import browser_start, browser_close
    from check_parameters import check_parameters
      
    print ('Running test 1: checking section heading, email address and password inputs, Login button.')    
    driver = browser_start(url)
    wait = WebDriverWait(driver, 2)
    wait.until(EC.visibility_of_element_located((By.ID, 'test-1-div'))) # wait for the page to load
    test_email = 'abc@test.com'
    test_password = 'abc123'
    expected_test1_heading = 'Test 1'
    heading1 = driver.find_element(By.CSS_SELECTOR, '#test-1-div>h1').text
    check_parameters('Section heading', expected_test1_heading, heading1)
    
    if driver.find_element(By.ID, 'inputEmail'):
        email = driver.find_element(By.ID, 'inputEmail')
        print ('Email address field found')
    else:
        print ('Email address field missing')
    #print (email.get_attribute('placeholder'))
    email.send_keys(test_email)
     
    if driver.find_element(By.ID, 'inputPassword'):
        password = driver.find_element(By.ID, 'inputPassword')
        print ('Password field found')
    else:
        print ('Password field missing')
    #print (password.get_attribute('placeholder'))
    password.send_keys(test_password)

    if driver.find_element(By.CLASS_NAME, 'btn'):
        sign_in_button = driver.find_element(By.CLASS_NAME, 'btn')
        print ('Sign in button found')
    else:
        print ('Sign in button missing')
    #print (sign_in_button.text)
    sign_in_button.click()
    browser_close(driver)