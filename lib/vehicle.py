class Vehicle:
    
    def __init__(self, wheel_size, wheel_number) -> None:
        self.wheel_size, self.wheel_number = wheel_size, wheel_number
        
        
    def go(self):
        return "vrrrrrrrooom!"
    
    def fill_up_tank(self):
        return "filling up!"
