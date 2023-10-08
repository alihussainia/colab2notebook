import requests
def show_ip_address():
  url = "https://ipv4.icanhazip.com/"  
  return requests.get(url).text.replace("\n", "")

if __name__ == "__main__":
    show_ip_address()