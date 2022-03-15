def emailProcess(email):
    email_username = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    return [email_username, email_domain]

def printMessage(email_username, email_domain):
    print(f"User name is {email_username}")
    print(f"Email domani is {email_domain}")

def main():
    email = input("Nhap vao email: ").strip()
    email_username, email_domain = emailProcess(email)
    printMessage(email_username,email_domain)

if __name__ == "__main__":
    main()