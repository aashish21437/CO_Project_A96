import sys
from sys import stdin


class regi:
    def __init__(self, address): 
        self.value = 0;
        self.address = address

    def addr(self):
        return self.address

    def val(self):
        return self.value



global R0;
global R1;
global R2;
global R3;
global R4;
global R5;
global R6;
global FLAGS;


R1,R2,R0,R4,R5,R3,R6 = regi("001"),regi("010") , regi("000"), regi("100"), regi("101") ,regi("011"), regi("110")

def binaryCode(n):
    y = ""
    y  = bin(n)
    y = y[2:]
    l = len(y)
    out = ("0")*(8-l) + y
    return out


def Addition(r1, r2, r3): 
    a = r1.addr()
    c = r3.addr()
    b = r2.addr()
    
    return "10000" + "00" + a + b + c

def AND(r1, r2, r3):
    
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
   
    return "11100" + "00" + a + b + c
    
def Move_Immediate(r1, x): 
    a = r1.addr()
   
    binary = binaryCode(x)
    

    
 

    return "10010" + a + binary


def Subtraction(r1, r2, r3): 
    b = r2.addr() 
    a = r1.addr()
    c = r3.addr()
    
   
    return "10001" + "00" + a + b + c

def Invert(r1, r2):
    a = r1.addr()
    b = r2.addr()
  
    return "11101" + "00000" + a + b
    
    



def Move_regi(r1, r2):
    
    a = r1.addr()
    b = r2.addr()
    

    return "10011" + "00000" + a + b

def Load(r1, x):
   
    a = r1.addr()
    
    binary = binaryCode(x)
    
    return "10100" + a + binary

def Right_Shift(r1, x):
    
    binary = binaryCode(x)

    a = r1.addr()
    
    return "11000" + a + binary

def Store(r1, x):
    
    a = r1.addr()
    binary = binaryCode(x)
   
    return "10101" + a + binary

def Multiply(r1, r2, r3):
   
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    return "10110" + "00" + a + b + c
            


def Divide(r3, r4):
    a = r3.addr()
    b = r4.addr()
    
    return "10111" + "00000" + a + b
    

def XOR(r1, r2, r3):
    
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    
    return "11010" + "00" + a + b + c

   


def Left_Shift(r1, x):
    
    binary = binaryCode(x)

    a = r1.addr()
    
    return "11001" + a + binary





            
def OR(r1, r2, r3):
  
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    
    return "11011" + "00" + a + b + c
        

 
    
def Jump_if_Greater_Than(x):
    binary = binaryCode(x)
    
    return "01101" + "000" + binary



def Compare(r1, r2):
     
    a = r1.addr()
    b = r2.addr()
    # call flag here
    return "11110" + "00000" + a + b
    

def Unconditional_Jump(x):
    binary = binaryCode(x)
    

    return "11111" + "000" + binary

def Halt():
    # flag(0,0,0,0)
    return "0101000000000000"
    

def Jump_if_Less_Than(x):
    binary = binaryCode(x)
    
    return "01100" + "000" + binary



def Jump_if_Equal(x):
    binary = binaryCode(x)
    
    return "01111" + "000" + binary


    
global all_resistors_1;
global variable_counter;

global l

global OutputFile;
global label_dict;
global all_regis;
global variable_dict;


instructions = sys.stdin.readlines()     #taking input
all_regis = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"];
all_regis_1 = ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"];



OutputFile = [];

variable_dict = {}
variable_counter = 0;

label_dict = {}

instr = 0
check = 0
while(instr<len(instructions)):
    if "/n" in instructions[instr]:
        #for int
        instructions[instr].replace("/n", "")
    #check idhar bhi 
    check = check + 1
    #print(check)
    ins = list((instructions[instr]).split())
    instr = instr+1
    if len(ins)==0:
        continue
    elif ins[0]=="var":
        variable_counter += 1
    else:
        break
instr = 0
check  = 0
while(instr<len(instructions)):

    if "/n" in instructions[instr]:
        #for int
        check = check + 1
        instructions[instr].replace("/n", "")
    
    #check ko +1 
    check  = check +1 
    #print(check)
    
    ins = list((instructions[instr]).split())
    
    if len(ins)==0:
        instr = instr + 1
        continue

    elif " :" in instructions[instr]:
        OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error (gap before ':')"]
        instructions = []
        instr = instr+1
        break

    elif ins[0][len(ins[0]) - 1]==":":
        d = ins[0][0:len(ins[0])-1]
        
        if d in label_dict.keys():
            OutputFile = ["Error in line number: " + str(instr+1) + "; Illegal use of labels/variables name"]
            instructions = []
            instr = instr + 1
            break
        else:
            label_dict[d] = instr - variable_counter
            instr = instr+1
    
    else:
        instr = instr + 1
        continue
    


check = 0

for instr in range(len(instructions)):
    if "/n" in instructions[instr]:
        #for int 
        check = check + 1 # t
        instructions[instr].replace("/n", "")
    ins = list((instructions[instr]).split())  #use default split

    

    if len(ins)==0:
        continue

    if ins[0][-1]==":":
        ins = ins[1:]
 
    if ins[0]=="hlt":
        if instr==len(instructions)-1:
            OutputFile.append(Halt());
            break
        else:
            OutputFile = ["Error in line number: " + str(instr+2) + "; 'hlt' not being used as the last instruction"]
            break
    
    elif ins[0]=="var":
        if len(ins)<2 :
            OutputFile = ["Error : variable not correctly assigned"]
            break

        elif len(ins)>2:
            OutputFile = ["Error : variable not correctly assigned"]
            break

        
        
        elif len(variable_dict)==variable_counter:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Variable defined in between code"]
            break
        
        elif ins[1] in variable_dict.keys():
            OutputFile = ["Error : Duplicate Variable Found"]
            break

        elif ins[1] in label_dict.keys():
            OutputFile = ["Error : Duplicate Label Found"]
            break

        
    
        d = ins[1]
        #if d in
        variable_dict[d] = len(instructions) + len(variable_dict) - variable_counter



    elif ins[0]=="add":

        if len(ins)>4:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error"]
            break
        
        elif len(ins)<4:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error"]
            break


        else:

           
            if (ins[1] in all_regis) or (ins[2] in all_regis) or (ins[3] in all_regis):

                    #1st regi detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd regi detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

                #3rd regi detection
                if ins[3]=="R0":
                    r3 = R0
                elif ins[3]=="R1":
                    r3 = R1
                elif ins[3]=="R2":
                    r3 = R2
                elif ins[3]=="R3":
                    r3 = R3
                elif ins[3]=="R4":
                    r3 = R4
                elif ins[3]=="R5":
                    r3 = R5
                elif ins[3]=="R6":
                    r3 = R6

                OutputFile.append(Addition(r1, r2, r3));
                

            else:
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid regi not found"]
                break

    elif ins[0]=="sub":
        if len(ins)==4:
           
            if (ins[1] not in all_regis) or (ins[2] not in all_regis) or (ins[3] not in all_regis):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid regi not found"]
                break

            else:
                #1st regi detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd regi detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

                #3rd regi detection
                if ins[3]=="R0":
                    r3 = R0
                elif ins[3]=="R1":
                    r3 = R1
                elif ins[3]=="R2":
                    r3 = R2
                elif ins[3]=="R3":
                    r3 = R3
                elif ins[3]=="R4":
                    r3 = R4
                elif ins[3]=="R5":
                    r3 = R5
                elif ins[3]=="R6":
                    r3 = R6

                OutputFile.append(Subtraction(r1, r2, r3));

        else:
            OutputFile = ["Error in line number: " + str(instr+1), "; Syntax Error"]
            break

    elif ins[0]=="mov":
        if len(ins)==3:
           
            if (ins[1] not in all_regis):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid regi not found"]
                break

            else:
                #1st regi detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

            if (ins[2])[0]=="$":  #this is detection of imm
                x = int(ins[2][1:])
                if x<0 or x>255:
                    OutputFile = ["Error in line number: " + str(instr+1) + "Illegal Immidiate Value"]
                    break
                else:
                    OutputFile.append(Move_Immediate(r1, x))
                    continue
                    
            
            elif (ins[2] not in all_regis_1) :
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid regi not found"]
                break

            else:
                #2nd regi detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6
                else:
                    r2 = FLAGS

            OutputFile.append(Move_regi(r1, r2))

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error"]
            break

    elif ins[0]=="ld":
        if len(ins)==3:
           
            if (ins[1] not in all_regis):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid regi not found"]
                break

            else:
                #1st regi detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

            jj = ins[2]

            if jj not in variable_dict.keys():
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Variable not defined"]
                break
            else:
                x = variable_dict[jj]
                OutputFile.append(Load(r1, x))

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break
    
    elif ins[0]=="st":
        if len(ins)!=3:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error"]
            break
        else:

        
            if (ins[1]  in all_regis):
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6
        jj = ins[2]
        

        if jj  in variable_dict.keys():
            x = variable_dict[jj]
            OutputFile.append(Store(r1, x))
            
        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Variable not defined"]
            break
    
    
    
    elif ins[0]=="div":

        if len(ins)!=3:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error"]

            break
        else:


            if (ins[1]  in all_regis) and (ins[2]  in all_regis):
                


                #1st regi detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd regi detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6
                

                OutputFile.append(Divide(r1, r2))

            else:
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid regi not found"]
                break

    elif ins[0]=="rs":

        if len(ins)!=3:

            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break
        else:

            if (ins[1]  in all_regis):

                if ins[1]=="R0":


                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                    if (ins[2])[0]=="$":  #this is detection of imm
                    
                        x = int(ins[2][1:])
                        if x<0 or x>255:
                            OutputFile = ["Error in line number: " + str(instr+1) + "; Illegal Immediate values"]
                            break
                        else:
                            OutputFile.append(Right_Shift(r1, x))
                            continue
                    else:
                        OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
                        break
            else:
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
                break
    
    elif ins[0]=="ls":

        if len(ins)!=3:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break
        else:
            if (ins[1] in all_regis):
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6


        if (ins[2])[0]!="$":  #this is detection of imm
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
                break
                
        else:
                x = int(ins[2][1:])
                if x<0 or x>255:
                    OutputFile = ["Error in line number: " + str(instr+1) + "; Illegal Immediate values"]
                    break
                else:
                    OutputFile.append(Left_Shift(r1, x))
                    continue
    
    elif ins[0]=="xor":
        if len(ins)==4:
           
            if (ins[1] not in all_regis) or (ins[2] not in all_regis) or (ins[3] not in all_regis):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid regi not found"]
                break

            else:
                #1st regi detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd regi detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

                #3rd regi detection
                if ins[3]=="R0":
                    r3 = R0
                elif ins[3]=="R1":
                    r3 = R1
                elif ins[3]=="R2":
                    r3 = R2
                elif ins[3]=="R3":
                    r3 = R3
                elif ins[3]=="R4":
                    r3 = R4
                elif ins[3]=="R5":
                    r3 = R5
                elif ins[3]=="R6":
                    r3 = R6

                OutputFile.append(XOR(r1, r2, r3));

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break
    elif ins[0]=="jgt":
        jj = ins[1]

        if jj not in label_dict.keys():
            OutputFile = ["Error in line number: " + str(instr+1) + "; Use of Undefined Labels"]
            break
        else:
            x = label_dict[jj]
            OutputFile.append(Jump_if_Greater_Than(x))

    elif ins[0]=="or":
        if len(ins) !=4:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break
        else:
            if ins[1]=="R0":
                r1 = R0
            elif ins[1]=="R1":
                r1 = R1
            elif ins[1]=="R2":
                r1 = R2
            elif ins[1]=="R3":
                r1 = R3
            elif ins[1]=="R4":
                r1 = R4
            elif ins[1]=="R5":
                r1 = R5
            elif ins[1]=="R6":
                r1 = R6

                #2nd regi detection
            if ins[2]=="R0":
                r2 = R0
            elif ins[2]=="R1":
                r2 = R1
            elif ins[2]=="R2":
                r2 = R2
            elif ins[2]=="R3":
                r2 = R3
            elif ins[2]=="R4":
                r2 = R4
            elif ins[2]=="R5":
                r2 = R5
            elif ins[2]=="R6":
                r2 = R6

            #3rd regi detection
            if ins[3]=="R0":
                r3 = R0
            elif ins[3]=="R1":
                r3 = R1
            elif ins[3]=="R2":
                r3 = R2
            elif ins[3]=="R3":
                r3 = R3
            elif ins[3]=="R4":
                r3 = R4
            elif ins[3]=="R5":
                r3 = R5
            elif ins[3]=="R6":
                r3 = R6

            OutputFile.append(OR(r1, r2, r3));

    elif ins[0]=="jmp":
        jj = ins[1]

        if jj not in label_dict.keys():
            OutputFile = ["Error in line number: " + str(instr+1) + "; Use of Undefined Labels"]
            break
        else:
            x = label_dict[jj]
            OutputFile.append(Unconditional_Jump(x))

    elif ins[0]=="and":
            if len(ins) !=4:
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
                break
            else:

                if (ins[1] not in all_regis) and (ins[2] not in all_regis) and (ins[3] not in all_regis):

                    OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid regi not found"]

                    break
                else:
                    if ins[1]=="R0":
                        r1 = R0
                    elif ins[1]=="R1":
                        r1 = R1
                    elif ins[1]=="R2":
                        r1 = R2
                    elif ins[1]=="R3":
                        r1 = R3
                    elif ins[1]=="R4":
                        r1 = R4
                    elif ins[1]=="R5":
                        r1 = R5
                    elif ins[1]=="R6":
                        r1 = R6

                    #2nd regi detection
                    if ins[2]=="R0":
                       r2 = R0
                    elif ins[2]=="R1":
                       r2 = R1
                    elif ins[2]=="R2":
                        r2 = R2
                    elif ins[2]=="R3":
                        r2 = R3
                    elif ins[2]=="R4":
                        r2 = R4
                    elif ins[2]=="R5":
                        r2 = R5
                    elif ins[2]=="R6":
                        r2 = R6

                    #3rd regi detection
                    if ins[3]=="R0":
                        r3 = R0
                    elif ins[3]=="R1":
                        r3 = R1
                    elif ins[3]=="R2":
                        r3 = R2
                    elif ins[3]=="R3":
                        r3 = R3
                    elif ins[3]=="R4":
                        r3 = R4
                    elif ins[3]=="R5":
                        r3 = R5
                    elif ins[3]=="R6":
                        r3 = R6

                    OutputFile.append(AND(r1, r2, r3));

    elif ins[0]=="je":
        jj = ins[1]

        if jj not in label_dict.keys():
            OutputFile = ["Error in line number: " + str(instr+1) + "; Use of Undefined Labels"]
            break
        else:
            x = label_dict[jj]
            OutputFile.append(Jump_if_Equal(x))

    

    elif ins[0]=="not":
        if len(ins)==3:
           
            if (ins[1] not in all_regis) or (ins[2] not in all_regis):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid regi not found"]
                break

            else:
                #1st regi detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd regi detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

            OutputFile.append(Invert(r1, r2))

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break

    elif ins[0]=="cmp":
        if len(ins)==3:
           
            if (ins[1] not in all_regis) or (ins[2] not in all_regis):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid regi not found"]
                break

            else:
                #1st regi detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd regi detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

            OutputFile.append(Compare(r1, r2))

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "Syntax error"]
            break

    
    
    elif ins[0]=="jlt":
        jj = ins[1]

        if jj not in label_dict.keys():
            OutputFile = ["Error in line number: " + str(instr+1) + "; Use of Undefined Labels"]
            break
        else:
            x = label_dict[jj]
            OutputFile.append(Jump_if_Less_Than(x))
    elif ins[0]=="mul":
        if len(ins) !=4:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error"]
            break
        else:

            if (ins[1]  in all_regis) and (ins[2]  in all_regis) and (ins[3] in all_regis):

            #1st regi detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd regi detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

                #3rd regi detection
                if ins[3]=="R0":
                    r3 = R0
                elif ins[3]=="R1":
                    r3 = R1
                elif ins[3]=="R2":
                    r3 = R2
                elif ins[3]=="R3":
                    r3 = R3
                elif ins[3]=="R4":
                    r3 = R4
                elif ins[3]=="R5":
                    r3 = R5
                elif ins[3]=="R6":
                    r3 = R6

                OutputFile.append(Multiply(r1, r2, r3));
            else:

                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid regi not found"]

                break
    else:
        OutputFile = ["Error in line number: " + str(instr+1) + "; Undefined Instruction"]
        break

    

    
     
tr = 1
p = "0101000000000000"

troje = len(OutputFile)   
if troje ==1:
    chk = OutputFile[0].split()
    if tr ==1:
        tr = tr + 1
    if "Error" in chk:
        print(OutputFile[0])
    elif OutputFile[0]=="01010000000000111":#
        print(p) 
    elif OutputFile[0]==p:
        print(p)
    else:
        print("Error: hlt not present")

elif p not in OutputFile:
     OutputFile = ["Error: hlt not present"]
     print("Error: hlt not present")

else:
    for bb in OutputFile:     # for printing the Output
        print(bb)
        
