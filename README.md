Disaster Response AI System

Project Summary
I built an AI-powered system designed to help a drone navigate through a disaster zone. The drone has to find the quickest path from a starting point to a goal while avoiding obstacles like debris.

What I Created
The "Brain" (A Algorithm):* I used the A* (A-Star) algorithm to make the drone smart. Instead of searching randomly, it uses a calculation (Manhattan distance) to choose the shortest path to the goal.

The "World" (10x10 Grid): I built a digital map that represents a disaster area where the drone can move and detect obstacles.

The "Dynamic Re-planner": I added a feature that simulates a change in the environment. If the drone is moving and suddenly hits a new obstacle, it automatically stops and calculates a brand-new path to get around it.

Data Logging: I built a custom logger that automatically records how long the AI takes to make decisions. This gives me real data to prove that my system is fast and efficient.

Why My Project is Different
Instead of just writing code that works once, I built a modular system. Every part of the project is in a separate file (Environment, AI Engine, Logger), which makes the code clean and professional. I also have an automated performance_log.csv file that tracks my results, which I used for my project evaluation.

How to run it
Make sure you have Python installed.

Download the files.

Simply run the following command in your terminal:

Bash
python main.py

Reflections (Part E)
I learned that building AI for disaster zones is not just about the math; it’s about safety. In a real-world scenario, I believe an AI like this should have a "Human-in-the-Loop" feature, where a human responder has the final say before the drone follows a new path to ensure it doesn't accidentally interfere with rescue operations.
