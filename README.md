# Pong Game

This is a Pong Game which sends mouse position to BigQuery. The game is constructed using Object Oriented paradigm with Visitor pattern.

Run main.py file in the lib folder to start the game.

After the game, we have the mouse positions during the game. We can use this data to check and authorise the person who played the game (just like a password). The main assumption is  that each person has unique play style.

The reason for choosing Object Oriented Paradigm is that I wanted to get more familiar with it. The reason for choosing the Visitor pattern was the realization that I need a system that in which, each component communicates with all other component. I cant have some components communicate only with some components (the ball should communicate with the bar and the walls, the bar should communicate with the walls).
