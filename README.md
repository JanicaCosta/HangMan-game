# HANGMAN game

Hangman is an old-school favorite, a word game where the goal is simply to find the missing word or words Python terminal game, which runs in the Code Institute mock terminal on Heroku.

As Part of the project 3, I have choosen this game show my skills and my knowladge on python.

You can try the game here:
https://hangman-3project-joaocosta.herokuapp.com/


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

![image](https://user-images.githubusercontent.com/117991189/232340031-8502ef43-cb1b-4c52-9e2b-afe65fbf6375.png)

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

the game will start when the hangman drawn it starts and shows the number of letter for the ramdom word.

![image](https://user-images.githubusercontent.com/117991189/232338616-5392b928-7aef-4dd3-999a-14748e9a1596.png)

the goal is to the player guess the word, if he fails, the code will tell you the word and will show game over.

if you guess the word, you won.
![image](https://user-images.githubusercontent.com/117991189/232338743-15421ca9-3a3c-45a4-ac38-00873cbc3e51.png)


## game finnished 

at the end of the game, you will have the chance to play again, or if not, you can finished and the code will show you a message thanking you for playing.

![image](https://user-images.githubusercontent.com/117991189/232338845-51592523-ab88-443b-8bcb-2cc7d7989a91.png)

# Validator testing

![image](https://user-images.githubusercontent.com/117991189/232339696-a4063856-7587-4b52-bf8f-c51b342c2afb.png)
* No errors were returned from PEP8online.com

![image](https://user-images.githubusercontent.com/117991189/232340238-ebbe2717-b770-4f42-9dae-352f5e773139.png)
* lighthouse tested

![image](https://user-images.githubusercontent.com/117991189/232340593-ee6e348e-eadc-4b8a-a841-379977c53f11.png)
* [Python tutor](https://pythontutor.com/visualize.html#mode=edit)


# Deployment steps

1. Git add and git commit the changes made

2. Log into [Heroku](https://id.heroku.com/login) or create a new account and log in

3. top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

4. Write app name - it has to be unique, it cannot be the same as this app

5. Choose Region - I am in Europe

6. Click "Create App" The page of your project opens.

7.  Choose "settings" from the menu on the top of the page

8. Go to section "Config Vars" and click the button "Reveal Config Vars"

9. In the field for "KEY" enter "PORT"-  capital letters and value"8000" 

10. Go to section "Build packs" and click "Add build pack"

   * in this new window - click Python and "Save changes" [`Heroku/Python`]
   * click "Add build pack" again
   * in this new window - click Node.js and "Save changes" [`Heroku/NodeJS`]
   * take care to have those apps in this order: [`Python`] first, [`Node.js`] second, drag and drop if needed

11. Next go to "Deploy" in the menu bar on the top

12. Go to section "deployment method", choose "GitHub"

13. New section will appear "Connect to GitHub" - Search for the repository to connect to

14. type the name of your repository and click "search"

15. once Heroku finds your repository - click "connect"

16. Scroll down to the section "Automatic Deploys"

17. Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy
   * As I wanted to have control over when to deploy the version, I have chosen manual deployment by pressing the Deploy branch button instead of Enable Automatic Deploys 

18. Click "Deploy branch"

Once the program runs: you should see the message "the app was successfully deployed"

 19. Click the button "View". This View button will open the terminal game in the new window. Here is the deployed page [Hangman](https://hangman-game1x.herokuapp.com/)

 20. As manual deployment was chosen, I had to come back to the Heroku deployment page whenever I have an updated working version pushed into the GitHub page.

# Images

Are created by using ASCII art. 
http://patorjk.com/software/taag/#p=display&f=ANSI%20Regular&t=Hangman

the main image for the reception.

![image](https://user-images.githubusercontent.com/117991189/232340395-29212052-c5d2-4b4c-a7ba-76d0fd8edd88.png)










