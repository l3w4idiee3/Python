addressBook = {
    'phoneNumber': [],
    'emailAddress': ''
}

def add_contact():
    name = input("Enter the contact name: ")
    phone_number = input("Enter the phone number: ")
    email_address = input("Enter the email address: ")
    addressBook['phoneNumber'].append(phone_number)
    addressBook['emailAddress'] = email_address
    print(f"Contact '{name}' added successfully!")

def search_contact():
    name = input("Enter the contact name: ")
    if name in addressBook['phoneNumber']:
        print(f"Contact '{name}' found!")
        print("Phone Number:", name)
        print("Email Address:", addressBook['emailAddress'])
    else:
        print(f"Contact '{name}' not found!")
def update_contact():
    name = input("Enter the contact name: ")
    if name in addressBook['phoneNumber']:
        new_phone_number = input("Enter the new phone number: ")
        new_email_address = input("Enter the new email address: ")
        addressBook['phoneNumber'].remove(name)
        addressBook['phoneNumber'].append(new_phone_number)
        addressBook['emailAddress'] = new_email_address
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found!")
def delete_contact():
    name = input("Enter the contact name: ")
    
    if name in addressBook['phoneNumber']:
        addressBook['phoneNumber'].remove(name)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found!")

# Test the functions
add_contact()
search_contact()
update_contact()
search_contact()
delete_contact()
search_contact()