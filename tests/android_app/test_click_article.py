from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_click_article(mobile_management):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Selene')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Selene'))

    with step('Click article'):
        elements = browser.all((AppiumBy.CLASS_NAME, 'android.view.ViewGroup'))
        desired_element = elements[2]
        desired_element.click()
