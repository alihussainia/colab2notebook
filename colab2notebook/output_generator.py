from subprocess import call
import time
from .ip_finder import show_ip_address
from .notebook_starter import run
from .notebook_url import show_url
from .generate_token import show_token

out_dict={}

def start_book():
  # output_dictionary
  out_dict["IP Address"]= show_ip_address()
  run()  # Call the run function
  #time.sleep(2)
  out_dict["URL"]= show_url()
  time.sleep(2)
  out_dict["Token"]= show_token()
  
  if any(value in (None, '') for value in out_dict.values()):
    start_book()

  call("sudo rm -R temp.txt",shell=True)    
  return out_dict


if __name__ == "__main__":
  start_book()