import os
from dotenv import load_dotenv

def version():
    """
    Returns the version of the hivebox application.
    This function retrieves the version information from the .env file.
    """

    # Load environment variables from .env file
    load_dotenv()

    # Retrieve the application version from environment variables
    app_version = os.getenv("APP_VERSION")
    return app_version

def main():
    """
    Main function for the hivebox application.
    This function serves as the entry point for the application.
    """
    print(f"Hello from hivebox! Version: {version()}")


if __name__ == "__main__":
    main()
