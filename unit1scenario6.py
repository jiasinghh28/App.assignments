class Vehicle:
    def __init__(self, vehicle_number, brand, price, category):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price
        self.category = category

    def display(self):
        print("Vehicle Number:", self.vehicle_number)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Category:", self.category)
        print("------------------------")


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print("Vehicle added successfully!")

    def display_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles available.")
        else:
            print("\n--- All Vehicles ---")
            for vehicle in self.vehicles:
                vehicle.display()


# Create showroom object
showroom = Showroom()

# Add vehicles
vehicle1 = Vehicle("V001", "BMW", 5000000, "Luxury")
vehicle2 = Vehicle("V002", "Toyota", 1500000, "Economy")
vehicle3 = Vehicle("V003", "Mercedes", 6000000, "Luxury")

showroom.add_vehicle(vehicle1)
showroom.add_vehicle(vehicle2)
showroom.add_vehicle(vehicle3)

# Display all vehicles
showroom.display_all_vehicles()
