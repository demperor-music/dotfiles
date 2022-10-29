import sys, os, subprocess
dirname = os.path.dirname(__file__)
if len(sys.argv) > 2:
    change = -2 * (sys.argv[1].lower() == "prev") + 1
    child = subprocess.Popen(["ls", "-1", sys.argv[2].replace('\n','')], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    wallpapers = child.stdout.read().decode().split('\n')
    wallpapers.pop()
    if sys.argv[1].lower() == 'set':
        change = 0

    with open(f'{dirname}/wallpaper.index', 'r') as x: 
        index = x.read().replace('\n','')
        i = (int(index) + change) % len(wallpapers)
    
    with open(f'{dirname}/wallpaper.index', 'w') as x:
        x.write(f"{i}")

    print(f"{sys.argv[2]}/{wallpapers[i]}")

else:
    print("Wallpaper switcher\n")

    print("Pass output into whatever wallpaper provider you have")

    print(f"Usage: python3 {sys.argv[0]} (prev/next/set) (folder)\n")
