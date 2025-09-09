from gologin import GoLogin

# Your GoLogin API token
API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NmFhNjk1MjI2M2EzZDdkNjU3NjYxY2EiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NzA4MDYwOGYwZDkzMzYxMzlhZWQ4YTcifQ.UC33raqIjbFMZhO4Gd2IU-9QgdhThJ47bGCeepY1D8w"

# The ID of the GoLogin profile you want to use
PROFILE_ID = "665c9952c62851d488aace9d"

# The local path to the Chrome extension you want to load
# Make sure to use forward slashes (/) or double backslashes (\\) in the path
EXTENSION_PATH = "C:/Users/soban/.gologin/extensions/chrome-extensions/igaclmimgmfeodenomlhngfjbbppfnng@2_0_57_0"

def main():
    """
    This script launches a GoLogin profile and keeps it open for manual use.
    """
    gl = None
    try:
        # Initialize GoLogin with your token, profile ID, and extension path
        gl = GoLogin({
            "token": API_TOKEN,
            "profile_id": PROFILE_ID,
            "extra_params": [f"--load-extension={EXTENSION_PATH}"]
        })

        # Start the GoLogin profile. This will open the browser window.
        print("Starting GoLogin profile...")
        gl.start()
        print("Profile is running. The browser window should be open on your desktop.")

        # Keep the script running so the browser stays open.
        # The user can press Enter in the terminal when they are done.
        input("Press Enter in this terminal to close the profile and exit.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Stop the GoLogin profile to close the browser and end the session.
        if gl:
            print("Closing GoLogin profile...")
            gl.stop()
            print("Profile session stopped.")
        print("Script finished.")

if __name__ == "__main__":
    main()
