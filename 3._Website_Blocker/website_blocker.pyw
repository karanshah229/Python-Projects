import time
from datetime import datetime as dt

# Websites can be redirected using Hosts File
# Windows Path: C:\Windows\System32\drivers\etc\hosts
# Linux Path: etc\hosts
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com", "youtube.com", "www.youtube.com"]

while True:
    # Check if Time is between 9 AM to 5 PM
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        # Working Hours
        with open(hosts_path, 'r+') as file:
            content = file.read()
            # Block Websites not already blocked in hosts file
            for website in website_list:            
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        # Fun hours so,
        # Remove all the entries made to hosts file
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
