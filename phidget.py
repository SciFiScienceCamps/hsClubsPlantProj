from Phidget22.Phidget import *
from Phidget22.Devices.DigitalInput import *
import time

def onStateChange(self, state):
	print("State [" + str(self.getHubPort()) + "]: " + str(state))

def main():
	digitalInput2 = DigitalInput()
	digitalInput4 = DigitalInput()

	digitalInput2.setIsHubPortDevice(True)
	digitalInput2.setHubPort(2)
	digitalInput4.setIsHubPortDevice(True)
	digitalInput4.setHubPort(4)

	digitalInput2.setOnStateChangeHandler(onStateChange)
	digitalInput4.setOnStateChangeHandler(onStateChange)

	digitalInput2.openWaitForAttachment(5000)
	digitalInput4.openWaitForAttachment(5000)

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	digitalInput2.close()
	digitalInput4.close()

main()