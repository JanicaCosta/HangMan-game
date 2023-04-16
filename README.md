# HANGMAN game

Hangman is an old-school favorite, a word game where the goal is simply to find the missing word or words Python terminal game, which runs in the Code Institute mock terminal on Heroku.

As Part of the project 3, I have choosen this game show my skills and my knowladge on python.

You can try the game here:
https://hangman-project3-joao.herokuapp.com/


# Data Model

This is the flowchart made during the planning stage of the project. This flowchart has been used to visualise the functions and behavior control during the building stage of the project.

![image](https://user-images.githubusercontent.com/117991189/232302350-e51fef8e-745b-4c70-81b1-623e5580dd67.png)

# How to play

* You will have to choose on which category to select, in this game you can choose or Countries/Cities or Football clubs

* You will be presented with a number of blank spaces representing the missing letters you need to find.

* Use the keyboard to guess a letter.

* If your chosen letter exists in the answer, then all places in the answer where that letter appears will be revealed.

* Every time you guess a letter wrong you lose a life and the hangman begins to appear, piece by piece.

* To win you need to solve the puzzle before the hangman dies.


# Technology


*  This game was created with:

    * [Gitpod](https://www.gitpod.io/) used to develop a project and organise version control 

    * [Github](https://github.com) used to host repository
       
    * [Heroku](https://id.heroku.com/login) used to deploy my application

* [Lucid](https://lucid.app/users/login#/login) used to create the flowchart for the project.

* The Code Institute's GitHub [python-essentials-template](https://github.com/Code-Institute-Org/python-essentials-template) for Python is used in order for the program to display properly in the deployed site on Heroku.

* [random](https://docs.python.org/3/library/random.html) to randomize anagram

* [time](https://docs.python.org/3/library/time.html) to slow down printed statements

* [Python 3](https://www.python.org/) - an interpreted high-level general-purpose backend programming language.

# Features

## Reception

![image](https://user-images.githubusercontent.com/117991189/232332589-6f94c5b1-be5b-4650-b1d6-7bf609db5532.png)

at the beggining we have a the title of the game, which will be clear after few seconds.

## Register the name of the player

![image](https://user-images.githubusercontent.com/117991189/232332725-265317f2-234f-4582-be4d-6578618530fc.png)

A function to get a valid name was cretead where has been put few conditions as no numbers and no more then 8 letters, otherwise will come with an error.

![image](https://user-images.githubusercontent.com/117991189/232332811-5a00f8fb-b361-43e3-9c91-108817d68492.png)


## Rules of the game

![image](https://user-images.githubusercontent.com/117991189/232332843-fbf4b9b4-12c6-43c6-85c8-7b8272d58b68.png)


Will be asked to the player if knows the rules for the game. again, if the player does not asnwer yes or no, will come with an error. some colours and styling has been added.

![image](https://user-images.githubusercontent.com/117991189/232332900-084877a8-002d-448f-bec4-968631e8174f.png)

if the says yes, will proceed, if the players says no will show the rules.

## Function to clear the screen after 2 seconds

a function to clear screen has been created to clear the screen after 3 seconds, to not fill up the screen with code.

![image](https://user-images.githubusercontent.com/117991189/232333112-9126db57-fff8-41dc-9151-5908e06a2ca0.png)


## choose the category for the game

![image](https://user-images.githubusercontent.com/117991189/232333155-e66dd7d5-875a-49f2-946a-0f7c33a57ea6.png)

has been created two diferent categories with few words
the function choose the category is giving 2 options to the player, if he choose any other number than 1 or 2 will come with a error. the question will be asked again.

![image](https://user-images.githubusercontent.com/117991189/232333203-42495e21-0518-4084-91ec-c3b1b8e1209e.png)

## Game starts

the game will start when 









