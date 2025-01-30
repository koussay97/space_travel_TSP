from typing import Dict, List
from node import *
from spaceship_node import SpaceshipNode


class Scenarios(ABC): 
    """_summary_
    this class constructs the scenarios required for the comparaison,
    including planet data and spaceship data

    """
    @staticmethod
    def super_boosters_realistic() -> Dict[str,float]:
        """
        A more realistic set of booster powers for escaping planetary atmospheres.
        Returns:
            dict: A dictionary of booster power (in Newtons) for each planet.
            max 5000
        """
        return {
            "Sun": 0,          # Extreme gravity and heat require significant boost
            "Mercury": 0,       # Low gravity but proximity to the Sun requires moderate boost
            "Earth": 3000,        # Standard booster for Earth's gravity and atmosphere
            "Mars": 3500,         # Thin atmosphere but requires extra thrust for interplanetary travel
            "Jupiter": 2500,      # High gravity but thick atmosphere reduces booster requirements
            "Saturn": 2600,        # Lower gravity and thick atmosphere require minimal boost
            "Uranus": 4000,       # Extreme distance and cold require powerful boosters
            "Neptune": 5000,      # Farthest planet, requiring significant boosters
            "Pluto": 0,        # Low gravity but extreme distance requires moderate boost
            "Venus": 4000,        # Thick atmosphere and high gravity require standard boost
        }
        
        
    @staticmethod
    def super_boosters_extreme() -> Dict[str,float]:
        """
        An extreme set of booster powers for escaping planetary atmospheres.
        Returns:
            dict: A dictionary of booster power (in Newtons) for each planet.
            max 10,000
        """
        return {
            "Sun": 2000,         # Extreme gravity and heat require massive boosters
            "Mercury": 0,      # Low gravity but proximity to the Sun requires significant boost
            "Earth": 6700,       # Overpowered booster for Earth's gravity and atmosphere
            "Mars": 4600,         # Thin atmosphere but requires extra thrust for interplanetary travel
            "Jupiter": 7000,      # High gravity but thick atmosphere reduces booster requirements
            "Saturn": 6800,       # Lower gravity and thick atmosphere require moderate boost
            "Uranus": 5700,      # Extreme distance and cold require extremely powerful boosters
            "Neptune": 8900,     # Farthest planet, requiring the most powerful boosters
            "Pluto": 500,        # Low gravity but extreme distance requires significant boost
            "Venus": 8000,       # Thick atmosphere and high gravity require overpowered boost
        }
    @staticmethod
    def super_boosters_minimal() -> Dict[str,float]:
        """
        A minimal set of booster powers for escaping planetary atmospheres.
        Returns:
            dict: A dictionary of booster power (in Newtons) for each planet.
        max 3,000
        """
        return {
            "Sun": 1300,          # Extreme gravity and heat require minimal boost (very challenging)
            "Mercury": 500,       # Low gravity but proximity to the Sun requires minimal boost
            "Earth": 1800,         # Minimal booster for Earth's gravity and atmosphere
            "Mars": 1900,          # Thin atmosphere but requires minimal extra thrust
            "Jupiter": 2000,       # High gravity but thick atmosphere reduces booster requirements
            "Saturn": 1000,        # Lower gravity and thick atmosphere require minimal boost
            "Uranus": 2800,       # Extreme distance and cold require moderate boosters
            "Neptune": 2300,      # Farthest planet, requiring significant boosters
            "Pluto": 800,         # Low gravity but extreme distance requires minimal boost
            "Venus": 3000,         # Thick atmosphere and high gravity require minimal boost
        }
   
    @staticmethod
    def spaceshipData() -> List[Dict[str, Dict[str, float]]]:
        return [
            {
                'SpaceX Merlin 1D (Falcon 9)': {
                    'Mass': 470,
                    'Thrust': 845000,
                    'Air_Friction': {
                        "Sun":0,
                        "Mercury": 0,
                        "Venus": 225775,
                        "Earth": 658.6,
                        "Mars": 10.75,
                        "Jupiter": 86,
                        "Saturn": 102.1,
                        "Uranus": 225.8,
                        "Neptune": 241.9,
                        "Pluto": 0
                    }
                }
            },
            {
                'SpaceX Raptor 2 (Starship)': {
                    'Mass': 1600,
                    'Thrust': 2300000,
                    'Air_Friction': {
                        "Sun":0,
                        "Mercury": 0,
                        "Venus": 1336500,
                        "Earth": 3897.5,
                        "Mars": 63.62,
                        "Jupiter": 509.0,
                        "Saturn": 604.4,
                        "Uranus": 1336.5,
                        "Neptune": 1431.0,
                        "Pluto": 0
                    }
                }
            },
            {
                'Blue Origin BE-4 (New Glenn)': {
                    'Mass': 5500,
                    'Thrust': 2400000,
                    'Air_Friction': {
                        "Sun":0,
                        "Mercury": 0,
                        "Venus": 1336500,
                        "Earth": 3897.5,
                        "Mars": 63.62,
                        "Jupiter": 509.0,
                        "Saturn": 604.4,
                        "Uranus": 1336.5,
                        "Neptune": 1431.0,
                        "Pluto": 0
                    }
                }
            },
            {
                'RS-25 (Space Shuttle Main Engine)': {
                    'Mass': 3500,
                    'Thrust': 2279000,
                    'Air_Friction': {
                        "Sun":0,
                        "Mercury": 0,
                        "Venus": 1336500,
                        "Earth": 3897.5,
                        "Mars": 63.62,
                        "Jupiter": 509.0,
                        "Saturn": 604.4,
                        "Uranus": 1336.5,
                        "Neptune": 1431.0,
                        "Pluto": 0
                    }
                }
            },
            {
                'RD-180 (Atlas V)': {
                    'Mass': 5480,
                    'Thrust': 4152000,
                    'Air_Friction': {
                        "Sun":0,
                        "Mercury": 0,
                        "Venus": 1336500,
                        "Earth": 3897.5,
                        "Mars": 63.62,
                        "Jupiter": 509.0,
                        "Saturn": 604.4,
                        "Uranus": 1336.5,
                        "Neptune": 1431.0,
                        "Pluto": 0
                    }
                }
            },
            {
                'F-1 (Saturn V)': {
                    'Mass': 8400,
                    'Thrust': 7740000,
                    'Air_Friction': {
                        "Sun":0,
                        "Mercury": 0,
                        "Venus": 1336500,
                        "Earth": 3897.5,
                        "Mars": 63.62,
                        "Jupiter": 509.0,
                        "Saturn": 604.4,
                        "Uranus": 1336.5,
                        "Neptune": 1431.0,
                        "Pluto": 0
                    }
                }
            },
            {
                'RL-10 (Upper Stage Engine)': {
                    'Mass': 168,
                    'Thrust': 110000,
                    'Air_Friction': {
                        "Sun":0,
                        "Mercury": 0,
                        "Venus": 225775,
                        "Earth": 658.6,
                        "Mars": 10.75,
                        "Jupiter": 86,
                        "Saturn": 102.1,
                        "Uranus": 225.8,
                        "Neptune": 241.9,
                        "Pluto": 0
                    }
                }
            },
            {
                'Draco Thruster (SpaceX)': {
                    'Mass': 2,
                    'Thrust': 400,
                    'Air_Friction': {
                        "Sun":0,
                        "Mercury": 0,
                        "Venus": 2100,
                        "Earth": 6.125,
                        "Mars": 0.1,
                        "Jupiter": 0.8,
                        "Saturn": 0.95,
                        "Uranus": 2.1,
                        "Neptune": 2.25,
                        "Pluto": 0
                    }
                }
            },
            {
                'Millennium Falcon (Star Wars)': {
                    'Mass': 100000,
                    'Thrust': 3000000,
                    'Air_Friction': {
                        "Sun":0,
                        "Mercury": 0,
                        "Venus": 24900000,
                        "Earth": 43300,
                        "Mars": 706.86,
                        "Jupiter": 5655.0,
                        "Saturn": 6715.0,
                        "Uranus": 14850.0,
                        "Neptune": 15900.0,
                        "Pluto": 0
                    }
                }
            }
        ]
   
    @staticmethod
    def construct_planets_with_boosters(boosters: dict) -> List[BasePlanetNode]:
        """
        Constructs a list of planet nodes with the given booster values.
        
        Args:
            boosters (dict): A dictionary of booster power (in Newtons) for each planet.
        
        Returns:
            List[BasePlanetNode]: A list of planet nodes initialized with the corresponding booster values.
        """
        planets = []
        
        # Iterate through the boosters dictionary
        for planet_name, booster_value in boosters.items():
            if planet_name == "Sun":
                planets.append(SunNode(station_boost=booster_value))
            elif planet_name == "Mercury":
                planets.append(MercuryNode(station_boost=booster_value))
            elif planet_name == "Earth":
                planets.append(EarthNode(station_boost=booster_value))
            elif planet_name == "Mars":
                planets.append(MarsNode(station_boost=booster_value))
            elif planet_name == "Jupiter":
                planets.append(JupiterNode(station_boost=booster_value))
            elif planet_name == "Saturn":
                planets.append(SaturnNode(station_boost=booster_value))
            elif planet_name == "Uranus":
                planets.append(UranusNode(station_boost=booster_value))
            elif planet_name == "Neptune":
                planets.append(NeptuneNode(station_boost=booster_value))
            elif planet_name == "Pluto":
                planets.append(PlutoNode(station_boost=booster_value))
            elif planet_name == "Venus":
                planets.append(VenusNode(station_boost=booster_value))
            else:
                raise ValueError(f"Unknown planet: {planet_name}")
        
        return planets  
    
    
    @staticmethod
    def construct_spaceships(spaceshipData: List[Dict[str, Dict[str, float]]]) -> List[SpaceshipNode]:
        """
        Constructs a list of SpaceshipNode instances from the given spaceship data.
        
        Args:
            spaceshipData (List[dict]): A list of dictionaries containing spaceship data.
        
        Returns:
            List[SpaceshipNode]: A list of SpaceshipNode instances.
        """
        spaceships = []
        
        # Iterate through the spaceship data
        for spaceship_dict in spaceshipData:
            for name, attributes in spaceship_dict.items():
                # Extract mass and thrust from the attributes
                mass = attributes.get("Mass")
                thrust = attributes.get("Thrust")
                air_friction_on_each_planet= attributes.get("Air_Friction")
                # Create a SpaceshipNode instance and add it to the list
                spaceship = SpaceshipNode(name=name, mass=mass, engine_thrust_power=thrust,air_friction_on_each_planet=air_friction_on_each_planet)
                spaceships.append(spaceship)
        
        return spaceships
