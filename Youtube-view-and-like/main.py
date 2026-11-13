views = 0
likes = 0
choice = 0
def func_view():
    global views
    views += 1
#makes the function to add views to the views counter
def func_like():
    global likes
    likes += 1
#makes the function to add a like to the like counter 
def func_view_analytics():
    print("Views = ", views)
    print("likes = ", likes)
#displays the current counter values

while True:
    print("Welcome to yt what would you like to do?")
    choice = input("1. view| 2. like| 3. analytics| 4. exit")
#uses a while loop to keep askig the question and calls the function depending on 
    if choice == "1":
        func_view()
    if choice == "2":
        func_like()
    if choice == "3":
        func_view_analytics()
    if choice == "4":
        print("Thanks for using youtube!")
        break
    
