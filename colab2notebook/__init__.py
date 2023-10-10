from .output_generator import start_book
from .notebook_stopper import stop_book

def start():
    output_dict = start_book()

    print(f"IP Address: {output_dict['IP Address']}\n")
    print(f"URL: {output_dict['URL']}")
    print(f"Token: {output_dict['Token']}")

def stop():
    stop_book()