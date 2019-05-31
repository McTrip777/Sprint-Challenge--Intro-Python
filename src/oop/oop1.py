# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# Vehicle is the base class of all of these subclasses
class Vehicle:
    pass
#   GroundVehicle is a childclass of Vehicle
class GroundVehicle(Vehicle):
    pass
#   Car is a grandchildclass of Vehicle and childclass of GroundVehicle
class Car(GroundVehicle):
    pass
#   Motorcycle is a grandchildclass of Vehicle and childclass of GroundVehicle
class Motorcycle(GroundVehicle):
    pass
#   FlightVehicle is a childclass of Vehicle
class FlightVehicle(Vehicle):
    pass
  #   Starship is a childclass of FlightVehicle and grandchildclass of Vehicle
class Starship(FlightVehicle):
    pass
#   Airplane is a childclass of FlightVehicle and grandchildclass of Vehicle
class Airplane(FlightVehicle):
    pass