from dataclasses import dataclass, field
import datetime
import math
from typing import Dict, Optional

# Assuming these decorators are defined elsewhere
from custom_exception import MechanicalError
from node import BasePlanetNode
from validator_decorators import is_float, is_string,is_valid_dict_of_air_friction_forces

@dataclass
class SpaceshipNode:
    
    _air_friction_on_different_planets: Dict[str,(float|int)]=field(default_factory=None,init=False)
    """
    the air friction value on each planet,
    """
    _current_journey_time: datetime.timedelta = field(default_factory=datetime.timedelta)
    """
    the time spent by the spaceship so far
    """
    _name: str = field(init=False, default=None)
    """
    Spaceship name
    """
    
    _mass: float = field(init=False, default=None)
    """
    Spaceship weight in kilograms (kg)
    """
    
    _engine_thrust_power: float = field(init=False, default=None)
    """
    Engine thrust power in Newtons (N)
    """
    
    def __init__(
        self,
        name: Optional[str] = None,
        mass: Optional[float] = None,
        engine_thrust_power: Optional[float] = None,
        air_friction_on_each_planet: Optional[Dict[str,(float|int)]]=None
    ):
        """
        Initializes the spaceship with validated attributes.
        """
        # Create an empty instance
            # Initialize _current_journey_time to zero
        self._current_journey_time = datetime.timedelta()
        self._validate_and_set_attributes(name, mass, engine_thrust_power, air_friction=air_friction_on_each_planet)
    
    def _validate_and_set_attributes(
        self,
        name: Optional[str],
        mass: Optional[float],
        engine_thrust_power: Optional[float],
        air_friction: Optional[Dict[str,(float|int)]]
    ) -> None:
        """
        Validates and sets the attributes.
        """
        try:
            if air_friction is not None:
                self.__validate_air_friction_forces_dict(air_friction)
                object.__setattr__(self,'_air_friction_on_different_planets',air_friction)
            if name is not None:
                self.__validate_name(name)
                object.__setattr__(self, '_name', name)
            if mass is not None:
                self.__validate_mass(mass)
                object.__setattr__(self, '_mass', mass)
            if engine_thrust_power is not None:
                self.__validate_engine_thrust_power(engine_thrust_power)
                object.__setattr__(self, '_engine_thrust_power', engine_thrust_power)
        except Exception as e:
            print(f"Validation error: {e}")
        
    @staticmethod
    @is_string
    def __validate_name(value):
        """
        Validates the spaceship name.
        """
        pass

    @staticmethod
    @is_float
    def __validate_mass(value):
        """
        Validates the spaceship weight.
        """
        pass

    @staticmethod
    @is_float
    def __validate_engine_thrust_power(value):
        """
        Validates the engine thrust power.
        """
        pass
    
    @staticmethod
    @is_valid_dict_of_air_friction_forces
    def __validate_air_friction_forces_dict(value):
        """
        Validate the dictionary of air friction forces
        """
        pass
    
    def copy_with(
        self,
        name: Optional[str] = None,
        mass: Optional[float] = None,
        engine_thrust_power: Optional[float] = None,
        air_friction: Optional[Dict[str,(float|int)]]=None
    ) -> 'SpaceshipNode':
        """
        Creates a new instance with updated attributes.
        """
        # Create an empty instance
        new_instance = SpaceshipNode()
        # Validate and set attributes
        new_instance._validate_and_set_attributes(
            name if name is not None else self._name,
            mass if mass is not None else self._mass,
            engine_thrust_power if engine_thrust_power is not None else self._engine_thrust_power,
            air_friction if air_friction is not None else self._air_friction_on_different_planets,
        )
        return new_instance
    
    def __hash__(self):
        """
        Computes the hash value of the spaceship based on its attributes.
        """
        return hash((self._name, self._mass, self._engine_thrust_power))

    def __eq__(self, other: object) -> bool:
        """
        Compares two spaceship instances for equality.
        """
        if not isinstance(other, SpaceshipNode):
            return False
        return (
            self._name == other._name
            and self._mass == other._mass
            and self._engine_thrust_power == other._engine_thrust_power
        )
        
    @property
    def name(self) -> str:
        """
        Returns the spaceship name.
        """
        return self._name
    
    @property
    def air_friction_on_each_planet(self)->Dict[str,(float|int)]:
        """_summary_
        Returns approximate air friction for each planet  in the form  of a dict
        """
        return self._air_friction_on_different_planets
    
    @property
    def mass(self) -> float:
        """
        Returns the spaceship weight.
        """
        return self._mass  # Fixed: Use _mass instead of _weight
    
    @property
    def engine_thrust_power(self) -> float:
        """
        Returns the engine thrust power.
        """
        return self._engine_thrust_power
    
    @property
    def current_journey_time(self) -> datetime.timedelta:
        """
        Returns the time spent in the journey.
        """
        return self._current_journey_time
    
    def get_time_needed_to_cross_the_atmosphere_of_planet(self, planet: BasePlanetNode) -> datetime.timedelta:
        """
        Calculates the time needed for the spaceship to cross the atmosphere of a given planet,
        using the pre-calculated air friction force.

        Args:
            planet (BasePlanetNode): The planet whose atmosphere the spaceship is crossing.

        Returns:
            datetime.timedelta: The time needed to cross the atmosphere.
        """
        try:
            # Convert atmosphere altitude from kilometers to meters
            atmosphere_altitude_meters = planet.atmosphere_altitude * 1000

            # Calculate net force
            net_force = (
                planet.station_boost_for_thrust_power_launch +
                self._engine_thrust_power  # Thrust power
                - self.air_friction_on_each_planet[planet.name]  # Pre-calculated air friction force
                - self.get_space_ship_mass_on_planet(planet=planet)  # Gravitational force
            )

            # If net force is zero or negative, the spaceship cannot proceed
            if net_force <= 0:
                raise MechanicalError(f"The spaceship '{self.name}' cannot overcome the forces acting against it on planet {planet.name}. to  cross the atmosphere")

            # Calculate acceleration
            acceleration = net_force / self._mass

            # Calculate time using the kinematic equation: d = 0.5 * a * t^2 => t = sqrt(2d / a)
            time_seconds = math.sqrt((2 * atmosphere_altitude_meters) / acceleration)

            # Convert time to a timedelta object
            return datetime.timedelta(seconds=time_seconds)

        except MechanicalError as e:
            print(f"⚡⚡⚡Error crossing atmosphere: {e}")
            raise
            

    def get_space_ship_mass_on_planet(self, planet: BasePlanetNode) -> float:
        return self._mass * planet.surface_gravety_g
    
    def get_time_needed_to_land_on_the_planet_from_its_atmosphere(self, planet: BasePlanetNode) -> datetime.timedelta:
        """
        Calculates the time needed for the spaceship to land on the planet from its atmosphere,
        using the pre-calculated air friction force.

        Args:
            planet (BasePlanetNode): The planet on which the spaceship is landing.

        Returns:
            datetime.timedelta: The time needed to land.
        """
        try:
            # Convert atmosphere altitude from kilometers to meters
            atmosphere_altitude_meters = planet.atmosphere_altitude * 1000

            # Calculate net force
            net_force = (
                self._engine_thrust_power # Thrust power (slows down the descent)
                + self.air_friction_on_each_planet[planet.name]  # Air friction force (opposes motion)
                - self.get_space_ship_mass_on_planet(planet=planet)  # Gravitational force
            )

            # If net force is zero or negative, the spaceship cannot slow down sufficiently
            if net_force <= 0:
                raise MechanicalError(f"The spaceship {self.name} cannot slow down sufficiently to land safely. on planet {planet.name}")

            # Calculate acceleration (deceleration is negative acceleration)
            acceleration = net_force / self._mass

            # Calculate time using the kinematic equation: d = 0.5 * a * t^2 => t = sqrt(2d / |a|)
            time_seconds = math.sqrt((2 * atmosphere_altitude_meters) / abs(acceleration))

            # Convert time to a timedelta object
            return datetime.timedelta(seconds=time_seconds)

        except MechanicalError as e:
            print(f'🌍🌍🌍Landing Error : {e}')
            raise
          
        
    def calculate_the_time_needed_to_travel_between_two_planets(
        self, 
        planetA: BasePlanetNode,
        planetB: BasePlanetNode,
    ) -> datetime.timedelta:
        """
        Calculates the time needed to travel between two planets based on the actual distance,
        the spaceship's thrust power, and its mass. Assumes a straight-line trajectory with constant acceleration.

        Args:
            planetA (BasePlanetNode): The starting planet.
            planetB (BasePlanetNode): The destination planet.

        Returns:
            datetime.timedelta: The time needed to travel between the two planets.

        Raises:
            Exception: If the calculation fails.
        """
        try:
            # Get the distance between the two planets (in meters)
            distance_between_planets = abs(planetA.distance_from_the_sun - planetB.distance_from_the_sun) * 1e9  # Convert million km to meters

            # Calculate the acceleration of the spaceship (a = F / m)
            acceleration = self._engine_thrust_power / self._mass

            # Calculate the time required to travel the distance using the kinematic equation:
            # distance = 0.5 * a * t^2 => t = sqrt(2 * distance / a)
            time_seconds = math.sqrt((2 * distance_between_planets) / acceleration)

            # Convert time to a timedelta object
            
            return datetime.timedelta(seconds=time_seconds)

        except Exception as e:
            print(f"Error calculating travel time between planets: {e}")
            raise
    def calculate_total_journey_time_from_planetA_to_planetB(
        self,
        planetA: BasePlanetNode,
        planetB: BasePlanetNode,
    ) -> datetime.timedelta:
        """
        Calculates the total journey time from planetA to planetB, including:
        - Time to exit planetA's atmosphere.
        - Time to travel between the two planets.
        - Time to land on planetB.

        Args:
            planetA (BasePlanetNode): The starting planet.
            planetB (BasePlanetNode): The destination planet.

        Returns:
            datetime.timedelta: The total journey time.

        Raises:
            Exception: If any of the calculations fail.
        """
        try:
            # Time to exit planetA's atmosphere
            exit_time = self.get_time_needed_to_cross_the_atmosphere_of_planet(planetA)

            # Time to travel between the two planets
            travel_time = self.calculate_the_time_needed_to_travel_between_two_planets(planetA, planetB)

            # Time to land on planetB
            landing_time = self.get_time_needed_to_land_on_the_planet_from_its_atmosphere(planetB)

            # Total journey time
            total_time = exit_time + travel_time + landing_time

            # Update the current journey time
            self._current_journey_time += total_time
            return total_time

        except Exception as e:
            print(f"Error calculating total journey time: {e}")
            raise
           