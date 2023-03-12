import webbrowser
import requests as requests

if __name__ == '__main__':
    print("hello world")
    pageurl = input("Podaj stronę internetową: ")
    date1 = input("Podaj pierwszą datę w formacie rok miesiąc dzień, np. 20060101: ")
    url1 = "http://archive.org/wayback/available?url="+pageurl+"&timestamp="+str(date1)
    response = requests.get(url1)
    d = response.json()
    page1 = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page1)

    date2 = input("Podaj drugą datę w formacie rok miesiąc dzień, np. 20060101: ")
    url2 = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date2)
    response = requests.get(url2)
    d = response.json()
    page2 = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page2)

    date3 = input("Podaj trzecią datę w formacie rok miesiąc dzień, np. 20060101: ")
    url3 = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date3)
    response = requests.get(url3)
    d = response.json()
    page3 = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page3)

