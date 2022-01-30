def init():
    return "\\x1=\\step;"
def var(idx):
    return "\\x"+ str(idx+1) + "=\\x" + str(idx) + "+\\step;"

def lr_line(name, idx, sign):
    return "\\" + name + str(idx) + "=\\x" + str(idx) + sign + "\\eps;"

n = 2
count = 2 * n * n
print(init())
for i in range(0, count):
    print(var(i+1))
    
for i in range(0, count+1):
    print(lr_line("l", i+1, "-"))
    print(lr_line("r", i+1, "+"))
