import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_sampleDemo():
    print("Hi this is my first circleCI ")
    print("Hi this is my second line circleCI ")
    driver = webdriver.Chrome(executable_path="D:\\selenium\\drivers\\chromedriver.exe")
    #driver = webdriver.Remote(
    #    command_executor='http://127.0.0.1:4444/wd/hub',
    #    desired_capabilities=DesiredCapabilities.CHROME)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    print("URL is OPEN")




