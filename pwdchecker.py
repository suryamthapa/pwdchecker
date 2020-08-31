"""
----------------------------------------------------------------------------------------------
***You can directly jump into the code (line 82)!
***However, if you are a beginner, i recommend you to go thoroughly over the project walkthrough.
***It will help, indeed!
----------------------------------------------------------------------------------------------

So, this is the password checker, which checks whether the given password is safe or not,
And tells us how many times the password is hacked(found in breached databases).
This is one of the beginners project which is worth giving a try.

Requirements:
1. You should have at least a bit of the knowledge of python basics.
    For loops
    If else statements
    Functions
2. if Requirements[0]==True:
        "You are good to go!"
This is the complete walkthrough of the project.
___________________________________
Basic overview/plan of the project:
---------------------------------------------------------------------------------------------------
Remember, it is not about the number of lines of codes(syntax), it is all about solving the problem.
---------------------------------------------------------------------------------------------------
Let's understand the intuition behind solving this problem.

The basic concept is to take the help of api provided by pwnedpasswords.com
It takes the first five characters of the hashed password as query,
And it returns the list all the hashed form of passwords that matches the given first five characters.
(Will be more clear, when you go following through)
Along with the list, it also returns the number of times the password is found in breached databases.

And then, inside the returned list, we have to check whether the hash of our password is present or not.
If not present:
    "Our password is safe."
else:
    "Our password has been found in breached databases.(hacked)"

-----------------------------------------------------
Let's break our project/problem into different steps.
(Again,remember, it is all about solving the problem.)
-----------------------------------------------------

We have a password (user gives as an argument in command line or in terminal) which we want to check.
So,
===1. Read the password from the command line/terminal.
    We can simply take input from terminal using input() function.
    OR take the help of SYS module--built in module of python.

Now, we got the password from the user.
Then , we have to get the hashed form of given password(based on SHA1 algorithm)
===2. To get the hashed form of password, we can get the help of "hashlib" library.===

Then, we have to break the hashed password into head and tail.
head = first five characters of our hashed password.
tail = characters after 5th position
===3.We know list indexing and slicing techniques,
     so, it is like eating the piece of delicious cake.

Now, we got the first five characters of our hash.
Then,we have to pass the first five character as a query attached with the url.
"https://api.pwnedpasswords.com/range/" + query
Then, we have to make a http request.
===4.For HTTP requests, We can take the help of requests module.
    That's easy.

In return, we will get the list of hashed passwords which matches our head(1st five characters) along with their breach count.
Now, we have to check whether the tail of our hashed password is present in the list or not.
If not present:
    "Our password is safe."
else:
    "Our password has been found in breached databases.(hacked)"

That's all!

Simple, isn't it?

Let's dive into our code!
"""

# Importing necessary modules
import hashlib
import requests
import sys


def request_the_api(quer):
    """
    Take the first five characters of hash form of password.
    Attach it to the url and make a request.
    And returns whatever it gets.
    """
    url = "https://api.pwnedpasswords.com/range/" + quer
    # print(url)
    req = requests.get(f"{url}")
    if req.status_code != 200:
        raise RuntimeError(F"This is wrong way.")
    return req


def password_check(password):
    """
    Takes the user input password as argument,
    And get the hashed form of password(based on sha1 algorithm)
    Take the first five characters and pass it furthur to make a api request.
    And finally, returns the result.
    """
    hashed = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    head, tail = hashed[:5], hashed[5:]
    req = request_the_api(head)
    return result(req.text, tail)


def result(req_text, tail):
    """
    Takes the list returned from the web 
    And check whether the tail of our hash is present inside the list or not?
    """
    lines = (line.split(":") for line in req_text.splitlines())
    # print(i for i in lines)
    for h, c in lines:
        # print(h,c)
        if h == tail:
            return c
    return 0


def main(passwords):
    """
    Takes the passwords given in the command line.
    If multiple passwords are given, it loops through all of them.
    """
    for i in passwords:
        c = password_check(i)
        if c:
            print(f"{i} is hacked {c} times")
        else:
            print(f"{i} is safe.")


if __name__ == "__main__":
    main(sys.argv[1:])

"""
Additionally, we can embed it in gui(tkinter/kivy/guizero) as per our wish.

My Learnings:
As a beginner, i was just diving into more complex concepts of python.
And playing around with the modules as "requests", "sys", was a great fun.
Before this project, I didn't know that we can take arguments from command line too.
Beside enhancing my ideas on functions, additionally, I got some basic knowledge about how this "API" thing works.
And ya! don't hesitate to google around! Search, Explore and Learn!

If you got to learn something from this project, i'd love to know!
If you have any queries/feedbacks, I'm just one DM away!
Instagram: @ysafarinep
            instagram.com/ysafarinep

Regards!
"""