import requests

# Faz uma requisição GET para a URL "https://www.betrybe.com/"
response = requests.get("https://www.betrybe.com/")

# Imprime o código de status da resposta HTTP
print(response.status_code)

# Imprime o valor do header "Content-Type" da resposta HTTP
print(response.headers["Content-Type"])

# Imprime o conteúdo da resposta HTTP como texto
print(response.text)

# Faz uma requisição POST para a URL "http://httpbin.org/post" com o corpo "some content"
response = requests.post("http://httpbin.org/post", data="some content")

# Imprime o conteúdo da resposta HTTP como texto
print(response.text)

# Faz uma requisição GET para a URL "http://httpbin.org/get" com o header "Accept" definido como "application/json"
response = requests.get("http://httpbin.org/get", headers={"Accept": "application/json"})

# Imprime o conteúdo da resposta HTTP como texto
print(response.text)

# Faz uma requisição GET para a URL "http://httpbin.org/get"
response = requests.get("http://httpbin.org/get")

# Converte o conteúdo da resposta HTTP em formato JSON e imprime
print(response.json())

# Faz uma requisição GET para a URL "http://httpbin.org/status/404"
response = requests.get("http://httpbin.org/status/404")

# Lança uma exceção caso a resposta HTTP tenha um código de erro
response.raise_for_status()
