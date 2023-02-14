import pandas as pd
import numpy as np
import random

class Team:
    def __init__(self, sponsor, budget):
        self.sponsor = sponsor
        self.budget = budget
        self.inventory = {}
        self.active = True
        self.record = {'win': 0, 'loss': 0, 'score': 0, 'cars_used': 0}

    def __str__(self):
        return f'Team {self.sponsor}: ${self.budget} budget, {len(self.inventory)} cars in inventory, {"active" if self.active else "eliminated"}'

class Tournament:
    def __init__(self, cars_df, name, num_teams=16):
        if not isinstance(num_teams, int):
            raise TypeError("The number of teams must be an integer.")
        if num_teams <= 0:
            raise ValueError("The number of teams must be positive and non-zero.")
        if int(num_teams**0.5)**2 != num_teams:
            raise ValueError("The number of teams must be a perfect square.")
        self.cars_df = cars_df
        self.name = name
        self.num_teams = num_teams
        self.teams = []
        self.sponsors = None
        self.champion = None

    def __repr__(self):
        return f'Tournament({self.name}, num_teams={self.num_teams})'

    def __str__(self):
        return f'{self.name} Tournament ({self.num_teams} teams)'

    def generate_sponsors(self, specified_sponsors=None, low=100, high=1000, incr=100):
        if specified_sponsors and len(specified_sponsors) > self.num_teams:
            raise ValueError("The specified number of sponsors cannot be greater than the number of teams.")
        if not self.sponsors:
            self.sponsors = list(set(self.cars_df['Makeer']))
        if specified_sponsors:
            random.shuffle(self.sponsors)
            self.sponsors = specified_sponsors + self.sponsors[len(specified_sponsors):self.num_teams]
        else:
            random.shuffle(self.sponsors)
            self.sponsors = self.sponsors[:self.num_teams]
        for i, sponsor in enumerate(self.sponsors):
            budget = random.randint(low, high)
            budget = budget - budget % incr
            team = Team(sponsor, budget)
            self.teams.append(team)

    def generate_teams(self):
        if not self.sponsors:
            self.generate_sponsors()
        for team in self.teams:
            self._purchase_inventory(team)

    def _purchase_inventory(self, team):
        makeer_cars = self.cars_df[self.cars_df['Makeer'] == team.sponsor]
        makeer_cars = makeer_cars[makeer_cars['MSRP'] <= team.budget]
        makeer_cars = makeer_cars.sort_values('MPG-H', ascending=False)
        num_cars = min(len(makeer_cars), len(team.inventory) + int(team.budget/makeer_cars['MSRP'].min()))
        chosen_cars = makeer_cars.iloc[:num_cars]
        for _, car in chosen_cars.iterrows():
            team.inventory[car['Model']] = car
            team.budget -= car['MSRP']
        team.record['cars_used'] += num_cars

    def buy_cars(self):
        if not self.sponsors:
            self.generate_sponsors()
        for team in self.teams:
            self._purchase_inventory(team)

    def hold_event(self):
        round_num = 0
        while len(self.teams) > 1
