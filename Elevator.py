class Elevator:
    """Class representing an elevator in a building."""

    def __init__(self, current_floor:int=0, speed:int=10):
        """Initialization of variables"""
        self.current_floor = current_floor
        self.speed = speed

    def move_floors(self, current_floor:int = None, target_floors:list = [], verbose:bool = False):
        """Assuming no repeat floors in the target_floors list, and that the elevator moves in the order of the target_floors list.
        Inputs: current_floor (optional): the floor the elevator is currently on. If not provided, it will use the elevator's current_floor attribute.
                target_floors: a list of floors the elevator needs to move to in order.
                verbose: whether to print the details of each move.
        Output: time (int) taken to move through all the target floors, and a list of visited floors ([int]) in the order they were visited."""

        time = 0
        
        if current_floor is not None:
            self.current_floor = current_floor

        visited_floors = [self.current_floor]

        if target_floors:
            for floor in target_floors:
                #Calculate time taken to move to the next floor and update the current floor
                time += abs(self.current_floor - floor) * self.speed
                self.current_floor = floor

                if verbose:
                    print(f"Moved to floor {floor}. Time taken: {time} seconds.")
                #Add to the list of visited floors
                visited_floors.append(floor)
        return time, visited_floors
        
    def call(self, floor:int, verbose:bool = False):
        """Simulates calling the elevator to a specific floor. It calculates the time taken to move to that floor and updates the current floor.
        Input: floor (int) the floor to which the elevator is called. Verbose (bool) whether to print the details of the call.
        Output: time (int) taken to move to the called floor."""

        time = abs(self.current_floor - floor) * self.speed
        self.current_floor = floor
        if verbose:
            print(f"Elevator called to floor {floor}. Time taken: {time} seconds.")
        return time
    

    #Getters and Setters
    def get_current_floor(self):
        return self.current_floor
    def get_speed(self):
        return self.speed
    def set_current_floor(self, new_floor:int):
        self.current_floor = new_floor
        print(f"Current floor set to {self.current_floor}.")
    def set_speed(self, new_speed:int):
        self.speed = new_speed
        print(f"Speed set to {self.speed} units per second.")

if __name__ == "__main__":
    # Basic Testing
    start_floor = 12
    speed = 10
    floors = [2,9,1,32]

    elevator = Elevator(start_floor, speed)
    print(f"Initial floor: {elevator.get_current_floor()}")
    print(f"Initial speed: {elevator.get_speed()} units per second.")

    print(elevator.move_floors(target_floors=floors))
    
    print("\n")
    #Extra functionality testing
    elevator.set_current_floor(5)
    elevator.set_speed(15)
    
    print(f"Updated floor: {elevator.get_current_floor()}")
    print(f"Updated speed: {elevator.get_speed()} units per second.")
    
    time, visited_floors = elevator.move_floors(target_floors=[2,9,1,32], verbose=True)
    print(f"Time taken: {time} seconds")
    print(f"Visited floors: {visited_floors}")