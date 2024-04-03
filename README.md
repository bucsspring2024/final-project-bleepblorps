
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Team Members

Steven Doljansky

***

## Project Description

Pyramid scheme simulator. Run and manage your own pyramid scheme. Will you pay off your devastating financial obligations in time?

***    

## GUI Design

Top window showing money owed to IRS, Banks, and Mafia on the right side and slider allowing you to take out loans with varying interest rate tied to your credit score (tied to previous loans owed) as well as a display showing interest owed which is deduced by your interest rate and total loans.

Timer in the middle top of the screen of 7 minutes countdown when press play

Starts with one person (you) in the middle of the screen and you purchase button. Click button 100 times to hire first person.
Each person on the most bottom layer makes $15. Second layer of people hire a new person every 30-50 seconds. Stop hiring after 4 people on second layer (people hired by second layer before also hire a new person in 20-30 seconds). $15 per 25 seconds on very bottom layer. Each layer adds 1 to power of money made on the layer below them.


def generate_random_string(length):
    letters = string.ascii_letters
    result_str = "".join(random.choice(letters))

name = 'A'
people = {}
for _ in range(1000):
    people[name] = random.randint(10)
    name = ord(name)
json.dump()

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start Screen Before Game/Timer Starts
2. Countdown Timer
3. Button (clicker to hire next employee)
4. Visual Representation of Totally Not a Pyramid Scheme
5. Names of Employees

### Classes

- << You should have a list of each of your classes with a description >>

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
