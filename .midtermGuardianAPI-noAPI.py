import requests, json, time, os, sys
from pprint import pprint
# import file on recently published articles on The Guardian
import theguardian_content

# create content
content = theguardian_content.Content(api='insert-API-key')

# gets raw_response
raw_content = content.get_request_response()
jsonData = json.loads(raw_content.text)

# content
pprint("Content Response headers {}." .format(content.response_headers()))

# get all results of a page
json_content = content.get_content_response()
all_results = content.get_results(json_content)
pprint("All results {}" .format(all_results))

# actual response
pprint("Response {response}" .format(response=json_content))


# Definitions
# create an empty list to store output, eventually will print all output added
lines = []

# starting point to pull jsonData
news = jsonData["response"]["results"]

# introduction and welcome user
print("Hello! What is your name?")
myName = input()

def displayIntro():
    print(
        "Welcome, "
        + myName
        + """! This is an program that draws data from the newsite, The Guardian.
Let's see the details on the recently published articles."""
    )
    time.sleep(1)

# choosing to see data from specific article, or aggregate
def which():
    type = ""
    while type != "specific" and type != "aggregate" and type != "s" and type != "a":
        print("Do you want to see data from a specific article, or aggregate data?")
        type = input()

        lines.append(type) #add output to list
    return type

# if chosen output is aggregate, then user can choose 1-5 based on type of data they want
def aggregate():
    agg = ""
    while agg != "1" and agg != "2" and agg != "3" and agg != "4" and agg != "5":
        print("Which type of data do you want to see: type, section, date, title, or url? (1-5)")
        agg = input()
        print("Details:")
        if agg == "1":
            a = "type"      
        elif agg == "2":
            a = "sectionName"
        elif agg == "3":
            a = "webPublicationDate"
        elif agg == "4":
            a = "webTitle"
        elif agg == "5":
            a = "webUrl"
    for k in news:
        print(k[a])

        lines.append(str(print(k[a]))) # add output to list

# choose to see details from one specific article (1-10)
def articleChoice():
    choice = ""
    while choice not in range(0,10):
        print("Pick which article you want more details from. (0-9)")
        choice = input()
        print("Article " + choice + ":")
        choice = int(choice)
        text = pprint(news[int(choice)])

        lines.append(str(text)) # add output to list

def program(chosenOutput):
    output = ""
    if chosenOutput == "specific" or chosenOutput == "s":
        print("You chose specific.")
        output = articleChoice()
    elif chosenOutput == "aggregate" or chosenOutput == "a":
        print("You chose aggregate.")
        output = aggregate()


# main

displayIntro()
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    choice = which()
    program(choice)

    print(
        "Do you want to view any details again, "
        + myName
        + "?"
    )

    playAgain = input()

# write output to .txt file
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')