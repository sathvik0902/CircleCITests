import pytest
from selenium import webdriver

def test_sampleDemo():
    print("Hi this is my first circleCI ")
    print("Hi this is my second line circleCI ")
    driver = webdriver.Chrome(executable_path="D:\\selenium\\drivers\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    print("URL is OPEN")
