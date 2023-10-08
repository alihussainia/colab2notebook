import subprocess 

def stop_notebook():
  # Run the command
  result = subprocess.run(
      "fuser -k 8888/tcp",
      shell=True,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      text=True
  )

  # Check if there was any output on stdout
  if result.stdout.strip():
    print("Notebook Stopped")

if __name__ == "__main__":
  stop_notebook()
