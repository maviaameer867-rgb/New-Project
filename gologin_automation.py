import time
from gologin import GoLogin
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Your GoLogin API token
API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NmFhNjk1MjI2M2EzZDdkNjU3NjYxY2EiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NzA4MDYwOGYwZDkzMzYxMzlhZWQ4YTcifQ.UC33raqIjbFMZhO4Gd2IU-9QgdhThJ47bGCeepY1D8w"

# The ID of the GoLogin profile you want to use
PROFILE_ID = "665c9952c62851d488aace9d"

# The local path to the Chrome extension you want to load
# Make sure to use forward slashes (/) or double backslashes (\\) in the path
EXTENSION_PATH = "C:/Users/soban/.gologin/extensions/chrome-extensions/igaclmimgmfeodenomlhngfjbbppfnng@2_0_57_0"

def main():
    """
    This is the main function of the script.
    It starts a GoLogin profile, connects to it with Selenium,
    and performs some automated actions.
    """
    gl = None
    driver = None
    try:
        # Initialize GoLogin with your token and profile ID
        # We also pass the extension path using the 'extra_params' option
        gl = GoLogin({
            "token": API_TOKEN,
            "profile_id": PROFILE_ID,
            "extra_params": [f"--load-extension={EXTENSION_PATH}"]
        })

        # Start the GoLogin profile and get the debugger address
        print("Starting GoLogin profile...")
        debugger_address = gl.start()
        print(f"GoLogin profile started with debugger address: {debugger_address}")

        # Add a delay to allow the browser to fully initialize
        print("Waiting for 5 seconds for the browser to initialize...")
        time.sleep(5)

        # Create Chrome options and set the debugger address
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", debugger_address)

        # Get the Chromium version for the webdriver
        chromium_version = gl.get_chromium_version()

        # Install the webdriver
        service = Service(ChromeDriverManager(driver_version=chromium_version).install())

        # Connect to the browser using Selenium
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Now you can control the browser with Selenium
        print("Navigating to https://gologin.com...")
        driver.get("https://gologin.com")

        # You can add your automation logic here
        # For example, find elements and interact with them
        print("Page title:", driver.title)

        # Keep the browser open for a while to see the result
        print("Waiting for 30 seconds...")
        time.sleep(30)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Stop the GoLogin profile and close the browser
        if driver:
            print("Closing the browser...")
            driver.quit()
        if gl:
            print("Stopping GoLogin profile...")
            gl.stop()
        print("Script finished.")

if __name__ == "__main__":
    main()
