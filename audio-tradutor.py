import urllib2

url = "https://translate.google.com.br/#pt/en/Chegou%20um%20Novo%20Pedido%20de%20Shake.%0AChegou%20um%20Novo%20Pedido%20de%20Shake.%0AChegou%20um%20Novo%20Pedido%20de%20Shake."
request = urllib2.Request(url)
request.add_header('User-agent', 'Mozilla/5.0') 
opener = urllib2.build_opener()

f = open("data.wav", "wb")
f.write(opener.open(request).read())
f.close()

