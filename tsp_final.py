from asyncio import run, sleep
import asyncio
from typing import List
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
from datetime import timedelta
from custom_exception import MechanicalError
from node import*
from spaceship_node import SpaceshipNode
from scenarios import Scenarios
import pandas  as pd

from tsp_utils import TspUtils

# Assuming the classes are already defined as provided in the question

# Step 1: Create instances of planets with static boost station forces in 'Scenarios'class


extreme_boosters_planet_list: List[BasePlanetNode] = Scenarios.construct_planets_with_boosters(boosters=Scenarios.super_boosters_extreme())
advanced_boosters_planet_list: List[BasePlanetNode] = Scenarios.construct_planets_with_boosters(boosters=Scenarios.super_boosters_realistic())
minimal_boosters_planet_list: List[BasePlanetNode] = Scenarios.construct_planets_with_boosters(boosters=Scenarios.super_boosters_minimal())

# Step 2: Create instances of spaceships with static data in 'Scenarios' class
spaceship_list: List[SpaceshipNode] = Scenarios.construct_spaceships(spaceshipData=Scenarios.spaceshipData())

# Step 3: Create DataFrames to store spaceship capabilities for each booster scenario
spaceships_capable_of_travelling_in_extreme_boosters_planet_list = pd.DataFrame(
    columns=[planet.name for planet in extreme_boosters_planet_list]
)
spaceships_capable_of_travelling_in_advanced_boosters_planet_list = pd.DataFrame(
    columns=[planet.name for planet in advanced_boosters_planet_list]
)
spaceships_capable_of_travelling_in_minimal_boosters_planet_list = pd.DataFrame(
    columns=[planet.name for planet in minimal_boosters_planet_list]
)

def spaceship_capability_comparaison(dataFrame: pd.DataFrame, planetList: List[BasePlanetNode])-> pd.DataFrame:
    """_summary_
    conduct analysis before journey to define which ships are best suited for space travel
    """
    i=0
    while i <=(len(spaceship_list)-1):
        testResult:List=[]
        j = 0
        while j <=(len(extreme_boosters_planet_list)-1):
            try:
                spaceship_list[i].get_time_needed_to_cross_the_atmosphere_of_planet(planet= planetList[j])
                spaceship_list[i].get_time_needed_to_land_on_the_planet_from_its_atmosphere(planet= planetList[j])
                testResult.append(True)
                j+=1
               

            except MechanicalError as e:    
                testResult.append(False)
                j+=1
            except Exception as f:
                print(f)
                
        dataFrame.loc[spaceship_list[i].name]=testResult
        i+=1
        
    print(dataFrame)
    print('\n')     
    print("########### WE SHOULD USE THESE SHIPS ###################")
    reliable_ships=get_list_of_safe_spaceships(dataFrame=dataFrame)
    print(reliable_ships)
    print('\n')
    return  reliable_ships   
        
        
        
def get_list_of_safe_spaceships(dataFrame: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a filtered DataFrame containing only the spaceships that can safely travel to all planets.
    """
    safe_spaceships_df = dataFrame[dataFrame.all(axis=1)]
    return safe_spaceships_df


    
async def main():
   
    print("\n ##### 🔥 Simulated Mecanical Report 🔥 ########")  
    print("\n ######################################### With Extreme Boosters!! 🚀💥🔥")
    extreme_boost_reliable_ships=spaceship_capability_comparaison(dataFrame=spaceships_capable_of_travelling_in_extreme_boosters_planet_list,planetList=extreme_boosters_planet_list)
   
    print("\n ######################################### With Advanced Boosters: 🚀✨⚡")
    advanced_boost_reliable_ships=spaceship_capability_comparaison(dataFrame=spaceships_capable_of_travelling_in_advanced_boosters_planet_list,planetList=advanced_boosters_planet_list)
    
    print("\n ######################################### With Minimal Boosters: 🚀🌱")
    minimal_boost_reliable_ships=spaceship_capability_comparaison(dataFrame=spaceships_capable_of_travelling_in_minimal_boosters_planet_list,planetList=minimal_boosters_planet_list,)
    
    print("scenario EXTREME 1 -------------------------------")
    fastest_ship=TspUtils.construct_brute_force_algorithm(
        chosen_planet_list=extreme_boosters_planet_list,
        reliable_ships=extreme_boost_reliable_ships,
        global_ship_list= spaceship_list,
        starting_node="Earth"
        )
    TspUtils.show_graph(bruit_force_result=fastest_ship,)
    print("scenario EXTREME 1 complete ... starting new simulation ⌛⌛⌛")
    await sleep(delay=1)
    print("scenario Advanced 2 -------------------------------")
    fastest_ship2=TspUtils.construct_brute_force_algorithm(
        chosen_planet_list=advanced_boosters_planet_list,
        reliable_ships=advanced_boost_reliable_ships,
        global_ship_list= spaceship_list,
        starting_node="Earth"
        )
    TspUtils.show_graph(bruit_force_result=fastest_ship2,)
    print("scenario Advanced 2 complete ... starting new simulation ⌛⌛⌛")
    await sleep(delay=1)
    
    print("scenario Minimal 3 -------------------------------")
    fastest_ship3=TspUtils.construct_brute_force_algorithm(
        chosen_planet_list=minimal_boosters_planet_list,
        reliable_ships=minimal_boost_reliable_ships,
        global_ship_list= spaceship_list,
        starting_node="Earth"
        )
    TspUtils.show_graph(bruit_force_result=fastest_ship3,)
    print("scenario Advanced 2 complete ... starting new simulation")
    
    
   
asyncio.run(main())