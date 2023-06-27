def test3(url,data_sheet):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains
    from time import sleep
    from browser_tools import browser_start, browser_close
    from check_parameters import check_parameters
    from excel_utils import Excel_utils
    
    print ('Running test 3: checking section heading, checking that Option 1 is the default drop down list section.')
    driver = browser_start(url)
    test3_data = Excel_utils(data_sheet, 'test3', 'in')
    wait = WebDriverWait(driver, 2)
    page_load_element = test3_data.sht.cell(2,1).value
    #wait.until(EC.visibility_of_element_located((By.ID, 'test-3-div'))) # wait for the page to load
    wait.until(EC.visibility_of_element_located((By.ID, page_load_element))) # wait for the page to load
    expected_test3_heading = test3_data.sht.cell(2,2).value
    heading3_element = test3_data.sht.cell(2,3).value
    #heading3 = driver.find_element(By.CSS_SELECTOR, '#test-3-div>h1').text
    heading3 = driver.find_element(By.CSS_SELECTOR, heading3_element).text
    #expected_test3_heading = 'Test 3'
    check_parameters('Section heading', expected_test3_heading, heading3)
    #expected_dropdown_item = 'Option 1'
    expected_dropdown_item = test3_data.sht.cell(2,4).value
    dropdown_item_element = test3_data.sht.cell(2,5).value
    #dropdown_item = driver.find_elements(By.CSS_SELECTOR, '.dropdown')[0].text
    dropdown_item = driver.find_elements(By.CSS_SELECTOR, dropdown_item_element)[0].text
    check_parameters('Option 1', expected_dropdown_item, dropdown_item)
    #dropdown = driver.find_elements(By.CSS_SELECTOR, '.dropdown>button.btn')[0]
    dropdown_button_element = test3_data.sht.cell(2,6).value
    dropdown = driver.find_elements(By.CSS_SELECTOR, dropdown_button_element)[0]
    dropdown_item_select_element = test3_data.sht.cell(2,7).value
    #dropdown_item_select = driver.find_elements(By.CSS_SELECTOR, '.dropdown-item')[2]
    dropdown_item_select = driver.find_elements(By.CSS_SELECTOR, dropdown_item_select_element)[2]
    ActionChains(driver).move_to_element(dropdown).click(dropdown).perform()
    ActionChains(driver).move_to_element(dropdown_item_select).click(dropdown_item_select).perform()
    browser_close(driver)