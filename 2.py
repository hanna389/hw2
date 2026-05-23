import csv
import os

def load_contact_book(path: str) -> list[dict[str, str]]:
    if not os.path.exists(path):
        return []

    with open(path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [dict(row) for row in reader]


def print_contact_book(contact_book: list[dict[str, str]]):
    for i, contact in enumerate(contact_book):
        print(f"[{i}] {contact}")


def save_contact_book(path: str, contact_book: list[dict[str, str]]) -> None:
    if not contact_book:
        return

    with open(path, mode="w", encoding="utf-8", newline="") as file:
        fieldnames = list(contact_book[0].keys())
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(contact_book)


def add_contact(
    contact_book: list[dict[str, str]], new_contact: dict[str, str]
) -> None:
    for contact in contact_book:
        if contact["email"] == new_contact["email"]:
            print(f"Contact with email {new_contact['email']} already in contact book.")
            return

    contact_book.append(new_contact)


def get_new_contact() -> dict[str, str]:
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")

    return {"first_name": first_name, "last_name": last_name, "email": email}


def remove_contact(contact_book: list[dict[str, str]]):
    index = None

    while not index:
        new_index = int(input("Enter index of contact to remove: "))
        if new_index < 0 or new_index >= len(contact_book):
            print("Invalid index. Try again.")
        else:
            index = new_index

    contact_book.pop(index)


HELP_TEXT = """
Allowed commands:
- add
- remove
- print
- exit
- help
""".strip()

def main():
    contact_book = load_contact_book("./contacts.csv")
    print_contact_book(contact_book)

    is_running = True
    while is_running:
        command = input("Enter command: ").strip().lower()

        if command == "help":
            print(HELP_TEXT)
        elif command == "add":
            add_contact(contact_book, get_new_contact())
        elif command == "remove":
            print_contact_book(contact_book)
            remove_contact(contact_book)
        elif command == "print":
            print_contact_book(contact_book)
        elif command == "exit":
            is_running = False
        else:
            print(f"Unknown command {command}. Use \"help\" to get a list of allowd commands.")

    save_contact_book("./contacts.csv", contact_book)

if __name__ == "__main__":
    main()