import re
def validate_password(password):
  pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
  match = re.match(pattern, password)
  return bool(match)
pswd=input("enter password:")
res=validate_password(pswd)
if res:
  print("valid password")
else:
  print("Invalid password")
