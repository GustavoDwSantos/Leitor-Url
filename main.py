
from urlopen import urlopen


def main():
    
    url = urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    print(url)
    if float(url) < 4.70:
        print ("pode comprar")
    else: 
        print ("não pode comprar")

if __name__ == '__main__':
    main()