def test1(url, data_sheet):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from time import sleep
    from browser_tools import browser_start, browser_close
    from check_parameters import check_parameters
    from excel_utils import Excel_utils
      
    print ('Running test 1: checking section heading, email address and password inputs, Login button.')    
    driver = browser_start(url)
    test1_data = Excel_utils(data_sheet, 'test1', 'in')
    wait = WebDriverWait(driver, 2)
    page_load_element = test1_data.sht.cell(2,1).value
    wait.until(EC.visibility_of_element_located((By.ID, page_load_element))) # wait for the page to load
    test_email = test1_data.sht.cell(2,2).value
    test_password = test1_data.sht.cell(2,3).value
    expected_test1_heading = test1_data.sht.cell(2,4).value
    heading1_element = test1_data.sht.cell(2,5).value
    heading1 = driver.find_element(By.CSS_SELECTOR, heading1_element).text
    check_parameters('Section heading', expected_test1_heading, heading1)
    
    email_element = test1_data.sht.cell(2,6).value
    if driver.find_element(By.ID, email_element):
        email = driver.find_element(By.ID, email_element)
        print ('Email address field found')
    else:
        print ('Email address field missing')
    email.send_keys(test_email)

    password_element = test1_data.sht.cell(2,7).value     
    if driver.find_element(By.ID, password_element):
        password = driver.find_element(By.ID, password_element)
        print ('Password field found')
    else:
        print ('Password field missing')
    password.send_keys(test_password)

    button_element = test1_data.sht.cell(2,8).value
    if driver.find_element(By.CLASS_NAME, button_element):
        sign_in_button = driver.find_element(By.CLASS_NAME, button_element)
        print ('Sign in button found')
    else:
        print ('Sign in button missing')
    sign_in_button.click()
    browser_close(driver)