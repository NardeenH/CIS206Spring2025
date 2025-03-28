import re

def remove_leading_zeros(ip):
    return re.sub(r'\b0+(\d)', r'\1', ip)  # Remove leading zeros from each octet

# Test case
ip_address = "216.08.094.196"
cleaned_ip = remove_leading_zeros(ip_address)
print(f"Original IP: {ip_address}")
print(f"Cleaned IP: {cleaned_ip}")
