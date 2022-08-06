import sys
#  import numpy as np
# import matplotlib.pyplot as plt

class regi:
   
    def __init__(self, address):
        self.value = 0;
        self.address = address

    def addr(self):
        return self.address

    def val(self):
        return self.value

class Flag_regi:
  
    def __init__(self) -> None:
        self.v = self.l = self.g = self.e = 0
        

    def val(self):
        return "0"*12 + str(self.v) + str(self.l) + str(self.g) + str(self.e)

    def addr(self):
        return "111"

    def reset(self):
        self.v = self.l = self.g = self.e = 0

global R0;global R1;global R2;global R3;global R4;global R5;global R6;global FLAGS;global vardicti;
R1,R2,R0,R4,R5,R3,R6 = regi("001"),regi("010") , regi("000"), regi("100"), regi("101") ,regi("011"), regi("110")

def convBintoint(s):
  
    return int(s, 2)

FLAGS = Flag_regi()

def convIntegertobin(n, ln):
    
    bnr = bin(n)
    bnr = bnr.replace('0b','')
    while len(bnr)<ln:
        bnr = "0" + bnr

    return bnr 


vardicti = {}

def printer(prog_count):
    

    prg = convIntegertobin(prog_count, 8)

    r0,r1,r2,r3,r4,r5,r6,flg = convIntegertobin(R0.val(), 16) ,convIntegertobin(R1.val(), 16) ,convIntegertobin(R2.val(), 16) ,convIntegertobin(R3.val(), 16) ,convIntegertobin(R4.val(), 16) ,convIntegertobin(R5.val(), 16), convIntegertobin(R6.val(), 16) ,FLAGS.val()
    return [prg, r0, r1, r2, r3, r4, r5, r6, flg]


def sub(r1, r2, r3):
    FLAGS.reset()
    a = r1.val()
    b = r2.val()

    x = a-b 

    if x<0:
        r1.value = 0
        FLAGS.v = 1

    else:
        FLAGS.reset()
        r3.value = x    

def add(r1, r2, r3):
    FLAGS.reset()
    a = r1.val()
    b = r2.val()

    x = a+b 

    if x<=65535:
        r3.value = x
        
    
    else:
        FLAGS.v = 1
        binx = convIntegertobin(x, 17)
        binx = binx[1:17]
        nx = convBintoint(binx)
        r1.value = nx
       
        


def Load(r1, mem):
    
    if mem in vardicti.keys():
        pa = vardicti[mem]
    else:
        vardicti[mem] = 0
        pa = vardicti[mem]

    r1.value = pa 
    FLAGS.reset()
    

def Compare(r1, r2):
    FLAGS.reset()
    if r1.val()>r2.val():
        FLAGS.g = 1
    elif r1.val()<r2.val():
        FLAGS.l = 1
    
    else:
        FLAGS.e = 1

def Move_Immidiate(r1, imm):
    
    x = convBintoint(imm)
    r1.value = x
    FLAGS.reset()

def Move_regi(r2,r1):
    if r2==FLAGS:
        
        r1.value = convBintoint(FLAGS.val())
    else:
        r1.value = r2.val()

    FLAGS.reset()


def Store(r1, mem):
    
    if mem in vardicti.keys():
        vardicti[mem] = r1.val()
    else:
        vardicti[mem] = r1.val()
    
    FLAGS.reset()





def Multiply(r3,r1, r2):
    FLAGS.reset()
    x = (r2.val())*(r3.val())

    if x>65535:
        FLAGS.v = 1
        binx = convIntegertobin(x, 32)
        binx = binx[16:32]
        nx = convBintoint(binx)
        r1.value = nx
    
    else:
        
        r1.value = x


def rs(r1, imm):
    
    pa = convBintoint(imm)
    x = convIntegertobin(r1.val(), 16)
    
    x = "0"*pa + x
    x = x[0:16]
    r1.value = convBintoint(x)
    FLAGS.reset()

def Divide(r3, r4):
    R0.value, R1.value = (r3.val()//r4.val()), (r3.val()%r4.val()) 
    FLAGS.reset()



def LS(r1, imm):
   
    pa = convBintoint(imm)
    x = convIntegertobin(r1.val(), 16)
    x = x + "0"*pa
    x = x[len(x)-16:len(x)]
    r1.value = convBintoint(x)
    FLAGS.reset()
def Invert(r2, r1):
    xs = convIntegertobin(r2.val(), 16)
    xso = ""

def OR(r3,r1, r2):
    r1.value = (r2.val())|(r3.val())
    FLAGS.reset()

def XOR(r3,r1, r2):
    r1.value = (r2.val())^(r3.val())
    FLAGS.reset()



def AND(r3,r1, r2):
    r1.value = (r2.val())&(r3.val())
    FLAGS.reset()



    for i in range(16):

        if xs[i]!="0":
            xso = xso + "0"
        else:
            xso = xso + "1"

    
    r1.value = convBintoint(xso)

    FLAGS.reset()






# Main function
global pltpntx;
global pltpnty;

pltpntx = [];
pltpnty = [];

prg_count = 0
instructions=[]

CNO = 0

for i in sys.stdin.readlines():
    if i!="\n":
        instructions.append(i)

halted = False



while (not halted):
    pltpntx.append(CNO)
    CNO = CNO + 1
    pltpnty.append(prg_count)
    instr = instructions[prg_count]
    temp = 0
    if(instr == "010100000000001"):
        temp = temp + 1

    elif (instr=="0101000000000000"):
        FLAGS.reset();
        ctpt = printer(prg_count)
        print(*ctpt)
        
        halted = True
        break 
    elif(instr =="01010000000"):
        continue
    elif (instr[0:5] == "10001"):
        rg1 = instr[7:10]
        rg2 = instr[10:13]
        rg3 = instr[13:16]

        
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        sub(r1, r2, r3)

        ctpt = printer(prg_count)
        print(*ctpt)


    elif (instr[0:5] == "10000"):
        rg1 = instr[7:10]
        rg2 = instr[10:13]
        rg3 = instr[13:16]

        
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        add(r1, r2, r3)

        ctpt = printer(prg_count)
        print(*ctpt)
    
    
    
    elif (instr[0:5]=="10010"):
        rg1 = instr[5:8]

        
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        Move_Immidiate(r1, instr[8:16])

        ctpt = printer(prg_count)
        print(*ctpt)

    elif (instr[0:5]=="10011"):
        rg1 = instr[10:13]
        rg2 = instr[13:16]

        
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6
        elif rg1==FLAGS.addr():
            r1 = FLAGS

        
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        Move_regi(r1,r2)

        ctpt = printer(prg_count)
        print(*ctpt)

    elif (instr[0:5]=="10100"):
        rg1 = instr[5:8]

        
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        Load(r1, instr[8:16])

        ctpt = printer(prg_count)
        print(*ctpt)

    elif (instr[0:5]=="10101"):
        rg1 = instr[5:8]

        
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        Store(r1, instr[8:16])

        ctpt = printer(prg_count)
        print(*ctpt)

    elif (instr[0:5] == "10110"):
        rg1 = instr[7:10]
        rg3 = instr[13:16]
        rg2 = instr[10:13]
        

        
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

       
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        Multiply(r1, r2, r3)

        ctpt = printer(prg_count)
        print(*ctpt)

    elif (instr[0:5]=="11001"):
        rg1 = instr[5:8]

        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        LS(r1, instr[8:16])

        ctpt = printer(prg_count)
        print(*ctpt)

    elif (instr[0:5]=="10111"):
        rg3 = instr[10:13]
        rg4 = instr[13:16]

       
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        
        if rg4==R0.addr():
            r4 = R0
        elif rg4==R1.addr():
            r4 = R1
        elif rg4==R2.addr():
            r4 = R2
        elif rg4==R3.addr():
            r4 = R3
        elif rg4==R4.addr():
            r4 = R4
        elif rg4==R5.addr():
            r4 = R5
        elif rg4==R6.addr():
            r4 = R6

        Divide(r3, r4)

        ctpt = printer(prg_count)
        print(*ctpt)

    elif (instr[0:5]=="11000"):
        rg1 = instr[5:8]

      
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        rs(r1, instr[8:16])

        ctpt = printer(prg_count)
        print(*ctpt)

    

    elif (instr[0:5]=="11010"):
        rg1 = instr[7:10]
        rg2 = instr[10:13]
        rg3 = instr[13:16]

       
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

      
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        XOR(r1, r2, r3)

        ctpt = printer(prg_count)
        print(*ctpt)

    elif (instr[0:5]=="11011"):
        rg1 = instr[7:10]
        rg2 = instr[10:13]
        rg3 = instr[13:16]

       
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        OR(r1, r2, r3)

        ctpt = printer(prg_count)
        print(*ctpt)


    elif (instr[0:5]=="11110"):
        rg1 = instr[10:13]
        rg2 = instr[13:16]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6
        elif rg2==FLAGS.addr():
            r2 = FLAGS

        Compare(r1, r2)

        ctpt = printer(prg_count)
        print(*ctpt)

    elif (instr[0:5]=="11100"):
        rg1 = instr[7:10]
        rg2 = instr[10:13]
        rg3 = instr[13:16]

        
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        AND(r1, r2, r3)

        ctpt = printer(prg_count)
        print(*ctpt)

    elif (instr[0:5]=="11101"):
        rg1 = instr[10:13]
        rg2 = instr[13:16]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        Invert(r1, r2)

        ctpt = printer(prg_count)
        print(*ctpt)

    

    elif (instr[0:5]=="11111"):
        FLAGS.reset()
        ctpt = printer(prg_count)
        print(*ctpt)

        prg_count = convBintoint(instr[8:16])
        continue

    elif (instr[0:5]=="01100"):
        
        if (FLAGS.l != 1):
            FLAGS.reset()
            ctpt = printer(prg_count)
            print(*ctpt)

            prg_count += 1;
            continue
            

        else:
            FLAGS.reset()
            ctpt = printer(prg_count)
            print(*ctpt)

            prg_count = convBintoint(instr[8:16])
            continue

    elif (instr[0:5]=="01101"):

        if (FLAGS.g == 1):
            FLAGS.reset()
            ctpt = printer(prg_count)
            print(*ctpt)

            prg_count = convBintoint(instr[8:16])
            continue
            
        else:
            FLAGS.reset()
            ctpt = printer(prg_count)
            print(*ctpt)

            prg_count += 1;
            continue

    elif (instr[0:5]=="01111"):

        if (FLAGS.e == 1):
            FLAGS.reset()
            ctpt = printer(prg_count)
            print(*ctpt)

            prg_count = convBintoint(instr[8:16])
            continue
        else:
            FLAGS.reset()
            ctpt = printer(prg_count)
            print(*ctpt)

            prg_count += 1;
            continue
    elif (instr[0:5]=="01010"):
        ctpt=printer(prg_count)
        print(*ctpt)
        halted=True

    prg_count += 1; 


global variable_mem_list;

remain_lines = 256 - len(instructions)

for instr in instructions:
    print(instr[0:16])
    

variable_mem_list = list(vardicti.keys())
variable_mem_list.sort()

for mem_addr in variable_mem_list:
    pa = convIntegertobin(vardicti[mem_addr], 16)
    print(pa)
    remain_lines -=1
w = 0
while(w<remain_lines):
    w = w+1
    print("0"*16)

# # plotting code
# x_points = np.array(pltpntx)
# y_points = np.array(pltpnty)

# plt.scatter(x_points, y_points)

# plt.xlabel("Cycle Number")
# plt.ylabel("Memory Address")

# plt.show()



    


