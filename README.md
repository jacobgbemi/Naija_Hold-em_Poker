# Naija Hold-em Poker

![Game Screenshot](https://github.com/jacobgbemi/Texas_Hold-em_Poker/blob/master/poker/static/images/front_page/you.png)

[Naija Hold-em Poker](http://jacobgbemi.pythonanywhere.com/) is a web application designed to simplify the game of poker for beginners. The game is designed for Africans who know little or nothing about this card game.
To achieve this, betting is not implemented, and there is only two players, the Bot and the login player, while the rounds of pre-flop, flop, turn and river are merged into a single click of play button. Players can play as many times as they want, see their given cards and their best hands, including whether it is a win, lose or draw.

## Table of Content
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [The Approach](#The-Approach)
- [Authors](#Authors)
- [Features to Further Explored](#Features-to-Further-Explored)
- [Acknolodgement](#Acknolodgement)
- [References](#References)

## Introduction
We planned to create a game web application but we were not sure where to start from. After much deliberations, poker game was chosen. This is because board games and some few card games are more popular in Africa than poker game.
Although, there are about 13 different poker games, We're going to name ours Naija Hold'em Poker and be making our own rules.
Our implementation does not include betting. It is meant to make the game simple enough for a beginner. It utilizes Python, REST API and ORM for the ```backend``` and Jinja2 and HTML/CSS for the ```frontend ``` because of our familiarty with these functionalities.

### Frontend
- Jinja2 handles the routing
- CSS/HTML for building the game interface and player info
- Boostrap to make it responsive to different media

### Backend
- Handles GET, POST request
- Handles CRUD manipulation through REST API

### Database
Handles ORM (SQLAlchemy)
Creates model system
Create one to many relationship for players and comments

### Deployment
- Deployed on pythonanywhere

## The-Approach
- Test driven development (TDD) was implemented in building the game algorithms
- The deck is made up of 52 cards
- Each player gets 2 hole cards first

## Installation
- To install the app, simply clone this repository. 
- Make sure to install the requirements ```pip install -r requirement.txt```.
- Run the app.py ```python3 app.py```

## Usage
- To use this web application, kindly visit [Naija Hold-em Poker](http://jacobgbemi.pythonanywhere.com/).
- You will need to register and login before you can play the game
- After login, click ```start game```
- Then ```play```, and ```play again``` and again, until you ```quit```.
- Take note of ```How to Play``` and ```Poker Hands Ranking``` to help you understand the game.
- Players can ```add```, ```update```, and ```delete``` comments to express how they feel about the game.
- Players can see their game history (this feature is not working yet).

### Authors
- Gbemi Jacob Adebayo [LinkedIn]() | [Twitter]() | [GitHub]()
- Gbemi, aka Jag is a process engineer, a project engineer and a software enthusiast.
- Oluwadamilare Adedokun [LinkedIn](https://www.linkedin.com/in/oluwadamilare-adedokun-32a999256) | [Twitter](https://twitter.com/dev_damadet) | [GitHub](https://github.com/damadet)
- Oluwadamilare, aka Damadet is a digital artist looking to transition into tech.

### Features-to-Further-Explore
- Adding the game history
- Adding multiple players at the same time
- Adding betting functionality

### Acknolodgement
- Appreciation to [ALX SE School](https://alxafrica.com)
- And all other cohort 6 peers who had collaborated one way or the order.

### References
- [Poker page](https://www.playpokeronline.com/)
- [Youtube](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
- Other pages
