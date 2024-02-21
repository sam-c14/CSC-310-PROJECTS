class Vehicle:
    def __init__(self, vehicle_id, initial_position):
        self.vehicle_id = vehicle_id
        self.position = initial_position

    def update_position(self, new_position):
        self.position = new_position


class FleetTracker:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.vehicle_id] = vehicle

    def update_vehicle_position(self, vehicle_id, new_position):
        if vehicle_id in self.vehicles:
            self.vehicles[vehicle_id].update_position(new_position)
        else:
            print(f"Vehicle with ID {vehicle_id} not found.")

    def get_vehicle_position(self, vehicle_id):
        if vehicle_id in self.vehicles:
            return self.vehicles[vehicle_id].position
        else:
            print(f"Vehicle with ID {vehicle_id} not found.")


# Example usage:
fleet_tracker = FleetTracker()

# Adding vehicles
vehicle1 = Vehicle(1, (0, 0))
vehicle2 = Vehicle(2, (10, 5))
fleet_tracker.add_vehicle(vehicle1)
fleet_tracker.add_vehicle(vehicle2)

# Updating and retrieving positions
fleet_tracker.update_vehicle_position(1, (2, 3))
print(f"Vehicle 1 position: {fleet_tracker.get_vehicle_position(1)}")

fleet_tracker.update_vehicle_position(2, (15, 8))
print(f"Vehicle 2 position: {fleet_tracker.get_vehicle_position(2)}")
