from subprocess import call
def run():
  call('nohup jupyter notebook --port=8888 > jupyter.log 2>&1 &', shell=True)
if __name__ == "__main__":
    run()