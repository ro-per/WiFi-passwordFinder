import subprocess
#open a file, w+ creates it (OVERWRITE)
# --> ask name, search, ask again what to do when name already exists
f= open("passwords.txt","w+")
f.write("All the known passwords by this machine are:\n")
#search for passwords
data=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
profiles=[i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
#making titles
f.write("{:<30} |  {:<}".format("Network", "Password"))
f.write("\n\n")
#search for passwords
for i in profiles:
    results = subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    #print passwords to file and terminal
    try:
        print("{:<30} |  {:<}".format(i, results[0]))
        f.write("{:<30} |  {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30} |  {:<}".format(i, ""))
        f.write("{:<30} |  {:<}".format(i, ""))
    f.write('\n')    
#close file
f.close()