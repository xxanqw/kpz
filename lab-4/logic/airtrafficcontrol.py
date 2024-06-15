import uuid

class CommandCentre:
    def __init__(self):
        self._runways = []
        self._aircrafts = []

    def add_runway(self, runway):
        self._runways.append(runway)

    def add_aircraft(self, aircraft):
        self._aircrafts.append(aircraft)

    def request_landing(self, aircraft):
        for runway in self._runways:
            if runway.is_busy_with_aircraft is None:
                runway.is_busy_with_aircraft = aircraft
                runway.high_light_red()
                print(f"Aircraft {aircraft.name} has landed on runway {runway.id}.")
                return
        print("Could not land, all runways are busy.")

    def request_takeoff(self, aircraft):
        for runway in self._runways:
            if runway.is_busy_with_aircraft == aircraft:
                runway.is_busy_with_aircraft = None
                runway.high_light_green()
                print(f"Aircraft {aircraft.name} has took off from runway {runway.id}.")
                return
        print("Could not take off, aircraft is not on any runway.")

class Aircraft:
    def __init__(self, name, size, command_centre):
        self.name = name
        self.command_centre = command_centre
        self.is_taking_off = False

    def land(self):
        self.command_centre.request_landing(self)

    def take_off(self):
        self.command_centre.request_takeoff(self)

class Runway:
    def __init__(self, command_centre):
        self.id = uuid.uuid4()
        self.is_busy_with_aircraft = None
        self.command_centre = command_centre

    def high_light_red(self):
        print(f"Runway {self.id} is busy!")

    def high_light_green(self):
        print(f"Runway {self.id} is free!")
