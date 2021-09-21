from typing import List


def display_message():
    """Display a simple greeting."""
    print("Hey, I'm Markel Samuel")

display_message()

def favorite_book():
    """Display my favorite Book."""
    print("One of my favorite books is To Kill a Mockingbird. ")

favorite_book()

def make_shirt(shirt_size, text_printed):
    """Display Information about a pet. """
    print(f"\nMy shirt size is {shirt_size}")
    print(f"My shirt size is {shirt_size} and the text I want printed is {text_printed}")

make_shirt(shirt_size='Large', text_printed='I love Python')

def describe_city(city, country):
    """Display information about a city and country."""
    print(f"{city} is in {country}.")

describe_city(city='Columbia', country='United States')
describe_city(city='Pittsburgh', country='United States')
describe_city('Anderson', 'United States')

def city_country(city, country):
    """Return a city country pair."""
    print(f"{city}, {country}")

city_country('\nAnderson', 'United States')
city_country('Moscow', 'Russia')
city_country('Bejing', 'China')

def make_album(artist_name, album_title, tracklist= None):
    """Return a dictionary of information about an album and artist"""
    artwork = {'Artist': artist_name, 'Album': album_title}
    if tracklist:
        artwork['Tracklist'] = tracklist
    return artwork

album = make_album('Drake', 'Certified Lover Boy', tracklist = 24)
album2 = make_album('Billie Eillish', "don't smile at me", tracklist = 9)
album3 = make_album('Adele', '21', tracklist = 12)
print(f"\n{album}")
print(album2)
print(album3)

def get_user_albums(artist_name, album_title):
    """Get user input on album artist and title"""
    artwork = f"{artist_name} {album_title}"
    return artwork

#This is an infinite loop
while True:
    print("\nName one of you favorite artist and an album of their's.")
    print("(enter 'q' at any time to quit.)")
    a_name = input("Artist Name: ")
    if a_name == 'q':
        break
    al_name = input("Album Name: ")
    if al_name == 'q':
        break

    favorite_artist_album = get_user_albums(a_name, al_name)
    print(f"Your favorite artist and album is {favorite_artist_album}.")

make_album(artist_name = None, album_title = None,)

while True:
    print('\nYou can now save your favorite artist and there favorite albums with your next input. ')
    fav_album = make_album(input("Who's your favorite artist: "), input('Favorite album by them:  '))
    print(fav_album)
    userexit = input("If you would like to exit this enter q, if not continue by pressing enter: ")
    if userexit == 'q':
        break

#Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
def show_messages(messages):
    """Print simple short messages to the user"""
    for message in messages:
        msg = f"{message} in Anderson, SC."
        print(msg)

messages = ['\nGood morning', 'Good Afternoon', 'Good evening']
show_messages(messages)

# Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it's printed.
# After calling the function, print both of your lists to make sure the messages were moved correctly.
def send_messages(messages):
    """Print simple short messages to the user"""
message = ['Good morning', 'Good Afternoon', 'Good evening']
completed_messages = []
while message:
    current_messages = message.pop()
    print(f"\nPrinting model: {current_messages}")
    completed_messages.append(current_messages)

print("\nThe following messages have been printed:")
for completed_message in completed_messages:
        print(completed_message)

def send_messages():
    print("This function should print a copy of both list: ")

    send_messages(messages)

def make_sandwich(*toppings, additional= None):
    """Summarize the topings the customer wants on sandwich"""
    print("Making a sandwich with the following topings: ")
    for toping in toppings:
        print(f"-{toping}")

make_sandwich('shredded lettuce', 'shredded cheese', 'ham', 'pickles', additional= 'mustard')
make_sandwich('romaine lettuce', 'swiss cheese', 'turkey', 'beets', additional= 'vinegar')
make_sandwich('assorted lettuce', 'american cheese', 'bologna', 'sliced pickles', additional= 'ranch')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user. """
    user_info['first_name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('Markel', 'Samuel',
                             location='Anderson',
                             country= 'United States',
                             field ='Cybersecurity'
                             )
print(user_profile)

def make_car(make, model, **car_info):
    """Store information about a car in a dictionary."""
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)

print(car)