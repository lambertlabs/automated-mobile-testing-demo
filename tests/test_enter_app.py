def test_open_app(app_driver):
    app_driver.implicitly_wait(10)

    # by resource id
    app_driver.find_element_by_id('YesButton').click()

    # by UiSelector
    ui_selector = 'new UiSelector().textContains("OK")'
    app_driver.find_element_by_android_uiautomator(ui_selector).click()

    # Appium interacts with the Android OS, not just the app
    resource_id = 'com.android.packageinstaller:id/permission_deny_button'
    app_driver.find_element_by_id(resource_id).click()

    ui_selector = 'new UiSelector().textContains("I agree")'
    app_driver.find_element_by_android_uiautomator(ui_selector)

    # Press "Back" key.
    # See https://developer.android.com/reference/android/view/KeyEvent.html for keycodes
    app_driver.press_keycode(4)

    app_driver.find_element_by_id('ButtonPlay')
