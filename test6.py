def test6(url):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from browser_tools import browser_start, browser_close
    from check_parameters import check_parameters
    from get_cell import get_cell
    
    print ('Running test 6: checking section heading, check contents of table cell 2, 2.')
    url = 'C:/Users/dpenn/Desktop/Projects/Resolver/QE-index.html'
    driver = browser_start(url)
    wait = WebDriverWait(driver, 2)
    wait.until(EC.visibility_of_element_located((By.ID, 'test-6-div'))) # wait for the page to load
    expected_test6_heading = 'Test 6'
    heading6 = driver.find_element(By.CSS_SELECTOR, '#test-6-div>h1').text
    check_parameters('Section heading', expected_test6_heading, heading6)
    expected_table_value = 'Ventosanzap'
    actual_value = (get_cell(driver, 2, 2))
    check_parameters('Cell 2 2 contents', expected_table_value, actual_value)
          