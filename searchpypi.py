import requests, bs4, sys, webbrowser

print("Searching...")
res = requests.get("https://pypi.org/search/?q=" + ''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'parser.html')
link_elems = soup.select('.package-snippet')
num_open = min(5, len(link_elems))
for i in range(num_open):
    url = 'https://pypi.org' + link_elems[i].get('href')
    print(f'Opening {url}...')
    webbrowser.open(url)