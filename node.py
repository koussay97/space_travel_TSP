from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List, Optional, TypeVar


from validator_decorators import is_float, is_string

T = TypeVar('T', bound='BasePlanetNode')

@dataclass(frozen=True)
class BasePlanetNode(ABC):
    _name: str = field(default=None, init=False)
    """
    Planet name
    """
    
    _surface_gravety_g: float = field(default=None, init=False)
    """
    Surface gravity relative to each planet, for example: Earth g = 9.81
    """
    
    _distance_from_the_sun: float = field(default=None, init=False)
    """
    The distance separating the planet from the Sun in million km
    """
    
    _atmosphere_altitude: float = field(default=None, init=False)
    """
    The distance that the rocket needs to traverse so that the air friction force becomes negligible
    """
    
    _station_boost_for_thrust_power_launch: float = field(default=0.0, init=False)
    """
    Each planet has a preinstalled thrust station that boosts the spaceship after launch.
    The boost power fades when the spaceship is out of the atmosphere, meaning the boost power will be equal to 0 N.
    """
    @staticmethod
    @is_string
    def __validate_planet_name(value):
        return value
    @staticmethod
    @is_float
    def __validate_surface_gravety_g( value):
        return value
 
    @staticmethod
    @is_float
    def __validate_distance_from_the_sun(value):
        return value
    @staticmethod
    @is_float
    def __validate_atmosphere_altitude(value):
        return value
    @staticmethod
    @is_float
    def __validate_station_boost_for_thrust_power_launch(value):
        return value
    
    @classmethod
    def factory_child_constructor(
        cls: T, 
        *args, **kwargs,
    ) -> T:
        try:
            name = kwargs.get('name', args[0] if len(args) > 0 else None)
            station_boost_for_thrust_power_launch = kwargs.get('station_boost_for_thrust_power_launch', args[1] if len(args) > 1 else None)
            atmosphere_altitude = kwargs.get('atmosphere_altitude', args[2] if len(args) > 2 else None)
            distance_from_the_sun = kwargs.get('distance_from_the_sun', args[3] if len(args) > 3 else None)
            surface_gravety_g = kwargs.get('surface_gravety_g', args[4] if len(args) > 4 else None)
           
        
            new_instance = cls.__new__(cls)
            if name is not None:
                valid_name=new_instance.__validate_planet_name(value=name)
            if station_boost_for_thrust_power_launch is not None:
                valid_station_boost_for_thrust_power_launch= new_instance.__validate_station_boost_for_thrust_power_launch(value=station_boost_for_thrust_power_launch)               
            if atmosphere_altitude is not None:
                valid_atmosphere_altitude=new_instance.__validate_atmosphere_altitude(value=atmosphere_altitude)
            if distance_from_the_sun is not None:
                valid_distance_from_the_sun= new_instance.__validate_distance_from_the_sun(value=distance_from_the_sun) 
            if surface_gravety_g is not None:
                valid_surface_gravety_g=new_instance.__validate_surface_gravety_g(value=surface_gravety_g)
         
            
            object.__setattr__(new_instance, '_name', valid_name)
            object.__setattr__(new_instance, '_surface_gravety_g', valid_surface_gravety_g)    
            object.__setattr__(new_instance, '_station_boost_for_thrust_power_launch', valid_station_boost_for_thrust_power_launch)

            object.__setattr__(new_instance, '_distance_from_the_sun', valid_distance_from_the_sun)
            object.__setattr__(new_instance, '_atmosphere_altitude', valid_atmosphere_altitude)        
            return new_instance
        except TypeError as e:
            print(e)

    def copy_with(
        self,
        name: Optional[str] = None,
        station_boost_for_thrust_power_launch: Optional[float] = None,
        atmosphere_altitude: Optional[float] = None,
        distance_from_the_sun: Optional[float] = None,
        surface_gravety_g: Optional[float] = None,

    ):
        new_instance = self.__new__(self.__class__)
        try:
            if name is not None:
                self.__validate_planet_name(value=name)
                object.__setattr__( new_instance, '_name', name)
            if station_boost_for_thrust_power_launch is not None:
                self.__validate_station_boost_for_thrust_power_launch(value=station_boost_for_thrust_power_launch)
                object.__setattr__( new_instance, '_station_boost_for_thrust_power_launch', station_boost_for_thrust_power_launch)
            else :
                object.__setattr__( new_instance, '_station_boost_for_thrust_power_launch', self.station_boost_for_thrust_power_launch)
          
            if atmosphere_altitude is not None:
                self.__validate_atmosphere_altitude(value=atmosphere_altitude)
                object.__setattr__( new_instance, '_atmosphere_altitude', atmosphere_altitude)
            else : 
                object.__setattr__( new_instance, '_atmosphere_altitude', self.atmosphere_altitude)
           
            if distance_from_the_sun is not None:
                self.__validate_distance_from_the_sun(value=distance_from_the_sun)
                object.__setattr__( new_instance, '_distance_from_the_sun', distance_from_the_sun)
            else:
                object.__setattr__( new_instance, '_distance_from_the_sun', self.distance_from_the_sun)
           
            if surface_gravety_g is not None:
                self.__validate_surface_gravety_g(value=surface_gravety_g)
                object.__setattr__( new_instance, '_surface_gravety_g', surface_gravety_g)
            else:
                object.__setattr__( new_instance, '_surface_gravety_g', self.surface_gravety_g)
           
            return new_instance
        except TypeError as e:
            print(e)
    
    def __hash__(self):
        return hash((
            self._name,
            self._station_boost_for_thrust_power_launch,
            self._atmosphere_altitude,
            self._distance_from_the_sun,
            self._surface_gravety_g,
       
        ))

    def __eq__(self, value: T):
        return (
            self._name == value._name
            and self._station_boost_for_thrust_power_launch == value._station_boost_for_thrust_power_launch
            and self._atmosphere_altitude == value._atmosphere_altitude
            and self._distance_from_the_sun == value._distance_from_the_sun
            and self._surface_gravety_g == value._surface_gravety_g
          
        )
    @staticmethod    
    def planets_to_dict(planets: List['BasePlanetNode']) -> List[Dict[str, any]]:
        """
        Converts a list of BasePlanetNode instances into a list of dictionaries using __dict__.
        
        Args:
            planets (List[BasePlanetNode]): A list of planet instances.
        
        Returns:
            List[Dict[str, any]]: A list of dictionaries, where each dictionary represents a planet.
        """
        return [planet.__dict__ for planet in planets]
        
    @property
    @abstractmethod
    def name(self):
        pass
    
    @property
    @abstractmethod
    def station_boost_for_thrust_power_launch(self):
        pass
    
    @property
    @abstractmethod
    def atmosphere_altitude(self):
        pass
        
    @property
    @abstractmethod
    def distance_from_the_sun(self):
        pass
    
    @property
    @abstractmethod
    def surface_gravety_g(self):
        pass
        
   
    
    def __str__(self):
        return f"""<'{self.__class__.__name__}' : name : {self.name},
                 station_boost_for_thrust_power_launch: {self._station_boost_for_thrust_power_launch}, 
                 atmosphere_altitude: {self._atmosphere_altitude},
                 distance_from_the_sun: {self._distance_from_the_sun},
                 surface_gravety_g: {self._surface_gravety_g},
                 >"""
    ########################### Calculation Methods 
    def calculate_interplanetary_distance(self, other_planet: T):
        """
        Calculate the interplanetary distance between this planet and another planet.
        """
        return abs(self.distance_from_the_sun - other_planet.distance_from_the_sun)


############################### PLANET EARTH ##########################################################
class EarthNode(BasePlanetNode):
    
    def __init__(self, station_boost: float):
        super().__init__()
        name = "Earth"
        station_boost_for_thrust_power_launch = station_boost
        atmosphere_altitude = 100  # in KM
        distance_from_the_sun = 149.6  # in Million KM
        surface_gravety_g = 9.81
      
        
        instance = self.factory_child_constructor(
            self,
            name="Earth",
            station_boost_for_thrust_power_launch=station_boost_for_thrust_power_launch,
            atmosphere_altitude=atmosphere_altitude,
            distance_from_the_sun=distance_from_the_sun,
            surface_gravety_g=surface_gravety_g,
          
        )
        self.__dict__.update(instance.__dict__)
              
    @property
    def name(self):
        return self._name
    
    @property
    def station_boost_for_thrust_power_launch(self):
        return self._station_boost_for_thrust_power_launch
    
    @property
    def atmosphere_altitude(self):
        return self._atmosphere_altitude
    
    @property
    def distance_from_the_sun(self):
        return self._distance_from_the_sun
    
    @property
    def surface_gravety_g(self):
        return self._surface_gravety_g

    @property
    def air_friction_force(self):
        return self._air_friction_force


########################## THE SUN ###########################################
class SunNode(BasePlanetNode):
    def __init__(self, station_boost: float):
        super().__init__()
        name = "Sun"
        station_boost_for_thrust_power_launch = station_boost
        atmosphere_altitude = 0  # Negligible in KM
        distance_from_the_sun = 0  # in Million KM
        surface_gravety_g = 274
     
        instance = self.factory_child_constructor(
            name=name,
            station_boost_for_thrust_power_launch=station_boost_for_thrust_power_launch,
            atmosphere_altitude=atmosphere_altitude,
            distance_from_the_sun=distance_from_the_sun,
            surface_gravety_g=surface_gravety_g,
          
        )
        self.__dict__.update(instance.__dict__)
        
    @property
    def name(self):
        return self._name
    
    @property
    def station_boost_for_thrust_power_launch(self):
        return self._station_boost_for_thrust_power_launch
    
    @property
    def atmosphere_altitude(self):
        return self._atmosphere_altitude
    
    @property
    def distance_from_the_sun(self):
        return self._distance_from_the_sun
    
    @property
    def surface_gravety_g(self):
        return self._surface_gravety_g



############################# Mercury #######################################
class MercuryNode(BasePlanetNode):
    def __init__(self, station_boost: float):
        super().__init__()
        name = "Mercury"
        station_boost_for_thrust_power_launch = station_boost
        atmosphere_altitude = 100  # in KM
        distance_from_the_sun = 57.9  # in Million KM
        surface_gravety_g = 3.7
      
        instance= self.factory_child_constructor(
            name=name,
            station_boost_for_thrust_power_launch=station_boost_for_thrust_power_launch,
            atmosphere_altitude=atmosphere_altitude,
            distance_from_the_sun=distance_from_the_sun,
            surface_gravety_g=surface_gravety_g,
           
        )
        self.__dict__.update(instance.__dict__)
        
    @property
    def name(self):
        return self._name
    
    @property
    def station_boost_for_thrust_power_launch(self):
        return self._station_boost_for_thrust_power_launch
    
    @property
    def atmosphere_altitude(self):
        return self._atmosphere_altitude
    
    @property
    def distance_from_the_sun(self):
        return self._distance_from_the_sun
    
    @property
    def surface_gravety_g(self):
        return self._surface_gravety_g



############################# Venus #######################################
class VenusNode(BasePlanetNode):
    def __init__(self, station_boost: float):
        super().__init__()
        name = "Venus"
        station_boost_for_thrust_power_launch = station_boost
        atmosphere_altitude = 250  # in KM
        distance_from_the_sun = 108.2  # in Million KM
        surface_gravety_g = 8.87
    
        instance= self.factory_child_constructor(
            name=name,
            station_boost_for_thrust_power_launch=station_boost_for_thrust_power_launch,
            atmosphere_altitude=atmosphere_altitude,
            distance_from_the_sun=distance_from_the_sun,
            surface_gravety_g=surface_gravety_g,
     
        )
        self.__dict__.update(instance.__dict__)
        
    @property
    def name(self):
        return self._name
    
    @property
    def station_boost_for_thrust_power_launch(self):
        return self._station_boost_for_thrust_power_launch
    
    @property
    def atmosphere_altitude(self):
        return self._atmosphere_altitude
    
    @property
    def distance_from_the_sun(self):
        return self._distance_from_the_sun
    
    @property
    def surface_gravety_g(self):
        return self._surface_gravety_g




############################# Mars #######################################
class MarsNode(BasePlanetNode):
    def __init__(self, station_boost: float):
        super().__init__()
        name = "Mars"
        station_boost_for_thrust_power_launch = station_boost
        atmosphere_altitude = 125  # in KM
        distance_from_the_sun = 227.9  # in Million KM
        surface_gravety_g = 3.71
  
        instance = self.factory_child_constructor(
            name=name,
            station_boost_for_thrust_power_launch=station_boost_for_thrust_power_launch,
            atmosphere_altitude=atmosphere_altitude,
            distance_from_the_sun=distance_from_the_sun,
            surface_gravety_g=surface_gravety_g,

        )
        self.__dict__.update(instance.__dict__)
        
    @property
    def name(self):
        return self._name
    
    @property
    def station_boost_for_thrust_power_launch(self):
        return self._station_boost_for_thrust_power_launch
    
    @property
    def atmosphere_altitude(self):
        return self._atmosphere_altitude
    
    @property
    def distance_from_the_sun(self):
        return self._distance_from_the_sun
    
    @property
    def surface_gravety_g(self):
        return self._surface_gravety_g



############################# Jupiter #######################################
class JupiterNode(BasePlanetNode):
    def __init__(self, station_boost: float):
        super().__init__()
        name = "Jupiter"
        station_boost_for_thrust_power_launch = station_boost
        atmosphere_altitude = 5000  # in KM
        distance_from_the_sun = 778.5  # in Million KM
        surface_gravety_g = 24.79
      
        instance=self.factory_child_constructor(
            name=name,
            station_boost_for_thrust_power_launch=station_boost_for_thrust_power_launch,
            atmosphere_altitude=atmosphere_altitude,
            distance_from_the_sun=distance_from_the_sun,
            surface_gravety_g=surface_gravety_g,

        )
        self.__dict__.update(instance.__dict__)
        
    @property
    def name(self):
        return self._name
    
    @property
    def station_boost_for_thrust_power_launch(self):
        return self._station_boost_for_thrust_power_launch
    
    @property
    def atmosphere_altitude(self):
        return self._atmosphere_altitude
    
    @property
    def distance_from_the_sun(self):
        return self._distance_from_the_sun
    
    @property
    def surface_gravety_g(self):
        return self._surface_gravety_g




############################# Saturn #######################################
class SaturnNode(BasePlanetNode):
    def __init__(self, station_boost: float):
        super().__init__()
        name = "Saturn"
        station_boost_for_thrust_power_launch = station_boost
        atmosphere_altitude = 4000  # in KM
        distance_from_the_sun = 1434  # in Million KM
        surface_gravety_g = 10.44
      
        instance = self.factory_child_constructor(
            name=name,
            station_boost_for_thrust_power_launch=station_boost_for_thrust_power_launch,
            atmosphere_altitude=atmosphere_altitude,
            distance_from_the_sun=distance_from_the_sun,
            surface_gravety_g=surface_gravety_g,
   
        )
        self.__dict__.update(instance.__dict__)
        
    @property
    def name(self):
        return self._name
    
    @property
    def station_boost_for_thrust_power_launch(self):
        return self._station_boost_for_thrust_power_launch
    
    @property
    def atmosphere_altitude(self):
        return self._atmosphere_altitude
    
    @property
    def distance_from_the_sun(self):
        return self._distance_from_the_sun
    
    @property
    def surface_gravety_g(self):
        return self._surface_gravety_g




############################# Uranus #######################################
class UranusNode(BasePlanetNode):
    def __init__(self, station_boost: float):
        super().__init__()
        name = "Uranus"
        station_boost_for_thrust_power_launch = station_boost
        atmosphere_altitude = 3000  # in KM
        distance_from_the_sun = 2871  # in Million KM
        surface_gravety_g = 8.87
   
        instance = self.factory_child_constructor(
            name=name,
            station_boost_for_thrust_power_launch=station_boost_for_thrust_power_launch,
            atmosphere_altitude=atmosphere_altitude,
            distance_from_the_sun=distance_from_the_sun,
            surface_gravety_g=surface_gravety_g,
         
        )
        self.__dict__.update(instance.__dict__)
        
    @property
    def name(self):
        return self._name
    
    @property
    def station_boost_for_thrust_power_launch(self):
        return self._station_boost_for_thrust_power_launch
    
    @property
    def atmosphere_altitude(self):
        return self._atmosphere_altitude
    
    @property
    def distance_from_the_sun(self):
        return self._distance_from_the_sun
    
    @property
    def surface_gravety_g(self):
        return self._surface_gravety_g




############################# Neptune #######################################
class NeptuneNode(BasePlanetNode):
    def __init__(self, station_boost: float):
        super().__init__()
        name = "Neptune"
        station_boost_for_thrust_power_launch = station_boost
        atmosphere_altitude = 3500  # in KM
        distance_from_the_sun = 4495  # in Million KM
        surface_gravety_g = 11.15
    
        instance = self.factory_child_constructor(
            name=name,
            station_boost_for_thrust_power_launch=station_boost_for_thrust_power_launch,
            atmosphere_altitude=atmosphere_altitude,
            distance_from_the_sun=distance_from_the_sun,
            surface_gravety_g=surface_gravety_g,
            
        )
        self.__dict__.update(instance.__dict__)
        
    @property
    def name(self):
        return self._name
    
    @property
    def station_boost_for_thrust_power_launch(self):
        return self._station_boost_for_thrust_power_launch
    
    @property
    def atmosphere_altitude(self):
        return self._atmosphere_altitude
    
    @property
    def distance_from_the_sun(self):
        return self._distance_from_the_sun
    
    @property
    def surface_gravety_g(self):
        return self._surface_gravety_g



############################## Pluto #######################################
class PlutoNode(BasePlanetNode):
    def __init__(self, station_boost: float):
        super().__init__()
        name = "Pluto"
        station_boost_for_thrust_power_launch = station_boost
        atmosphere_altitude = 50  # in KM
        distance_from_the_sun = 5906  # in Million KM
        surface_gravety_g = 0.62
       
        instance = self.factory_child_constructor(
            name=name,
            station_boost_for_thrust_power_launch=station_boost_for_thrust_power_launch,
            atmosphere_altitude=atmosphere_altitude,
            distance_from_the_sun=distance_from_the_sun,
            surface_gravety_g=surface_gravety_g,
        )
        self.__dict__.update(instance.__dict__)
        
    @property
    def name(self):
        return self._name
    
    @property
    def station_boost_for_thrust_power_launch(self):
        return self._station_boost_for_thrust_power_launch
    
    @property
    def atmosphere_altitude(self):
        return self._atmosphere_altitude
    
    @property
    def distance_from_the_sun(self):
        return self._distance_from_the_sun
    
    @property
    def surface_gravety_g(self):
        return self._surface_gravety_g
