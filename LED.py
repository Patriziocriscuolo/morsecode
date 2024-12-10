import time

import pyvisa

# Create a ResourceManager instance to manage VISA resources
rm = pyvisa.ResourceManager("@py")


def list_resources():
    """List all available VISA resources.

    This function queries the VISA ResourceManager for connected devices and returns
    their addresses.

    Returns:
        list: A list of strings representing the addresses of available resources.
    """
    port = rm.list_resources()
    return port


def kort(device):

    device.query("OUT:CH0 1023")
    time.sleep(0.5)
    device.query("OUT:CH0 0")
    time.sleep(0.3)


def lang(device):

    device.query("OUT:CH0 1023")
    time.sleep(1)
    device.query("OUT:CH0 0")
    time.sleep(0.3)




class text:
    def __init__(self):
        self.device = rm.open_resource(
            "ASRL8::INSTR", read_termination="\r\n", write_termination="\n"
        )

        # Morse-code vertaling (A-Z, 0-9) met "kort" voor punt en "lang" voor streep
        self.alfa = {
            "A": "kort lang",
            "B": "lang kort kort kort",
            "C": "lang kort lang kort",
            "D": "lang kort kort",
            "E": "kort",
            "F": "kort kort lang kort",
            "G": "lang lang kort",
            "H": "kort kort kort kort",
            "I": "kort kort",
            "J": "kort lang lang lang",
            "K": "lang kort lang",
            "L": "kort lang kort kort",
            "M": "lang lang",
            "N": "lang kort",
            "O": "lang lang lang",
            "P": "kort lang lang kort",
            "Q": "lang lang kort lang",
            "R": "kort lang kort",
            "S": "kort kort kort",
            "T": "lang",
            "U": "kort kort lang",
            "V": "kort kort kort lang",
            "W": "kort lang lang",
            "X": "lang kort kort lang",
            "Y": "lang kort lang lang",
            "Z": "lang lang kort kort",
            "1": "kort lang lang lang lang",
            "2": "kort kort lang lang lang",
            "3": "kort kort kort lang lang",
            "4": "kort kort kort kort lang",
            "5": "kort kort kort kort kort",
            "6": "lang kort kort kort kort",
            "7": "lang lang kort kort kort",
            "8": "lang lang lang kort kort",
            "9": "lang lang lang lang kort",
            "0": "lang lang lang lang lang",
            " ": " ",
        }

    def morse(self, text):
        for char in text.upper():
            print(char)
            if char in self.alfa:
                morse_code = self.alfa[char]
                for woord in morse_code.split():
                    if woord == "kort":
                        kort(self.device)
                    elif woord == "lang":
                        lang(self.device)
                time.sleep(0.4)
                self.device.write("")
                time.sleep(0.6)
