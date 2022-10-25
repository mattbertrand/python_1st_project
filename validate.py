# email = input("What's your email? ").strip()

# username, domain = email.split("@")

# if username and domain.endswith(".com"):
#     print("Valid")
# else:
#     print("Invalid")

import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.com", email):
    print("Valid")
else:
    print("Invalid")