from .output_generator import start_notebook
from .notebook_stopper import stop_notebook


output_dict = start_notebook()

print(f"IP Address: {output_dict['IP Address']}\n")
print(f"URL: {output_dict['URL']}")
print(f"Token: {output_dict['Token']}")