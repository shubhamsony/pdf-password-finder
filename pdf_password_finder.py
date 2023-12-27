import PyPDF2
import itertools



GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def test_password(pdf_path, password):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Check if the PDF is encrypted
        if pdf_reader.is_encrypted:
            
            if pdf_reader.decrypt(password):
                print(f"{GREEN}The password is: '{password}' is correct.{RESET}")
                return True
            else:
                print(f"{RED}Password tried: '{password}' is incorrect.{RESET}")
                return False
        else:
            print("The PDF is not encrypted.")
            return False

pdf_path = input("input pdf path: ")
characters = "123456789abcdefghijklmnopqrstuvwxyz"
min_length = 1
max_length = 7  

# Try passwords of all lengths up to max_length
for i in range(min_length, max_length + 1):
    combinations = itertools.product(characters, repeat=i)
    for c in combinations:
        password_pos = ''.join(c)
        if test_password(pdf_path, password_pos):
            print(f"{GREEN}Password found!{RESET}")
            break
    else:
        continue
    break 
