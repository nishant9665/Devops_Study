import pytest
from selenium import webdriver
# pytest -v -s .\test_GridParallelExecutions.py -n 12
# this test executed on grid total executed is 16
# Allure report run the below command-
# pytest -v -s .\test_GridParallelExecutions.py -n 12 --alluredir="C:\Nishant_Study\nopcommerce\nopcommerceAdmin\Cloud-Grid\report"
# open the allure report , first search allure.bat file then type cmd like-
#C:\Users\user\scoop\apps\allure\2.32.0\bin>allure serve C:\Nishant_Study\nopcommerce\nopcommerceAdmin\Cloud-Grid\report
#Generating report to temp directory...
@pytest.mark.parametrize('num',range(4))
def test_seleniumGrid(num):
        print(num)
        server = "http://localhost:4444/wd/hub"
        options = webdriver.ChromeOptions()
        #options.capabilities['platform'] == 'windows'
        options.platform_name = 'windows'
        options.capabilities['browserName'] == 'chrome'
        driver = webdriver.Remote(command_executor=server, options=options)
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(driver.title)
        driver.quit()

@pytest.mark.parametrize('num', range(4))
def test_seleniumGrid2(num):
        print(num)
        server = "http://localhost:4444/wd/hub"
        options = webdriver.FirefoxOptions()
        options.platform_name = 'windows'
        options.capabilities['browserName'] == 'firefox'
        driver = webdriver.Remote(command_executor=server, options=options)
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(driver.title)
        driver.quit()
@pytest.mark.parametrize('num',range(4))
def test_seleniumGrid3(num):
        print(num)
        server = "http://localhost:4444/wd/hub"
        options = webdriver.EdgeOptions()
        options.platform_name = 'windows'
        options.capabilities['browserName'] == 'edge'
        driver = webdriver.Remote(command_executor=server, options=options)
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(driver.title)
        driver.quit()




