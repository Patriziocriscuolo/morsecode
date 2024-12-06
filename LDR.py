import pyvisa

# ASRL13::INSTR
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


device = rm.open_resource(
    "ASRL13::INSTR", read_termination="\r\n", write_termination="\n"
)


def get_output_value():
    """Get the value at which the arduino was previously set

    Returns:
        int: ADC value at which arduino was set
    """
    set_value = device.query("OUT:CH0?")
    return set_value


print(get_output_value())
