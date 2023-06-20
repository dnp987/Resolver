#if __name__ == '__main__':
def test2():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from time import sleep
    from browser_tools import browser_start, browser_close
    from check_parameters import check_parameters
    
    print ('Running test 2: checking section heading, checking that section list has three entries, second item and badge.')     
    url = 'C:/Users/dpenn/Desktop/Projects/Resolver/QE-index.html'
    driver = browser_start(url)
    wait = WebDriverWait(driver, 2)
    wait.until(EC.visibility_of_element_located((By.ID, 'test-2-div'))) # wait for the page to load
    expected_test2_heading = "Test 2"
    expected_list_item2 = "List Item 2"
    expected_list_item2_badge = '6'
    heading2 = driver.find_element(By.CSS_SELECTOR, '#test-2-div>h1').text
    check_parameters("Section heading", expected_test2_heading, heading2)
    list_items = driver.find_elements(By.CSS_SELECTOR, 'li.list-group-item')
    list_num = 3
    if len(list_items) == list_num:
        print (list_num,'list items found as expected')
    else:
        print ('Expected',list_num,'items, found',len(list_items))
            
    list_item2 = (driver.find_elements(By.CSS_SELECTOR, 'ul.list-group>li.list-group-item:nth-child(2)')[0].text)[:-1]
    check_parameters('List group', expected_list_item2, list_item2)

    list_item2_badge = driver.find_elements(By.CSS_SELECTOR, 'ul.list-group>li.list-group-item:nth-child(2)>span.badge')[0].text
    check_parameters('Second list item badge', expected_list_item2_badge, list_item2_badge)
   