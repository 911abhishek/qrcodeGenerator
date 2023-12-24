import re
import qrcode
from PIL import Image

def username_finder(choice, link):
    match choice:
        case "1":
            username_pattern = r'https?://(?:www\.)?instagram\.com/([^/?]+).*'
        case "2":
            username_pattern = r'https?://(?:www\.)?youtube\.com/(?:channel/|user/)?([^/?]+).*'
        case "3":
            username_pattern = r'https?://(?:www\.)?github\.com/([^/?]+).*'
        case "4":
            username_pattern = r'https?://(?:www\.)?wa\.me/([^/?]+).*'
        case "5":
            username_pattern = r'https?://(?:www\.)?facebook\.com/([^/?]+).*'

    match = re.match(username_pattern, link)
    if match:
        username = match.group(1)
        return username
    else:
        return "Username not found"

def qr_generator():
    link = input("Enter your link : ")
    # link = "https://github.com/911abhishek"
    print("Choose website of provided link:\n Instagram : 1\n Youtube :2\n Github: 3\n Whatsaap: 4\n Facebook: 5")
    choice = input("Please choose one: ")
    user_name = username_finder(choice, link)

    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="blue", back_color="white")
    if user_name == "Username not found":
        print("ERROR\nTry Again")
    else:
        img.save(f"{user_name}QR.png")
        img.show()

def main():
    qr_generator()

if __name__ == "__main__":
    main()
