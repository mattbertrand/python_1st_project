# email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if username and domain.endswith(".com"):
#     print("Valid")
# else:
#     print("Invalid")

import re

email = input("What's your email? ").strip()

# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email):
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|gov|net|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")