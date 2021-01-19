import re 

url = re.compile(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")

# vemos que https://relopezbriega.com.ar lo acepta como una url válida.
x = url.search("https://relopezbriega.com.ar")

print(x)

