class Converting:
    def __init__(self) -> None:
        pass
    def TemperatureCtoF(self, Celsius):
        """
        In here we will convert Celsius into fahrenheit
        """
        #After a quick search i found this is formula
        # °F = °C * 1.8 + 32
        #I could also have used an online converter with an API
        #But I hate having to much PyPi dependencies in my python code

        Fahrenheit = (Celsius * 1.8) + 32
        return Fahrenheit #That was easy but now for the reverse
    def TemperatureFtoC(self, Fahrenheit):
        """
        In here we convert Fahrenheit to Celsius
        
        This is for when your american friend says to you its 70 deegres outside (which is 21°C)        
        """
        #In here it is the opposite of the Celsius formula
        #its °C = (°F − 32) x 1.8
        Celsius = (Fahrenheit - 32) * 1.8
        return Celsius
    def MeasurmentWorldtoUS(self, number, mmcmmkm):
        """
        In here our mesurment gets converted into their
        measurment
        """
        unit = ""
        mmcmmkm = mmcmmkm.lower()
        if mmcmmkm == "mm": #inch
            unit == "mm"
            return unit
        elif mmcmmkm == "cm": #foot
            unit = "cm"
            return unit
        elif mmcmmkm == "m": #yard
            unit = "m"
            return unit
        elif mmcmmkm == "km": #mile
            unit = "km"   
            return unit
        else:
            #raise Exception("Something has gone wrong please check if statements")
            return "Something has gone wrong while figuring out thenit"

name = Converting()

print(name.MeasurmentUStoWorld(1, "Cm"))