import subprocess
import sys

SCENARIOS = {
    "please check system": [
        ["cat", "/etc/os-release"],
        ["cat", "/etc/fedora-release"],
    ], 
    "please check disk": [
        ["df", "-h", "/"],  
    ],
    "please show me the result": [
        ["ls", "-l", "/etc"]
    ],
}

while True: 
    user_input = input("Please write command: ").strip().lower()
    if user_input == "exit": 
        break
    if user_input in SCENARIOS: 
       for cmd in SCENARIOS[user_input]:  
          result = subprocess.run(cmd, capture_output=True, text=True)
          print(result.stdout.strip())
    else:
        print("Unknouwn command, please correct write commands again")
