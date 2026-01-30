# Habit-Tracker
Small, inefficient habit tracker that is still a work in progress

## How to Use
It is missing a lot of features since I originally made this for myself, but I thought others might want something similar so I uploaded it.
As of right now you have to add the activities yourself editing the source code in line 13 to a list of your own activities
Example:
```
ACTIVITIES = [
    "School",
    "Reading",
    "Workout"
]
```

The checked data is saved in a different .json file each month so you can go back and review it if you'd like (either by editing the source code in line 18 to the month's number to access your desired file or checking the file itself)
It's made in a way that the file will be reused the next year, and as of right now it will open with the data you had the year before
