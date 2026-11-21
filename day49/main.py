from app import create_app

from automation.browser import create_browser
from automation.login import login_to_gym


def run_website():

    app = create_app()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False
    )


def run_automation():

    driver = create_browser()

    try:

        login_to_gym(driver)

        input("\nPress Enter to close browser...")

    except Exception as e:

        print("Automation failed:", e)

        driver.save_screenshot(
            "screenshots/login_error.png"
        )

        raise

    finally:

        driver.quit()


if __name__ == "__main__":

    run_automation()