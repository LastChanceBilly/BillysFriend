import math

class FunCalc:
    def __init__(self):
        self.test = 0
        self.output=  " "
    def calcFunc(self, fx):
        self.output = " "
        def oadd(item):
            self.output += item
        if(fx != None):
            for i in fx:
                val = ord(i)
                if(val >= 48 and val <= 57):
                    oadd(i)
                elif((val >= 40 and val <= 47) or (val >= 60 and val <= 62) or val == 94):
                    if(val != 44):
                        oadd(i)
                    else:
                        return "Error, character "+i+" not defined"
                else:
                    return "Error, character "+i+" not defined"
            val = 0
            try:
                val = eval(self.output)
            except ZeroDivisionError:
                return "I know it may be hard, but try not to divide by zero pls"
            return(val)
        else:
            return "Error, no function was provided"