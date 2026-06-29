Project Summary

I built an AI-powered system that helps a drone navigate a disaster zone by finding the quickest path from start to finish while avoiding dangerous debris.

Core Features

The "Brain" (A Algorithm):* I implemented the A* algorithm, which uses smart calculations to find the shortest path instead of searching randomly.

Dynamic Re-planning:
If the drone hits a new obstacle while moving, it automatically stops and calculates a brand-new path to get around it.

Data-Driven Analysis: I created a custom logger that saves performance results to performance_log.csv, giving me real data to prove the system is fast and efficient.

Why My Project Is Different

This project stands out from standard tutorials because:

Modular Architecture: 
I separated the code into distinct files (Environment, AI Engine, Logger), which is how professional software is built.

Baseline Comparison:
I included a Dijkstra baseline to perform a comparative analysis, which provides mathematical proof that my A* implementation is more efficient than a basic blind search.


Real-World Logic:
The system handles real-time environment changes, simulating the unpredictable nature of actual disaster sites.


How to Run

Ensure Python 3.x is installed.

Run the following command in your terminal:

Bash
python main.py


Reflections

I learned that building AI for disaster zones is about more than just math; it is about safety. I believe an AI like this should always include a "Human-in-the-Loop" feature, where a human responder reviews the drone’s path to ensure it does not interfere with critical rescue operations.
