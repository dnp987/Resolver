def test4(url,data_sheet):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from time import sleep
    from browser_tools import browser_start, browser_close
    from check_parameters import check_parameters
    from excel_utils import Excel_utils
    
    print ('Running test 4: checking section heading, checking that first button is enabled and the second one disabled.')
    driver = browser_start(url)
    test4_data = Excel_utils(data_sheet, 'test4', 'in')
    wait = WebDriverWait(driver, 2)
    page_load_element = test4_data.sht.cell(2,1).value
    wait.until(EC.visibility_of_element_located((By.ID, page_load_element))) # wait for the page to load
    expected_test4_heading =  test4_data.sht.cell(2,2).value
    heading4_element = test4_data.sht.cell(2,3).value
    heading4 = driver.find_element(By.CSS_SELECTOR, heading4_element).text
    check_parameters('Section heading', expected_test4_heading, heading4)
    button_element = test4_data.sht.cell(2,4).value
    buttons = driver.find_elements(By.CSS_SELECTOR, button_element)
    for index, button in enumerate(buttons):
        disabled = button.get_attribute('disabled')
        if disabled:
            print ('Button',index,'is disabled')
        else:
            print ('Button',index,'is enabled')
    browser_close(driver)