import datetime
import sys, os, subprocess
if len(sys.argv) > 2:
    timeformat = "%Y-%m-%d %H-%M-%S"
    now = datetime.datetime.now().strftime(timeformat)

    if len(sys.argv) > 3:
        filename = sys.argv[3].replace(r"%t", now).replace("\n",'')
    else:
        filename = f"Screenshot from {now}.png"
    if len(sys.argv) > 4:
        notifTitle = sys.argv[4].replace("\n",'')
    else:
        notifTitle = "Screenshot taken!"
    
    directory = sys.argv[2]

    child = subprocess.Popen(["realpath", directory], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

    directory = child.stdout.read().decode().replace("\n",'')

    file = f"{directory}/{filename}"

    child = subprocess.Popen(["grimshot","save", sys.argv[1], file], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    
    if '/' in child.stdout.read().decode():
        os.system(f"wl-copy < \"{file}\"")
        os.system(f"notify-send '{notifTitle}' '{filename}' -i '{file}'")
    else:
        print("Operation cancelled.")
else:
    print("Wayland screen capture helper\n")

    print(f"Usage: python3 {sys.argv[0]} (TARGET) (DIRECTORY) [filename] [notifTitle]\n")

    print("Targets:\n\tactive: Active window.\n\tscreen: All visible outputs.\n\toutput: Currently active output.\n\tarea: User-defined region\n\twindow: User selected window.\n")
    
    print(r"Use %t in [filename] for it to be replaced by the current date and time.")
