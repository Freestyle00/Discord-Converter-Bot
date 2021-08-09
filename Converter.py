from unittest.signals import installHandler


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
        return Fahrenheit
        return f"{Celsius}°C is {round(Fahrenheit, 1)}°F"
    def TemperatureFtoC(self, Fahrenheit):
        """
        In here we convert Fahrenheit to Celsius
        
        This is for when your american friend says to you its 70 deegres outside (which is 21°C)        
        """
        #In here it is the opposite of the Celsius formula
        #its °C = (°F − 32) / 1.8
        Celsius = (Fahrenheit - 32) / 1.8 #uh this is akward but appratly i had it wrong but now it is fixed
        Celsius = round(Celsius, 1)
        return Celsius
        return f"{Fahrenheit}°F is {Celsius}°C"
    def MeasurmentWorldtoUS(self, number, mmcmmkm):
        """
        In here our measurment gets converted into US
        standards
        """
        mmcmmkm = mmcmmkm.lower()
        if mmcmmkm == "mm": #inch
            # mm × 0.039370078740157 = inch 
            inch = number * 0.03937008
            inch = round(inch, 3)
            return inch
            return f"{number}mm is {inch}in"
        elif mmcmmkm == "cm": #foot
            # cm * 0.032808 = foot
            foot = number * 0.032808
            foot = round(foot, 3)
            return foot
            return f"{number}cm is {foot}ft"
        elif mmcmmkm == "m": #yard
            # m * 1.093613
            yard = number * 1.093613
            yard = round(yard, 3)
            return yard
            return f"{number}m is {yard}yd"
        elif mmcmmkm == "km": #mile
            # km * 0.6213712
            mile = number * 0.6213712
            mile = round(mile, 3)
            return mile
            return f"{number}km is {mile}mi"
        else:
            #raise Exception("Something has gone wrong please check if statements")
            return False
    def MeasurmentUStoWorld(self, number, inftydmi):
        """
        This is to convert the US measurment into
        something more understandable for us
        """
        inftydmi = inftydmi.lower()
        if inftydmi == "in":
            # inch * 25.4
            milimeter = number * 25.4
            milimeter = round(milimeter, 3)
            return milimeter
            return f"{number}in is {milimeter}mm"
        if inftydmi == "ft" or inftydmi == "fe":
            # feet * 30.48
            centimeter = number * 30.48
            centimeter = round(centimeter, 3)
            return centimeter
            return f"{number}ft is {centimeter}cm"
        if inftydmi == "yd" or inftydmi == "ya":
            # yard * 0.9144
            meter = number * 0.9144
            meter = round(meter, 3)
            return meter
            return f"{number}yd is {meter}m"
        if inftydmi == "mi":
            # mile * 1.609344
            kilometer = number * 1.609344
            kilometer = round(kilometer, 3)
            return kilometer
            return f"{number}mi is {kilometer}km"
        return False
    def SpeedMPHtoKMH(self, number):
        """
        This is to convert the speed measurment Miles per hours,
        into Kilometers per hour
        """
        #1.609344 * MPH
        KMH = 1.609344 * number
        KMH = round(KMH, 1)
        return KMH
        return f"{number}MP/H is {KMH}KM/H"
    def SpeedKMHtoMPH(self, number):
        """
        This is to convert the speed measurment Kilometers per hours,
        into Miles per hour
        """
        #0.6213712 * KMH
        MPH = 0.6213712 * number
        MPH = round(MPH, 1)
        return MPH
        return f"{number}KM/H is {MPH}MP/H"
