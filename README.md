BlogSphere: A Simple Blog Post Website
Welcome to BlogSphere, a lightweight blog platform built with HTML, CSS (Bootstrap), and Flask. It's designed to provide a simple yet interactive blogging experience, allowing users to post, edit, delete, and view their blog posts. With an intuitive login and registration system, BlogSphere lets you personalize your profile and manage content with ease.

Features
🚀 Key Features:
User Authentication: Secure login and registration system.
Add and Delete Posts: Users can add new posts and delete existing ones after logging in.
Personalized Profile: Change your username and profile image.
Pagination: View 5 blog posts per page for a seamless browsing experience.
Responsive Design: Built using Bootstrap for a mobile-friendly, responsive layout.
✨ Interactive Elements:
Account Page: Once logged in, access the account page where you can update your username and upload a profile picture.
Default Profile Image: New users are given a default profile image, which can be changed at any time.
Pagination for Blog Posts: Navigate through blog posts with pagination (5 posts per page).
User-Friendly Design: A clean, intuitive user interface built with Bootstrap for ease of use.
How to Run the Project
Follow these steps to run BlogSphere locally on your machine.

🛠️ Prerequisites:
Install Python (v3.6 or higher) from python.org.
Install Flask:
bash
Copy code
pip install Flask
Install Flask-Mail for sending test emails:
bash
Copy code
pip install Flask-Mail
Make sure you have the necessary HTML, CSS, and Flask setup files.
⚡ Steps to Run the Application:
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/blogsphere.git
cd blogsphere
Run the Flask application:

bash
Copy code
python run.py
Open your browser and go to:

plaintext
Copy code
http://127.0.0.1:5000
You should now see the BlogSphere homepage! 🎉

🔑 Login Details:
For testing purposes, you can log in using the following credentials:

Email: testing@email.com
Password: 12345
Please note, this is a test email, and the login system is set up for local use only.

📱 User Pages:
Login Page: Enter your credentials to log into your account.
Registration Page: Register a new account (for local testing purposes, you can skip this as the default test credentials are available).
Account Page: Once logged in, you can modify your username, change your profile picture, and manage your posts.
Folder Structure
php
Copy code
blogosphere/
│
├── app/
│   ├── static/                 # Contains CSS, JS, and image files
│   ├── templates/              # Contains HTML templates
│   └── routes.py               # Contains Flask route definitions
│   └── forms.py                # Contains forms defintion
    └── models.py               # Conatins models.py
    └── site.db                 # site.db is the database 
├── run.py                      # Main entry point for running the Flask app
├── requirements.txt            # Lists all the necessary Python dependencies
└── README.md                   # This file
Customization
You can easily make modifications to suit your needs:

Modify Blog Post Layout: The design uses Bootstrap for responsiveness. You can tweak the CSS and HTML structure within templates/ to adjust the layout.
Add More Features: Add functionality like comments, search, or even allow multiple images per post.
Improve the UI: Feel free to replace the default profile image and refine the design by updating static/styles.css or modifying the templates.
Screenshots
Here are a few screenshots of BlogSphere to give you a feel of the design:

Homepage with a list of blog posts and navigation options.

Account page where you can update your profile and username.

Contributing
Feel free to contribute to BlogSphere! Whether it's adding new features, improving the code, or fixing bugs, your contributions are always welcome. To get started:

Fork the repository.
Create a new branch.
Make your changes.
Commit and push your changes.
Submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Enhancing Interactivity
For an even more interactive experience, here are some ideas to take your project further:

Live Post Preview: Allow users to preview their blog posts live as they type.
Like or Comment System: Allow other users to like or comment on blog posts.
Post Search: Add a search bar to filter through posts by keywords or tags.
Dark Mode: Implement a toggle for dark/light mode to enhance user experience.
Enjoy building and improving BlogSphere! 🚀


This project is based on a tutorial from YouTube who is Corey Schafer



