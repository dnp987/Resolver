if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from time import sleep
    from browser_tools import browser_start, browser_close
    from check_parameters import check_parameters
    
    print ('Running test 4: checking section heading, checking that first button is enabled and the second one disabled.')
    url = 'C:/Users/dpenn/Desktop/Projects/Resolver/QE-index.html'
    driver = browser_start(url)
    wait = WebDriverWait(driver, 2)
    wait.until(EC.visibility_of_element_located((By.ID, 'test-4-div'))) # wait for the page to load
    expected_test4_heading = 'Test 4'
    heading4 = driver.find_element(By.CSS_SELECTOR, '#test-4-div>h1').text
    check_parameters('Section heading', expected_test4_heading, heading4)
    buttons = driver.find_elements(By.CSS_SELECTOR, '#test-4-div>.btn')
    for index, button in enumerate(buttons):
        disabled = button.get_attribute('disabled')
        if disabled:
            print ('Button',index,'is disabled')
        else:
            print ('Button',index,'is enabled')