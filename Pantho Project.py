import csv

# File to store vaccine data
DATA_FILE = 'vaccine_data.csv'

def initialize_file():
    """Create the CSV file if it doesn't exist."""
    try:
        with open(DATA_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'NID', 'Age', 'Vaccine Status'])
    except FileExistsError:
        pass

def register_person():
    """Register a new person for vaccination."""
    name = input("Enter your name: ")
    nid = input("Enter your NID (National ID): ")
    age = input("Enter your age: ")
    
    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, nid, age, 'Pending'])
        print(f"Registration successful for {name}!")

def check_status():
    """Check vaccine status using NID."""
    nid = input("Enter your NID to check status: ")
    
    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            if row[1] == nid:
                print(f"Name: {row[0]}, Age: {row[2]}, Vaccine Status: {row[3]}")
                return
        print("No record found with that NID.")

def update_status():
    """Update a person's vaccine status."""
    nid = input("Enter your NID to update status: ")
    new_status = input("Enter new vaccine status (Pending, 1st Dose Taken, Fully Vaccinated): ")
    
    rows = []
    found = False

    with open(DATA_FILE, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows:
        if row[1] == nid:
            row[3] = new_status
            found = True

    if found:
        with open(DATA_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Vaccine status updated successfully!")
    else:
        print("No record found with that NID.")

def main():
    initialize_file()
    while True:
        print("\n--- COVID-19 Vaccine Tracker ---")
        print("1. Register for Vaccine")
        print("2. Check Vaccine Status")
        print("3. Update Vaccine Status")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            register_person()
        elif choice == '2':
            check_status()
        elif choice == '3':
            update_status()
        elif choice == '4':
            print("Thank you! Stay safe.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()

