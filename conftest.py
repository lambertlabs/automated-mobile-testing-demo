import os

import pytest
from appium import webdriver

EXECUTOR = "http://127.0.0.1:4723/wd/hub"
ANDROID_APP_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'android_apps')

apk_files = [file for file in os.listdir(ANDROID_APP_DIR) if file.endswith('.apk')]
assert len(apk_files) == 1, 'App directory can only contain one app file.'
ANDROID_APP_PATH = os.path.join(ANDROID_APP_DIR, apk_files.pop(0))


@pytest.fixture
def app_driver():
    driver = webdriver.Remote(
        command_executor=EXECUTOR,
        desired_capabilities={
            "app": ANDROID_APP_PATH,
            # Chess Free V3.02
            "appPackage": "uk.co.aifactory.chessfree",
            "appActivity": ".ChessFreeActivity",
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "Android Emulator",
            "automationName": "UiAutomator2",
        }
    )

    yield driver
    driver.quit()
