import time
import os
import json
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect
from simple_chalk import chalk
from urllib.request import urlopen


class SSHandler:
    def auth():
        # On Start
        SSHandler.clear()

        # This function will make token send to token function.

        APP_KEY = "2lo6jryu1oaqbrq"
        APP_SECRET = "jvzxnq5h9mp95bu"

        auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)

        authorize_url = auth_flow.start()

        print("\n1. Go to: " + authorize_url)
        print('2. Click "Allow" (you might have to log in first).')
        print("3. Copy the authorization code.\n")

        try:
            auth_code = input("Enter the authorization code here: ").strip()
        except KeyboardInterrupt:
            SSHandler.error(1)
        except:
            SSHandler.error(2)
        else:
            pass

        try:
            oauth_result = auth_flow.finish(auth_code)
        except Exception as e:
            print("Error: %s" % (e,))
            exit(1)

        dbx = dropbox.Dropbox(oauth2_access_token=oauth_result.access_token)
        account = dbx.users_get_current_account()

        print(chalk.green("Successfully Login!"), "\n")
        print(chalk.bold.blue("Welcome " + account.name.given_name))

        token = open("token.txt", "w")
        token.write(oauth_result.access_token)

    def token():
        try:
            token = open("token.txt", "r")
        except FileNotFoundError:
            token = open("token.txt", "w")
            SSHandler.auth()
            print("Try again by typing 'Python uploadFiles.py'")

            os.system("Python secureSystem.py")
        except:
            SSHandler.error(2)
        else:
            pass

        checkToken = token.read()

        if checkToken == "":
            access_token = "none"
            SSHandler.auth()
        else:
            access_token = checkToken

        return access_token

    def error(code) -> int:
        if code == 1:
            print("\n" + chalk.yellow("User exited!"))
            os._exit(0)
        elif code == 2:
            print("\n" + chalk.red("SomeThing Went Wrong?"))
            os._exit(1)
        elif code == 3:
            os._exit(0)
        else:
            code = 2

    def copyright():
        app = "Cloud Storage"
        copyRight = app + " Copyright © " + str(time.localtime().tm_year) + " Junaid"

        # Giving a line for Credits
        print("\n")
        # Credits
        print("This app is made by Junaid.")
        print(chalk.bgWhite.black(copyRight))

    def note():
        url = "https://api.npoint.io/c35bb5858b4c3561b0a6"
        response = urlopen(url)
        data_json = json.loads(response.read())

        return data_json["note"]

    def clear():
        # for windows
        if os.name == "nt":
            os.system("cls")

        # for mac and linux(if, os.name is 'posix')
        else:
            os.system("clear")

    def readyToActivateHiddenCam(status):
        file = open("SSController.txt", "w")
        file.write(str(status))
        file.close()

    def activateHiddenCam():
        os.system("Pythonw secureSystemHiddenCam.pyw")
