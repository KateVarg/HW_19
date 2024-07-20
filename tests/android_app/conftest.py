import pytest
from appium.options.android import UiAutomator2Options
from appium import webdriver
from selene import browser
import os
from dotenv import load_dotenv
from hw_19.utils import attach


@pytest.fixture(autouse=True)
def load_env():
    load_dotenv()
    assert os.getenv("USERNAME") is not None, "USERNAME not set in environment"
    assert os.getenv("ACCESS-KEY") is not None, "ACCESS-KEY not set in environment"


@pytest.fixture(scope='function')
def mobile_management():
    username = os.getenv("USERNAME")
    access_key = os.getenv("ACCESS-KEY")

    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": username,
            "accessKey": access_key,
        }
    })

    browser.config.driver = webdriver.Remote('http://hub.browserstack.com/wd/hub', options=options)

    browser.config.timeout = float(os.getenv("TIMEOUT"))

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)
    attach.add_video(browser)

    browser.quit()
