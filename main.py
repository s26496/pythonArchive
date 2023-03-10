import webbrowser
import requests as requests

if __name__ == '__main__':
    print("hello world")
    pageurl = input("Podaj stronę internetową: ")
    date = input("Podaj datę w formacie rok miesiąc dzień, np. 20060101: ")
    url = "http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date)
    response = requests.get(url)
    d = response.json()
    page = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)
