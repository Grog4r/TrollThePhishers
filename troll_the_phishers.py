import requests

import argparse
import random


class bc:

    HEADER = '\033[95m'

    OKBLUE = '\033[94m'

    OKCYAN = '\033[96m'

    OKGREEN = '\033[92m'

    WARNING = '\033[93m'

    FAIL = '\033[91m'

    ENDC = '\033[0m'

    BOLD = '\033[1m'

    UNDERLINE = '\033[4m'


email_providers = ["gmail.com", "outlook.com", "aol.com", "icloud.com", "yahoo.com", "gmx.com", "gmx.de"]

names = open("./lists/names.txt").readlines()

last_names = open("./lists/last_names.txt").readlines()

pw_part = open("./lists/pw_part.txt").readlines()


def generate_password():

    password = ""

    if random.choice([True, False, False, False]):

        password += random.choice(["*", "!", "?", "_", "%", "@", "#", "$"])

    if random.choice([True, False]):

        password += str(random.randint(0,1000))

    if random.choice([True, False, False, False]):

        password += random.choice(["*", "!", "?", "_", "%", "@", "#", "$"])

    password += random.choice(pw_part).strip()

    for i in range(random.randint(0,6)): password += str(random.randint(0,10))

    if random.choice([True, False]):

        password += random.choice(["*", "!", "?", "_", "%", "@", "#", "$"])

    return password



def generate_username():
    username = ""

    username += random.choice(names).strip()

    username += random.choice(["_", ".", "", "-"])

    if random.choice([True, False]):

        username += random.choice(last_names).strip()

    for i in range(random.randint(0,6)): username += str(random.randint(0,10))
    return username



if __name__ == '__main__':

    '''

    Main function

    '''


    parser = argparse.ArgumentParser(description="Troll them phishers.")

    parser.add_argument("url", help="URL of the Phishing site")

    parser.add_argument("-n", "--number", metavar="int", help="Number of requests sent, default=10", default=10, required=False)

    parser.add_argument("-uU", "--useUsernames", metavar="bool", help="Use usernames instead of email addresses.", action="store_const", const=True, default=False)

    parser.add_argument("-uT", "--usernameTerm", metavar="string", help="Set if \"username\" is something different in payload.", default="username", required=False)

    parser.add_argument("-pT", "--passwordTerm", metavar="string", help="Set if \"password\" is something different in payload.", default="password", required=False)


    args = parser.parse_args()


    for i in range(args.number):


        username = generate_username()

        if not args.useUsernames:

            username += "@" + random.choice(email_providers)

        password = generate_password()


        url = args.url if args.url[0:7] == "http://"  else "http://" + args.url


        post_data ={

            args.usernameTerm: username,

            args.passwordTerm: password,

            "login": "login"

        }


        headers = {

            'method' : 'POST',

            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"

        }
        '''
            print(url)
            print(post_data)
            print(headers)
        '''

        response = requests.post(url, data=post_data, headers=headers)
        status_code = response.status_code

        response_text = response.text


        if(status_code == 200 and response_text[:2] == "OK"):

            print(f"{bc.BOLD}{bc.OKBLUE}{username}{bc.ENDC}; {bc.WARNING}{password}{bc.ENDC} -> {bc.OKGREEN}{status_code}{bc.ENDC}")

        else:

            print(f"{bc.BOLD}{bc.OKBLUE}{username}{bc.ENDC}; {bc.WARNING}{password}{bc.ENDC} -> {bc.FAIL}{status_code}{bc.ENDC}")