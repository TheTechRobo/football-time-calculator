# football-time-calculator
I don't like football, but here's a calculator to convert from "football time" to approx. real time.

# Usage
```
>>> from footballTimeCalculator import *
>>> calculateFootballTimeToReal(1)
2.5
```

Or, if you prefer it to be interactive, run `main.py`.

# Todo
Turn into an app with GUI.

# Algorithm
Algorithm comes from the fact that a football game is supposed to last 60 minutes, but actually lasts two and a half hours. So I multiply the rogiinal number by 2.5 and it works! Sadly it doesn't account for overtime but that's because it's unpredictable.
