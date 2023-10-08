import subprocess

def show_token():
  # Token Command
  command = "jupyter notebook list | grep -oP '(?<=token=)[^&]+' | awk -F '::' '{print $1}'"

  # Run the command in the shell
  result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

  # Return the output of the command
  return result.stdout

  if __name__ == "__main__":
    show_token()