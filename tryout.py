



from typing import List
from scenarios import Scenarios
from spaceship_node import SpaceshipNode
from tsp_utils import TspUtils

# im too lazy to write unit tests, therefore im writing dumb-dumb manual test main functions :) 

spaceship_list: List[SpaceshipNode] = Scenarios.construct_spaceships(spaceshipData=Scenarios.spaceshipData())


res=TspUtils.check_ship_is_valid(ship_list=spaceship_list,ship_name="SpaceX Raptor 2 (Starship)")

print(res)

