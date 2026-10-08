import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry_text = input("\nEnter your journal entry:\n")
            if not entry_text.strip():
                print("Entry cannot be empty!")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            formatted_entry = f"[{timestamp}]\n{entry_text}\n\n"

            
            with open(self.filename, 'a', encoding='utf-8') as file:
                file.write(formatted_entry)

            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied to write to the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_entries(self):
        try:
            
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()
                if not content.strip():
                    print("\nNo journal entries found. Start by adding a new entry!")
                else:
                    print("\nYour Journal Entries:")
                    print("----------------------------------------")
                    print(content.strip())

        except FileNotFoundError:
            print("\nNo journal entries found. Start by adding a new entry!")
        except PermissionError:
            print("Error: Permission denied to read the file.")
        except Exception as e:
            print(f"An error occurred while reading: {e}")

    def search_entry(self):
        try:
            keyword = input("\nEnter a keyword or date to search:\n").strip()
            if not keyword:
                print("Search keyword cannot be empty!")
                return

            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read()

            
            entries = content.strip().split("\n\n")
            matching = []
            for entry in entries:
                if keyword.lower() in entry.lower():
                    matching.append(entry)

            if matching:
                print("\nMatching Entries:")
                print("----------------------------------------")
                for m in matching:
                    print(m)
                    print()  
            else:
                print(f"\nNo entries were found for the keyword: {keyword}.")

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.")
            
        except Exception as e:
            print(f"Search failed due to: {e}")

    def delete_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("\nNo journal entries to delete.")
                return

            confirm = input("\nAre you sure you want to delete all entries? (yes/no): ").strip().lower()
            if confirm == 'yes':
                
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")
            else:
                print("\nDeletion cancelled.")

        except FileNotFoundError:
            print("\nNo journal entries to delete.")
        except PermissionError:
            print("Error: Permission denied to delete the file.")
        except Exception as e:
            print(f"Failed to delete entries: {e}")


def main():
    manager = JournalManager("journal.txt")

    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:")
        print("\n1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("\nUser Input:\n").strip()

        if choice == '1':
            manager.add_entry()
        elif choice == '2':
            manager.view_entries()
        elif choice == '3':
            manager.search_entry()
        elif choice == '4':
            manager.delete_entries()
        elif choice == '5':
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("\nInvalid option. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()
