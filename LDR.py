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


def meet_LDR():
    LDR = rm.open_resource(
        "ASRL13::INSTR", read_termination="\r\n", write_termination="\n"
    )
    # meer licht is minder weerstrand, V = IR, dus de I wordt groter en V kleiner, meet V
    LDR.query("OUT:CH0 1023")
    ADC_res = int(LDR.query("MEAS:CH2?"))  # meet ADC voor resistor
    ADC_tot = int(LDR.query("MEAS:CH1?"))  # meet ADC voor alles
    voltage_LDR = (ADC_tot - ADC_res) / 1023 * 3.3
    print(voltage_LDR)

    # als LED aan staat is LDR ongeveer 2.087096774193548
    # als LED uit staat is LDR ongeveer 2.7806451612903227


meet_LDR()
