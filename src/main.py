
import random
import string
import pyperclip
from termcolor import colored

COMMON_WORDS = [
    "apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua",
    "yew", "zucchini"
]

def generate_password():
    password = ""
    for _ in range(4):
        password += random.choice(COMMON_WORDS)
    password = password[:20]
    return password

def main():
    password = generate_password()
    print(colored(password, "green"))
    pyperclip.copy(password)

if __name__ == "__main__":
    main()
