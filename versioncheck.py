import json
import requests
from log import log
from time import sleep

class get:
    def __init__(self) -> None:
        with open("version.json") as f:
            self.options = json.load(f)

    def creatorname(self) -> str:
        """
        Retrieves the creators name.

        Returns:
            str: Example of creatorname: "N4GR"
        """
        return self.options["creator"]
    
    def creatorlink(self) -> str:
        """
        Retrieves the creators name.

        Returns:
            str: Example of creatorlink: "https://github.com/N4GR"
        """
        return self.options["creator_link"]
    
    def version(self) -> int:
        """
        Retrieves the current version.

        Returns:
            int: Example of version: 2
        """
        return self.options["version"]
    
    def reponame(self) -> str:
        """
        Retrieves the repository name.

        Returns:
            str: Example of reponame: "Fortnite-Lego-AFK-XP"
        """
        return self.options["repo_name"]

class versioning:
    def __init__(self) -> None:
        self.response = self.checkConnection()[1]
        self.connection = self.checkConnection()[0]
        
    def checkConnection(self) -> tuple[bool | dict]:
        """
        Checks if the user is connected to the internet.

        Returns:
            tuple(bool, dict): True if successful connection, False if not. Also returns dict of response.
        """
        try:
            response = requests.get(f"https://api.github.com/repos/{get().creatorname()}/{get().reponame()}/releases/latest", timeout = 5)
            return True, response
        except requests.ConnectionError:
            return False

    def latestVersion(self) -> str:
        """
        Retrieves the latest version from github.

        Returns:
            str: Example of latestversion: "v2"
        """
        return self.response.json()["tag_name"]

    def version_check(self) -> bool:
        """
        Checks if the latest version from github is the same as the currently installed version.

        Returns:
            bool: True if the version is the same, False if the connection failed or the version isn't the same.
        """

        if self.connection is False:
            return False, "connection-fail"
        
        if get().version() != self.latestVersion():
            return False, "different-version"
        else:
            return True, "Complete"

if __name__ == "__main__":
    check = versioning()
    version_check = check.version_check()
    successful_connection = version_check[0]
    connection_note = version_check[1]

    if successful_connection is False and connection_note == "different-version":
        print(log().error(f"NOT RUNNING THE LATEST VERSION\n"))
        print(log().error(f"Your version: v{get().version()}"))
        print(log().error(f"latest version: {check.latestVersion()}\n"))
        print(log().error(f"The newest version can be found here: {get().creatorlink()}/{get().reponame()}/releases/latest"))
        input(log().error("Press enter to continue anyway..."))
    else:
        print(log().success(f"Passed version check"))
        sleep(2)