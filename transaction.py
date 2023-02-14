''' Design a Tournament class to have teams of car efficiency enthusiasts collect an inventory of fuel efficient cars by finding sponsorship from car makers. Once sponsors are arranged and teams are formed, teams will compete by facing off head-to-head (pairwise, bracket-style) until only one Tournament.champion prevails. Competitors perform by driving each car in their inventory the distance that 1 gallon of fuel will permit them to travel in highway situations. The winning team of a match will have collectively driven their vehicles the furthest. That is, the sum of the MPG-H ratings in their inventory will be the score that decides the winner.

Begin with the data you have saved in the cardata_modified.csv file. Read in and modify this data so that:

The Prices are rounded to the nearest $100.
Only cars made after the Year 2000 are retained in the DataFrame.
Only car Makeers with more than 55 entries in the dataset are retained in the DataFrame.
Teams will be able to choose cars for their inventory from this modified DataFrame.

1.4.1. Define a Tournament class
The class should be initialised with:
a DataFrame of cars, as designed above
No missing values are permitted.
a tournament name
an optional number of competing teams, defaulting to 16.
If the input number of teams is not an integer, raise the appropriate kind of exception, and a message saying, "The number of teams must be an integer."
Also, assert that the value is positive and non-zero.
Ensure that this number is a perfect square.
Include sensible object representation dunder methods (i.e. __repr__ and __str__).
Add a method to generate_sponsors.
The method should, by default, randomly select a sponsor for each team from the available list of Makeers (with no duplicates).
It should optionally accept a list of specified sponsors with a length up to the number of teams.
If the supplied list is shorter, the remainder of the teams will be set random sponsors, as in the default case.
Once sponsors are assigned, the sponsor should randomly allocate a budget in some range of incremental integer values defined by low, high, and incr parameters to this method. Choose sensible default values for these.
Add a method to generate_teams.
This method should simply populate a list of teams in the Tournament class.
The teams should be members of the Team class, a class internal to the Tournament class.
A Team object should hold information about:
their sponsor
their budget
their inventory
their active status, i.e. whether they are eligible to compete in the next round of the tournament.
their performance record (e.g., win/loss, score, number of cars they used in competition)
This class should also have some kind of __str__ representation.
Be thoughtful about which of these characteristics are mutable and how to change them if they are not mutable.
Add a method to buy_cars.
This method will allow the Teams to each purchase their initial inventory.
Add a method to _purchase_inventory.
This internal method should take 1 argument: a single Team object.
With the information provided by the Team, isolate cars that are available from the sponsoring Makeer.
Considering the Team budget, select the set of cars representing the optimal choice. That is, purchase as many cars as the budget permits, while trying to maximise MPG-H.
For more comprehensive implementations, expect this to be the most computationally expensive part of this sub-task. It can reasonably require a few seconds to perform the task.
When these are selected, the Team's budget and inventory should be updated.
Add a method to hold_event (i.e., execute the tournament competition process.)
Cycle through the matches, keeping track of Team performance metrics.
After each match, allocate a financial prize to the winning Team. You can decide how to implement this; perhaps the prize increases in every round.
After awarding the prize, allow the Team to _purchase_inventory again (increasing the number of cars in their inventory) before the next match.
Newly purchased cars can be duplicates of members of the Team's existing inventory.
At the end of the tournament event, record the Tournament.champion.
1.4.2. Execute your Tournament class
The process of building and executing the stages associated with the tournament might look something like this:

t1 = Tournament(car, "The First Folks")
t1.generate_sponsors()
t1.generate_teams()
t1.buy_cars()
t1.hold_event()
print(f'The champion of {t1.name} Tournament is the {t1.champion}')
...
The champion of The First Folks Tournament is the Team sponsored by Nissan with $32000 available and 32 cars.
You should be able to produce some visual (e.g., printed or plotted) record of the Tournament matches. For example:

t1.show_win_record()
...

         Scion: ['W     ', 'W     ', 'L     ']
        Suzuki: ['L     ']
        Subaru: ['W     ', 'L     ']
    Land Rover: ['L     ']
        Nissan: ['W     ', 'W     ', 'W     ', 'W     ']
         Dodge: ['L     ']
         Lexus: ['L     ']
          Saab: ['W     ', 'L     ']
 Mercedes-Benz: ['L     ']
         Buick: ['W     ', 'L     ']
    Volkswagen: ['W     ', 'W     ', 'L     ']
    Oldsmobile: ['L     ']
       Hyundai: ['W     ', 'W     ', 'W     ', 'L     ']
      Infiniti: ['L     ']
      Cadillac: ['L     ']
           BMW: ['W     ', 'L     ']
1.4.2. Compare the results of multiple Tournament executions
Lastly, execute at least 2 Tournaments in full. Compare the performance of their .champions and produce a ranked representation of the different Tournaments. For example:
Tournament ranking:
Position     Name                     Sponsor                  Score
1            The Other Group          Chevrolet                2044
2            The First Folks          Nissan                   1737

'''


