# import urllib
# use urllib.request to get the data from the url
# write a function that takes a url and returns a response

import urllib.request as urllib

print("This is a website connectivity checkup program")
input_url = input("Input the url of the website you want to check: ")

def main(url):
    print("Checking connectivity...")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully.")
    print("The response code was", response.getcode())

main(input_url)
