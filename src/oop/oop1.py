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
  def __init__(self):
    #   GroundVehicle is a subclass of Vehicle
    class GroundVehicle(Vehicle):
      def __init__(self):
        pass
        #   Car is a subclass of Vehicle and GroundVehicle
        class Car(GroundVehicle):
          def __init__(self):
            pass
        #   Motorcycle is a subclass of Vehicle and GroundVehicle
        class Motorcycle(GroundVehicle):
          def __init__(self):
            pass
    #   FlightVehicle is a subclass of Vehicle
    class FlightVehicle(Vehicle):
      def __init__(self):
        pass
        #   Starship is a subclass of FlightVehicle and Vehicle
        class Starship(FlightVehicle):
          def __init__(self):
            pass
        #   Airplane is a subclass of FlightVehicle and Vehicle
        class Airplane(FlightVehicle):
          def __init__(self):
            pass