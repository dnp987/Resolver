def test2(url, data_sheet):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from time import sleep
    from browser_tools import browser_start, browser_close
    from check_parameters import check_parameters
    from excel_utils import Excel_utils
    
    print ('Running test 2: checking section heading, checking that section list has three entries, second item and badge.')     
    driver = browser_start(url)
    test2_data = Excel_utils(data_sheet, 'test2', 'in')
    wait = WebDriverWait(driver, 2)
    page_load_element = test2_data.sht.cell(2,1).value
    wait.until(EC.visibility_of_element_located((By.ID, page_load_element))) # wait for the page to load
    expected_test2_heading = test2_data.sht.cell(2,2).value
    heading2_element = test2_data.sht.cell(2,3).value
    expected_list_item2 = test2_data.sht.cell(2,4).value
    expected_list_item2_badge = str(test2_data.sht.cell(2,5).value)
    heading2 = driver.find_element(By.CSS_SELECTOR, heading2_element).text
    check_parameters("Section heading", expected_test2_heading, heading2)
    list_item_element = test2_data.sht.cell(2,6).value
    list_items = driver.find_elements(By.CSS_SELECTOR, list_item_element)
    list_num = 3
    if len(list_items) == list_num:
        print (list_num,'list items found as expected')
    else:
        print ('Expected',list_num,'items, found',len(list_items))
    list_item_2_element = test2_data.sht.cell(2,7).value       
    list_item2 = (driver.find_elements(By.CSS_SELECTOR, list_item_2_element)[0].text)[:-1]
    check_parameters('List group', expected_list_item2, list_item2)
    badge_element = str(test2_data.sht.cell(2,8).value)
    list_item2_badge = driver.find_elements(By.CSS_SELECTOR, badge_element)[0].text
    check_parameters('Second list item badge', expected_list_item2_badge, list_item2_badge)
