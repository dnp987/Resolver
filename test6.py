def test6(url,data_sheet):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from browser_tools import browser_start, browser_close
    from check_parameters import check_parameters
    from get_cell import get_cell
    from excel_utils import Excel_utils
    
    print ('Running test 6: checking section heading, check contents of table cell 2, 2.')
    driver = browser_start(url)
    test6_data = Excel_utils(data_sheet, 'test6', 'in')
    wait = WebDriverWait(driver, 2)
    page_load_element = test6_data.sht.cell(2,1).value
    wait.until(EC.visibility_of_element_located((By.ID, page_load_element))) # wait for the page to load
    expected_test6_heading = test6_data.sht.cell(2,2).value
    heading6_element = test6_data.sht.cell(2,3).value
    heading6 = driver.find_element(By.CSS_SELECTOR, heading6_element).text
    check_parameters('Section heading', expected_test6_heading, heading6)
    expected_table_value = test6_data.sht.cell(2,4).value
    actual_value = (get_cell(driver, 2, 2))
    check_parameters('Cell 2 2 contents', expected_table_value, actual_value)
    browser_close(driver)