import datetime
time=datetime.datetime(2025,1,12)
site_block=["www.telegram.com","www.youtube.com"]
host_path="C:/Windows/System32/drivers/etc/hosts"
redirect="127.0.0.1"

with open(host_path,"r+") as file:
    content=file.read()
    for website in site_block: 
        if website in content:
            pass
        else:
            file.write(redirect+" "+website+"\n") 