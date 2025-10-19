def test_login_positive(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element("id", "username").send_keys("tomsmith")
    driver.find_element("id", "password").send_keys("SuperSecretPassword!")
    driver.find_element("css selector", "button[type='submit']").click()

    flash = driver.find_element("id", "flash").text
    assert "You logged into a secure area!" in flash
