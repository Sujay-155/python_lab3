import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

# In-Memory Storage: Simulate a database using a list of dictionaries
user_records = []

# Lambda function to create a new user record
create_user = lambda name, email: {'name': name, 'email': email}

# Lambda function to insert the user record into the list
insert_user = lambda user: user_records.append(user)

# Lambda function to fetch all user records from the list
fetch_all_users = lambda: user_records


# Function to generate QR code from inputted data
def generate_qr_code(data):
    img = qrcode.make(data)
    img.save('imgqr.png')
    print("Image generated and saved as imgqr.png")


# Function to decode the QR code
def decode_qr_code(image_path):
    img = Image.open(image_path)
    decoded_data_raw = decode(img)
    if decoded_data_raw:
        decoded_data = decoded_data_raw[0].data.decode('utf-8')
        return decoded_data
    return ""


# User Registration Function
def RegisterUserFromSmartScan(image_path):
    # Decode the SmartScan Code to extract user data
    user_data = decode_qr_code(image_path)

    # Split user data by newlines if multiple records are encoded
    records = user_data.split('\n')

    for record in records:
        try:
            # Extract name and email from the decoded data
            name, email = record.split(',')

            # Create a new user record using the lambda function
            new_user = create_user(name, email)

            # Insert the user record into the in-memory list
            insert_user(new_user)
        except ValueError:
            print(f"Skipping invalid record: {record}")

    # Print the list of all registered users
    print("Registered Users:")
    for user in fetch_all_users():
        print(f"Name: {user['name']}, Email: {user['email']}")