from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    page.wait_for_load_state()

    # Заполняем поле email
    email_input = page.locator('//input[@id=":r0:"]')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input = page.locator('//input[@id=":r1:"]')
    username_input.fill("username")

    # Заполняем поле password
    password_input = page.locator('//input[@id=":r2:"]')
    password_input.fill("password")

    # Кликаем на кнопку registration
    reg_link = page.locator('//button[@id="registration-page-registration-button"]')
    reg_link.click()

    page.wait_for_load_state()

    # Проверка текста Dashboard
    dashboard_text = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_text).to_have_text('Dashboard')

    page.wait_for_timeout(5000)
