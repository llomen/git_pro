#专门用来跑上报自动化和置灰的设备   IPadmini2
from appium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

dev = {
    "platformName": "iOS",
    "deviceName": "可妮兔",
    "platformVersion": "12.5.5",
    "udid": "77b67553903be3fe74a1b4a361a075260f545dca",
    "bundleId": "com.imgo.tv.hd",
    "noReset": "true",
    "AutomationName": "XCUITest",
    "xcodeOrgId": "WKQZHDVG49",
    "xcodeSigningId": "iPad Developer"
}

dev1={
  "platformName": "iOS",
  "deviceName": "可妮兔",
  "platformVersion": "10.0.2",
  "udid": "00008020-001A54623A04002E",
  "bundleId": "com.hunantv.imgotv",
  "noReset": "true",
  "AutomationName": "XCUITest",
  "xcodeOrgId": "WKQZHDVG49",
  "xcodeSigningId": "iPhone Developer"
}
#用来跑UI自动化的设备  IPad Pro4
dev2 = {
    "platformName": "iOS",
    "deviceName": "可妮兔",
    "platformVersion": "12.5.5",
    "udid": "f4168aea0d6a99829d75f3ea681f430ad71df1ea",
    "bundleId": "com.imgo.tv.hd",
    "noReset": "true",
    "AutomationName": "XCUITest",
    "xcodeOrgId": "WKQZHDVG49",
    "xcodeSigningId": "iPad Developer"
}


mail = 'testitv@163.com'
mail_secret = "888888"