from pyfiglet import Figlet
import sys
import random


figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    f = Figlet(font = random.choice(font_list))
    txt = input("Input: ")
    print(f.renderText(txt))
elif len(sys.argv) == 3:
    if not sys.argv[2] in font_list:
        sys.exit("Invalid font")  
    if sys.argv[1] in ("-f", "--font"):
                f = Figlet(font = sys.argv[2])
                txt = input("Input: ")
                print(f.renderText(txt))
    else:
          sys.exit("Invalid arguments")
else:
     sys.exit("Invalid arguments")