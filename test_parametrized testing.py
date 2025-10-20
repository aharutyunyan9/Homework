import pytest
from selenium.webdriver.common.by import By
import time

# Parametrize with multiple username/password combos
@pytest.mark.parametrize("username, password, expected_message", [
    ("validuser@example.com", "ValidPassword123", "Welcome"),
    ("invaliduser@example.com", "WrongPassword", "Invalid username or password"),  # Expected failure
    ("", "", "Please fill out this field")
])
def test_demoqa_login(driver, username, password, expected_message):
    driver.get("https://demoqa.com/login")
    time.sleep(2)

    user_input = driver.find_element(By.ID, "userName")
    pass_input = driver.find_element(By.ID, "password")

    user_input.clear()
    pass_input.clear()

    user_input.send_keys(username)
    pass_input.send_keys(password)

    driver.find_element(By.ID, "login").click()
    time.sleep(2)


    try:
        # Successful login redirects to profile page
        profile_username = driver.find_element(By.ID, "userName-value").text
        assert username in profile_username
        print(f" Login successful for {username}")
    except:
        # Failed login shows error message
        error_message = driver.find_element(By.ID, "name").text
        assert expected_message in error_message
        print(f"Login failed for {username}: {error_message}")