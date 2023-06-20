def get_cell(driver, row, col):
    from selenium.webdriver.common.by import By
    tb = driver.find_elements(By.CSS_SELECTOR, '.table>tbody')[0]
    row_info = tb.find_elements(By.TAG_NAME, 'tr')[row]
    cell = row_info.find_elements(By.TAG_NAME, 'td')
    if len(cell) == 0:
        return "Calling index out of bounds"
    else:
        return cell[col].text