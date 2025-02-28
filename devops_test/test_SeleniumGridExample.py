from selenium import webdriver
"""1.download selenium grid jar
2.save in local folder and open the folder in cmd
3.C:\Nishant_Study\Software>java -jar selenium-server-4.28.0.jar standalone
4.we are getting the message at the last:INFO: Started Selenium Standalone 4.28.0 (revision ac34254): http://192.168.56.1:4444"""
def test_seleniumGrid():
    server = "http://localhost:4444/wd/hub"
    browserName="chrome"
    if browserName=="chrome":
        options = webdriver.ChromeOptions()
        #options.capabilities['platform'] == 'windows'
        options.platform_name = 'windows'
        options.capabilities['browserName'] == 'chrome'
        driver = webdriver.Remote(command_executor=server, options=options)
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(driver.title)
        driver.quit()
    elif browserName=="firefox":
        options = webdriver.FirefoxOptions()
        options.platform_name = 'windows'
        options.capabilities['browserName'] == 'firefox'
        driver = webdriver.Remote(command_executor=server, options=options)
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(driver.title)
        driver.quit()
    elif browserName=="internet":
        options = webdriver.IeOptions()
        options.platform_name = 'windows'
        options.capabilities['browserName'] == 'internet'
        driver = webdriver.Remote(command_executor=server, options=options)
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(driver.title)
        driver.quit()
    else:
        options = webdriver.EdgeOptions()
        options.platform_name = 'windows'
        options.capabilities['browserName'] == 'edge'
        driver = webdriver.Remote(command_executor=server, options=options)
        driver.maximize_window()
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(driver.title)
        driver.quit()


