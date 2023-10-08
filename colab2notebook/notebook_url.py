from subprocess import call

def show_url():
  call("touch temp.txt", shell=True)
  call("nohup lt --port 8888 > temp.txt &", shell=True)
  url=open('temp.txt').read()[13:]
  return str(url)
  
if __name__ == "__main__":
    show_url()