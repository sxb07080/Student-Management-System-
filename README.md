# Student Management System:

Hey there! So, the project I've been working on is a Student Management System. It's pretty cool because it lets users do a bunch of things related to managing student records, all through a user-friendly interface.

First off, when you want to use the system, you've got to register an account. It's straightforward but needs a unique username and a password that meets certain criteria—like having special characters, digits, uppercase and lowercase letters, and being between 6 to 12 characters long. Oh, and don't worry about security; passwords are MD5 hashed before they're stored.

Once you're registered, logging in is easy. If you mess up your username or password, it'll prompt you to try again until you get it right.

Now, onto the fun stuff—managing student records! Once you're logged in, you can add new students, update their info, delete them if needed, and even look up student scores for different courses. Everything's stored neatly in an SQLite database, managed using SQLAlchemy.

The system lets you show all students or filter them by name or ID, which is super handy when you've got a lot of data to sort through. Adding students is also straightforward, with validations for things like names (first letter capitalized, no digits), ages (between 0 and 100), and phone numbers in a specific format.

For scores, you can view and update grades for courses like CS 1030, CS 1100, and CS 2030. And if you need to tweak a student's details—like their age, major, or phone number—you can do that too.

Behind the scenes, the database structure is set up to ensure everything runs smoothly. We've got tables for users (that's where your account info goes), students (all the student data), and scores (for their grades). Each student gets a unique ID that starts from 700300001, which helps keep everything organized.

Oh, and we've added some neat features to handle errors gracefully and make sure everything inputted is in the right format. Regular expressions come in handy for checking things like phone numbers, and utility functions keep our code clean and easy to manage.

Overall, it's been a great project for learning about databases, security (thanks to MD5 hashing), and how to handle different types of data validation. Plus, it's really satisfying to see how all these pieces come together to create a functional and reliable system for managing student records.
