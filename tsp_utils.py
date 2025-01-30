from abc import ABC
from datetime import timedelta
from itertools import permutations
from typing import Dict, List, Tuple
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from node import BasePlanetNode
from spaceship_node import SpaceshipNode
import networkx as nx


class TspUtils(ABC):
    # brute force
    @staticmethod
    def build_time_matrix(formatted_planet_list:List[BasePlanetNode], spaceship:SpaceshipNode,)-> np.ndarray:
        
        n= len(formatted_planet_list)
        time_matrix = np.zeros((n,n))
        for i in range(n): 
            for j in range(n):
                time_matrix[i][j]=spaceship.calculate_total_journey_time_from_planetA_to_planetB(planetA=formatted_planet_list[i],planetB= formatted_planet_list[j]).total_seconds()    
        return time_matrix
    
    @staticmethod
    def check_ship_is_valid(ship_name:str, ship_list:list[SpaceshipNode])->SpaceshipNode:
      
        res : SpaceshipNode = None
        for i in range(len(ship_list)):
            if ship_name == ship_list[i].name: 
                res = ship_list[i]
        if res == None:
           raise TypeError(f"ship {ship_name} is not a known ship name")
        else :
            return res    
    
    @staticmethod
    def tsp_brute_force(time_metrix: np.ndarray,formatted_planet_list : List[BasePlanetNode], shipName:str,):
        
        best_tour_order: List[int]=[]
        number_of_planets: int= len(formatted_planet_list) 
        node_edges: List[timedelta] = None
        tour_time:timedelta = timedelta.max
        
        for perm in permutations(range(number_of_planets)):
            total_time= timedelta()
            test_edges=[]
            
            for i in range(number_of_planets-1):
                total_time += timedelta(time_metrix[perm[i]][perm[i+1]])
                test_edges.append(timedelta(time_metrix[perm[i]][perm[i+1]]))
            total_time+= timedelta((time_metrix[perm[-1]][perm[0]]))
            test_edges.append(timedelta(time_metrix[perm[-1]][perm[0]]))
            
            if total_time < tour_time:
                tour_time = total_time
                node_edges= test_edges
                best_tour_order = perm + (0,)
        formatted_best_tour_output= []
        for i in range(len(best_tour_order)-1):
            if i == (len(best_tour_order)-2):
                break 
            formatted_best_tour_output.append({
                "source":formatted_planet_list[i].name,
                "destination" : formatted_planet_list[i+1].name,
                "cost": node_edges[i]  
            })
        formatted_best_tour_output.append({
            "source": formatted_planet_list[-1].name,
            "destination": formatted_planet_list[0].name,
            "cost":node_edges[-1]
        })
        return (
            shipName,
            formatted_best_tour_output,
            tour_time,
            f"ship name 🛸: {shipName} Best Order 🗺️:: {[formatted_planet_list[i].name for i in best_tour_order]} optimal travel time ⌛: {tour_time}" )
        
    @staticmethod
    def format_planet_list_from_starting_node(planet_list:List[BasePlanetNode], starting_node:str)-> List[BasePlanetNode]:
        updatedList : List[BasePlanetNode]=[]
        for i in range(len(planet_list)):
            # placing the starting point at index 0 
            if planet_list[i].name == starting_node:
                alter = planet_list[i]
                planet_list.remove(alter)
                planet_list.insert(0,alter)  
                updatedList = planet_list
        return updatedList
    
    @staticmethod
    def construct_brute_force_algorithm(chosen_planet_list:List[BasePlanetNode],reliable_ships: pd.DataFrame, starting_node:str, global_ship_list:List[SpaceshipNode] ):
        results = []
        
        for i in reliable_ships.index:
            print(f"simulating :📈 {i}")
            print("processing ⏳...")
            
            results.append(
                TspUtils.tsp_brute_force(
                    formatted_planet_list=TspUtils.format_planet_list_from_starting_node(planet_list=chosen_planet_list,starting_node=starting_node),
                    shipName= i,
                    time_metrix= TspUtils.build_time_matrix(
                        formatted_planet_list=TspUtils.format_planet_list_from_starting_node(planet_list=chosen_planet_list,starting_node=starting_node),
                        spaceship=TspUtils.check_ship_is_valid(
                            ship_list=global_ship_list,
                            ship_name=i,),
                        )
                    )
            )
        print("############################################## 👨‍🚀!! TSP analysis result !!👨‍🚀####################################################TSP#########################")
        
        sorted_list = sorted(results, key=lambda x: x[2].total_seconds(), reverse=True)
            
        fastestShipRes = sorted_list[-1] 
        for  i in range(len(sorted_list)):
            print(f"\n{sorted_list[i][len(sorted_list[i])-1]}")
            print("\n")
        return fastestShipRes
                    
    @staticmethod
    def show_graph(bruit_force_result: Tuple[str, Dict, timedelta, str]):
        G = nx.DiGraph()    
        for objects in bruit_force_result[-3]:
            G.add_node(objects["source"])

   
        for obj in bruit_force_result[-3]:
        
            total_years = obj["cost"].total_seconds() / (24 * 3600 * 365)
            G.add_edge(u_of_edge=obj["source"], v_of_edge=obj['destination'], weight=total_years)

        
        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 10))  
        plt.title(f'fastest ship :: name {bruit_force_result[0]}')
        plt.text(0.5, 1.05, f"Making a Hamiltonian cycle in {bruit_force_result[-1]}", 
             ha='center', va='center', transform=plt.gca().transAxes, fontsize=12)
       
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=1000,  
            node_color='lightblue',
            font_size=10,
            font_weight='bold',
            edge_color='green',  
        )

        # Draw edge labels
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels={k: f"{v:.2f} years" for k, v in labels.items()},
            font_color='red',  
        )

      
        plt.show()
        


        
  
        

