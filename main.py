import webbrowser
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Back, Style

# Giving color to different text to make the data more clear to the user
init()
FORES = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
BRIGHTNESS = [Style.DIM, Style.NORMAL, Style.BRIGHT]


# General function
def random_article():
    # Calling random wikipedia page
    res = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    parse = BeautifulSoup(res.content, "html.parser")
    topic = parse.find(class_="firstHeading").text

    print("Getting random article...")
    print(".")
    print("..")
    new_article = (f"{topic}")
    print(new_article)
    read_article = input(
        f"Would you like to read about {new_article}? \nType 'Y' to read, 'N' to generate new article, or anything else to end this session: ")
    if read_article.upper() == 'Y':
        for item in parse.select("p"):
            print("--" + Fore.LIGHTMAGENTA_EX + item.text)


        print(Fore.BLUE + "-\x1B[3mIf there is no text displayed above, It means the webpage has no summary. Open the webpage to read.-\x1B[0m ")
        open_article = input(Fore.WHITE + "Would you like to see the full page? \nType 'Y' to open or 'N' for no: ")
        if open_article.upper() == 'Y':
            webbrowser.open("https://en.wikipedia.org/wiki/%s" % topic)
            print("Thanks for learning")

        elif open_article.upper() == 'N':
            next_article = input(
                "Would you like to generate another article? \nType 'Y' for yes, or 'N' to end this session: ")
            if next_article.upper() == 'Y':
                random_article()
            elif next_article.upper() == 'N':
                print("Thanks for learning!")
        else:
            open_article = input(
                Fore.GREEN + f"Would you like to see the full page? \nType 'Y' to open or 'N' for no: ")



    elif read_article.upper() == 'N':
        random_article()
    else:
        print("Thanks for learning!")


random_article()
