import inquirer
import pyfiglet
from simple_chalk import chalk
import secureSystemHandler


# On Start
secure = secureSystemHandler.SSHandler
if secure.token() == "none":
    secure.auth()
else:
    pass

secure.clear()

# Vars
rawLogo = pyfiglet.figlet_format("Secure")
logo = chalk.bold.blue(rawLogo)
rawSideLogo = pyfiglet.figlet_format("System")
sideLogo = chalk.bold.green(rawSideLogo)

# Display
print(logo, sideLogo)

interface = [
    inquirer.Confirm("run", message="You want to run SecureSystem"),
]

status = inquirer.prompt(interface)
secure.readyToActivateHiddenCam(status["run"])

print(chalk.yellow("\nSecureSystem is ready to launch!..."))
print(chalk.green("SecureSystem is launched!"))
print(
    chalk.yellow.bold("Note:")
)

secure.copyright()

secure.activateHiddenCam()
