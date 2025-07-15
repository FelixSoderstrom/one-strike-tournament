# Contributions rules

1. Contributions must be delivered in a folder.
2. The root MUST include a 'main.py' file.
3. the 'main.py' file must have an 'actions()' function.
4. The actions function MUST return a dictionary: 
{
    "walk_left": True,
    "walk_right": True,
    "dash_left": True,
    "dash_right": True,
    "attack": True,
    "block": True,
}




# Game loop

1. Capture screen
2. Vectorize image
3. Normalize image
4. Check if game is started/over
5. Get player action
6. Press buttons on controller




# Thoughts

- We need to prevent contribution classes (p1, p2) from getting images if the class is already running inference.
If the class is currently working on getting output for a previous image, we shouldnt give them a new one.
This would prevent the class from processing old images.
