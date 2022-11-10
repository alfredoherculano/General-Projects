# collect email from user
# split the email using the @ as separator, the first part as the username, the second part as the domain
# split the domain using the . as separator

def main():
    print(' Welcome to the email splicer ' + '\n')

    email_input = input('Enter your email address: ')

    (username, domain) = email_input.split('@')  # splitting and saving as a tuple
    (domain, extension) = domain.split('.')  #doing the same with the domain part

    print('Username: ', username)
    print('Domain: ', domain)
    print('Extension: ', extension)

main()