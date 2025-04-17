import random
import string

def generate_fake_email():
    # List of common email domains
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "example.com"]
    
    # Generate random username (5-15 characters)
    username_length = random.randint(5, 15)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    
    # Select random domain
    domain = random.choice(domains)
    
    # Combine to form email
    email = f"{username}@{domain}"
    return email

def main():
    print("Fake Email Generator - Created by Mr Sabaz Ali Khan")
    print("--------------------------------------------------")
    
    # Generate and display 5 fake emails
    num_emails = 5
    for i in range(num_emails):
        email = generate_fake_email()
        print(f"Generated Email {i+1}: {email}")

if __name__ == "__main__":
    main()