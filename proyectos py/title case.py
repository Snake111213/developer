
def check_titlecase(name):
    if name.istitle():
        print(f"'{name}' is already in title case.")
    else:
        return name.title()

check_titlecase("jane smith")
