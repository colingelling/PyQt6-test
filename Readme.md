# Learning Python with PyQt6
Currently I (author) am being part of a reintegration process to improve my knowledge about modern programming languages and overall my entire skill set. In September 2022, I decided to learn Python since it has the most advantages in a business type of workflow.

This file is part of the documentation of this project. Containing the following subjects:

- The use of Object Oriented Programming
- Organization and structure
- Environmental usage and the handling of secret information
- The navigation between windows
- Sessions

## The use of Object Oriented Programming
In the last years, I attempted to fine tune my knowledge about this structure of programming. I developed a lot of things for web apps and server environment applications. This is where I got my inspiration from for building with the Object Oriented way of processing in mind.

With PyQt6, it goes a little different than I was familiar with. For example the most annoying thing: Circular recursion. I needed to make sure that the application's structure was in a straight line. Different kinds of functionality also could extend or depend on each other, but you have to make sure that functions don't relate to other functions when they return to the earlier function to avoid these recursion mistakes.

That was the most challenging thing around OOP for this type of environment, next to that I had chosen for PyQt6 since I find it nice to work with.

## Organization and structure
This is where the fun begins because here are the contents of the application explained. In this state and particular for the project itself, is the app a test environment and started out as a project for learning and evolving my learning curve with Python.

So this application includes:

1. The main.py file<br>
This file is the original starting point of the application and 'initializes' other functionality.
2. Bootstrapper<br>
Inside the main.py file the bootstrapper has been called, this sets up the controller. Web applications may use this a lot, and since the concept of it is to load multiple background resources, I liked the idea of doing the same thing here.
3. Controllers<br>
The app window state has been handled through the main file, but the Controller(s) are there for serving the ability to switch between windows.
4. 
