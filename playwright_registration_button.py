from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto(" https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверяем, что кнопка Registration не активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # Заполняем поле email
    email_input = page.locator('//input[@id=":r0:"]')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input = page.locator('//input[@id=":r1:"]')
    username_input.fill("username")

    # Заполняем поле password
    password_input = page.locator('//input[@id=":r2:"]')
    password_input.fill("password")

    expect(registration_button).to_be_enabled()

    page.wait_for_timeout(5000)
