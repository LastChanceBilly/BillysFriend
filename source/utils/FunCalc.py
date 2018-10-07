import math

class FunCalc:
    def __init__(self):
        self.test = 0
    def calcFunc(self, fx):
        stack = []
        output = []
        def sadd(item):
            stack.append(item)
        def oadd(item):
            output.append(item)
        if(fx != None):
            for i in fx:
                val = ord(i)
                if(val >= 48 and val <= 57):
                    oadd(i)
                elif((val >= 40 and val <= 47) or (val >= 60 and val <= 62)):
                    if(val != 44 and val != 46):
                        if(val == 47):
                            if(len(stack) > 0):
                                op = stack[len(stack) -1]
                                oadd(op)
                                stack.remove(op)
                                sadd(i)
                            else:
                                sadd(i)
                        elif(val == 41):
                            if(len(stack) > 0):
                                count = 1
                                for x in stack[:-1]:
                                    count += 1
                                    stack[len(stack)-count] = " "
                                    if(x!="("):
                                        oadd(stack[len(stack)-count])
                                bu = []
                                for i in stack:
                                    if(i != " "):
                                        bu.append(i)
                                stack = []
                                stack = bu
                                print(bu)
                            else:
                                return "Error, missing ("
                        else:
                            sadd(i)
                    else:
                        return "Error, character "+i+" not defined"
                else:
                    return "Error, character "+i+" not defined"
            for i in stack:
                oadd(i)
            return(output)
        else:
            return "Error, no function was provided"



