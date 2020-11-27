#  Day 55 - Intermediate+ HTML & URL Parsing in Flask and the Higher Lower Game

Markup : 

1. Create a new project in PyCharm called higher-lower, add a server.py file.

2. Create a new Flask application where the home route displays an <h1> that says "Guess a number between 0 and 9" and display a gif of your choice from giphy.com.

Alternatively use the one I found on Giphy: https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif

3. Generate a random number between 0 and 9 or any range of numbers of your choice.

4. Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" and checks that number against the generated random number. If the number is too low, tell the user it's too low, same with too high or if they found the correct number. try to make the <h1> text a different colour for each page.  e.g. If the random number was 5:

3 is too low:

7 is too high:

and 5 is just right:

Here are the GIF URLs I used, but it's way more fun finding your own on giphy.com

High: https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif

Low: https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif

Correct: https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif

[Solution](https://gist.github.com/angelabauer/26eb9190a094761a9f49b22e8ee4c0fb)

## Installing
```sh
pip install -r requirements.txt
```

```sh
set FLASK_APP=hello.py
```

Run server
```sh
python -m flask run
```

## Advanced Decorators
[task](https://repl.it/@appbrewery/day-55-1-exercise#README.md)

[my_solution](main.py)

[solution](https://repl.it/@appbrewery/day-55-1-solution#main.py)
