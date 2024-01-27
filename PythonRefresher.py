# Connor Stomp Assignment 1 Python Refresher


def echo(text: str, repeitions: int = 3) -> str:
    echo = ""
    i = repeitions
    while i > 0:
         echo = echo +fadingAffect(text,i) + '\n'
         i = i-1
    return echo +'.'

def fadingAffect(text:str, index:int)->str:
    fadeString = ""
    while(index != 0):
        fadeString =fadeString+ text[-index]
        index = index - 1
    return fadeString

    
if __name__ == "__main__":
    text = input("Yell something at mountain: ")
    print(echo(text))