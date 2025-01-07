import os

# Function to block a website
def block_website(website):
    hosts_path = "/etc/hosts"  # for Unix-based systems
    if os.name == 'nt':
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # for Windows

    redirect_ip = "127.0.0.1"
    website_entry = f"{redirect_ip} {website}\n"

    # Check if website already blocked
    with open(hosts_path, 'r+') as file:
        content = file.read()
        if website in content:
            print(f"{website} is already blocked.")
        else:
            # Block the website
            file.write(website_entry)
            print(f"{website} has been blocked.")

# Example usage
block_website("www.example.com")
