def print_fancy(text):
    """
    Function to print text in a fancy way.
    """
    fancy_text = ""
    for char in text:
        fancy_text += char.upper() + " "
    print(fancy_text)


def main():
    print("Welcome to the Dream Job Finder!")
    print("Please provide the following details:")

    # Asking for user's details
    name = input("Your Name: ")
    age = input("Your Age: ")
    location = input("Your Location: ")
    dream_job = input("Your Dream Job: ")
    why_dream_job = input("Why is this your Dream Job?: ")
    
    # Printing in a fancy way
    print("\nYour Fancy Details:")
    print("Name:")
    print_fancy(name)
    print("\nAge:")
    print_fancy(age)
    print("\nLocation:")
    print_fancy(location)
    print("\nDream Job:")
    print_fancy(dream_job)
    print("\nWhy Dream Job:")
    print_fancy(why_dream_job)


if _name_ == "_main_":
    main()
