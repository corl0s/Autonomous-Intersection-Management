# from typing import Dict, Tuple, List, Set

# class Intersection:
#     def __init__(self, width: int, height: int, n_blocks: int):
#         self.width = width
#         self.height = height
#         self.n_blocks = n_blocks
#         self.tiles: Dict[Tuple[int, int, int], int] = {}  # Map from (x, y, time) to vehicle ID
#         self.reservations: Dict[int, Set[Tuple[int, List[Tuple[int, int]]]]] = {}  # Map from vehicle ID to set of (time, tiles)
#         self.timeouts: Dict[int, int] = {}  # Map from vehicle ID to timeout
#         self.blocks = self.divide_into_blocks()
        
#     def divide_into_blocks(self):
#         block_width = self.width // self.n_blocks
#         block_height = self.height // self.n_blocks
#         blocks = []
#         for x in range(0, self.width, block_width):
#             for y in range(0, self.height, block_height):
#                 blocks.append((x, y, x + block_width, y + block_height))
#         return blocks

#     def request_reservation(self, vehicle_id: int, proposed_arrival_time: int, acceleration: bool) -> Tuple[bool, List[Tuple[int, int]]]:
#         tc = self.current_time
#         if self.timeouts.get(vehicle_id, -1) < tc:
#             return False, []

#         ta = proposed_arrival_time
#         self.timeouts[vehicle_id] = tc + min(5, (ta - tc) // 2)

#         for acceleration in [True, False]:
#             tile_times = []
#             t = ta
#             # Create temporary vehicle based on reservation parameters
#             # Here, we assume V is the temporary vehicle

#             while True:  # Replace with the actual condition for V being in the intersection
#                 S = self.get_tiles_occupied_by_V(V, t)  # Get tiles occupied by V and its static buffer at time t
#                 tile_times.append((t, S))

#                 for s in S:
#                     if s in self.get_edge_tiles():
#                         buf = self.get_edge_tile_buffer()
#                     else:
#                         buf = self.get_internal_tile_buffer()

#                     for i in range(-buf, buf + 1):
#                         if self.tiles.get((s[0], s[1], t + i)) is not None and self.tiles[(s[0], s[1], t + i)] != vehicle_id:
#                             if acceleration:
#                                 break
#                             else:
#                                 return False, []

#                 t += 1  # Increment time step
#                 # Move V according to physical model
#                 # Here, we assume there's a method move_V() to move V
#                 move_V()

#                 if acceleration:
#                     increase_V_velocity()

#                 break  # Remove this break in your actual implementation

#             # Handle change requests
#             if request_is_change:
#                 old_tile_times = self.reservations.get(vehicle_id, set())
#                 for (ti, Si) in old_tile_times:
#                     for s in Si:
#                         self.clear_reserved_status(s, ti)

#                 for (ti, Si) in tile_times:
#                     for s in Si:
#                         self.tiles[(s[0], s[1], ti)] = vehicle_id

#                 self.reservations[vehicle_id] = tile_times

#             return True, tile_times

#     # Implement other necessary methods


# from typing import Tuple, Dict, Set

# class IntersectionPolicy:
#     def __init__(self, n : int = 5):
#         self.n = n
#         self.reservation_grid: Dict[Tuple[int, int], Set[int]] = {}  # Map from (x, y) to vehicle IDs
#         self.timeouts: Dict[int, int] = {}  # Map from vehicle ID to timeout

    # def request_reservation(self, vehicle_id: int, x: int, y: int, start_time: int, end_time: int) -> bool:
    #     """
    #     Request a reservation for the vehicle to occupy the specified tiles from start_time to end_time.
    #     Returns True if the reservation is accepted, False otherwise.
    #     """
        
    #     intersection_position = (int(x), int(y))
    #     if self.timeouts.get(vehicle_id, 0) > start_time:
    #         # Vehicle already has a reservation that has not expired
    #         return False

    #     for t in range(start_time, end_time + 1):
    #         if self.reservation_grid.get(intersection_position) and t in self.reservation_grid[intersection_position]:
    #             # Tile already reserved by another vehicle at this time
    #             return False

    #     # Reserve tiles for the vehicle
    #     for t in range(start_time, end_time + 1):
    #         if (x, y) not in self.reservation_grid:
    #             self.reservation_grid[(x, y)] = set()
    #         self.reservation_grid[(x, y)].add(t)

    #     # Set timeout for the reservation
    #     self.timeouts[vehicle_id] = end_time

    #     return True
    
# from typing import Dict, Set, Tuple

# class IntersectionPolicy:
#     def __init__(self, n: int = 10, car_length: int = 100, car_width: int = 50):
#         self.n = n
#         self.car_length = car_length  # Length of the cars
#         self.car_width = car_width
#         self.tile_size = 200 // n  # Assuming the intersection is a square of size 1000x1000
#         self.reservation_grid: Dict[Tuple[int, int], Set[int]] = {}  # Map from (x, y) to vehicle IDs
#         self.timeouts: Dict[int, int] = {}  # Map from vehicle ID to timeout
#         self.width = 200
#         self.height = 200
        
        
#     def divide_into_blocks(self):
#         block_width = self.width // self.n
#         block_height = self.height // self.n
#         blocks = []
#         for x in range(0, self.width, block_width):
#             for y in range(0, self.height, block_height):
#                 blocks.append((x, y, x + block_width, y + block_height))
#         return blocks

#     def request_reservation(self, vehicle_id: int, x: int, y: int, start_time: int, end_time: int) -> bool:
#         """
#         Request a reservation for the vehicle to occupy the specified tiles from start_time to end_time.
#         Returns True if the reservation is accepted, False otherwise.
#         """
#         blocks = self.divide_into_blocks()
#         # print(blocks)
#         # exit()
#         # Simulate the trajectory of the vehicle and check reservation grids at each time step
#         for t in range(start_time, end_time + 1):
#             if self.timeouts.get(vehicle_id, 0) > t:
#                 # Vehicle already has a reservation that has not expired
#                 return False

#             # Reserve grids for the vehicle
#             for tile_x in range(start_tile_x, end_tile_x + 1):
#                 for tile_y in range(start_tile_y, end_tile_y + 1):
#                     if (tile_x, tile_y) in self.reservation_grid and t in self.reservation_grid[(tile_x, tile_y)]:
#                         # Grid already reserved by another vehicle at this time
#                         return False
#                     if (tile_x, tile_y) not in self.reservation_grid:
#                         self.reservation_grid[(tile_x, tile_y)] = set()
#                     self.reservation_grid[(tile_x, tile_y)].add(t)
#         # print(self.reservation_grid)
#         # exit()
#         # Set timeout for the reservation
#         self.timeouts[vehicle_id] = end_time

#         return True


#     def unreserve_vehicle(self, vehicle_id: int):
#         """
#         Remove the reservation for the specified vehicle.
#         """
#         if vehicle_id in self.timeouts:
#             del self.timeouts[vehicle_id]

#         # Remove vehicle from reservation_grid
#         for position, vehicles in list(self.reservation_grid.items()):
#             if vehicle_id in vehicles:
#                 vehicles.remove(vehicle_id)
#                 if not vehicles:
#                     del self.reservation_grid[position]
#                 break

#     def simulate_trajectory(self, vehicle_id: int, x: int, y: int, start_time: int, end_time: int) -> bool:
#         """
#         Simulate the trajectory of the vehicle and check if the requested tiles are available for reservation.
#         Returns True if the trajectory is clear, False otherwise.
#         """
#         for t in range(start_time, end_time + 1):
#             if self.reservation_grid.get((x, y)) and t in self.reservation_grid[(x, y)]:
#                 # Tile already reserved by another vehicle at this time
#                 return False

#         return True

# # Example Usage
# n = 5  # Granularity of the policy
# intersection = IntersectionPolicy(n)

# # Request a reservation
# vehicle_id = 1
# x = 2
# y = 3
# start_time = 5
# end_time = 10
# if intersection.request_reservation(vehicle_id, x, y, start_time, end_time):
#     print("Reservation accepted.")
# else:
#     print("Reservation rejected.")

# # Simulate a trajectory
# if intersection.simulate_trajectory(vehicle_id, x, y, start_time, end_time):
#     print("Trajectory clear.")
# else:
#     print("Trajectory blocked.")


from typing import Dict, Set, Tuple
import pygame as pg
from car import Car

class IntersectionPolicy:
    def __init__(self, n: int = 10):
        self.n = n
        self.tile_size = 200 // n  # Assuming the intersection is a square of size 200x200
        self.reservation_grid: Dict[Tuple[int, int, int], int] = {}  # Map from (block_x, block_y, time) to vehicle ID
        self.timeouts: Dict[int, int] = {}  # Map from vehicle ID to timeout
        self.width = 200
        self.height = 200

    def divide_into_blocks(self):
        block_width = self.width // self.n
        block_height = self.height // self.n
        blocks = []
        for x in range(620, 620 + self.width, block_width):
            for y in range(300, 300 + self.height, block_height):
                blocks.append((x, y, x + block_width, y + block_height))
        return blocks

    # def request_reservation(self, vehicle_id: int, x: int, y: int, start_time: int, end_time: int) -> bool:
    #     """
    #     Request a reservation for the vehicle to occupy the specified tiles from start_time to end_time.
    #     Returns True if the reservation is accepted, False otherwise.
    #     """
    #     blocks = self.divide_into_blocks()

    #     # start_x, start_y = None, None 
    #     # # Check if the vehicle already has a reservation for the same blocks and time range
    #     # if all((start_x, start_y) in self.reservation_grid and t in self.reservation_grid[(start_x, start_y)] for block in blocks for t in range(start_time, end_time + 1)):
    #     #     return True

    #     # Check if the car's coordinates fall within any block and reserve the block
    #     for block in blocks:
    #         start_x, start_y, end_x, end_y = block
    #         if start_x <= x < end_x and start_y <= y < end_y:
    #             for t in range(start_time, end_time + 1):
    #                 if self.timeouts.get(vehicle_id, 0) > t:
    #                     # Vehicle already has a reservation that has not expired
    #                     return False

    #                 if (start_x, start_y) in self.reservation_grid and t in self.reservation_grid[(start_x, start_y)]:
    #                     # Tile already reserved by another vehicle at this time
    #                     if vehicle_id in self.reservation_grid[(start_x, start_y)][t]:
    #                         return True
    #                     else:
    #                         return False

    #                 # Reserve the block for the vehicle
    #                 if (start_x, start_y) not in self.reservation_grid:
    #                     self.reservation_grid[(start_x, start_y)] = set()
    #                 self.reservation_grid[(start_x, start_y)].add(t)

    #             # Set timeout for the reservation
    #             self.timeouts[vehicle_id] = end_time
    #             # print(re)
    #             return True

    #     return False

    def request_reservation(self, vehicle_id: int, x: int, y: int) -> bool:
        """
        Request a reservation for the vehicle to occupy the specified block.
        Returns True if the reservation is accepted, False otherwise.
        """
        blocks = self.divide_into_blocks()

        for block in blocks:
            start_x, start_y, end_x, end_y = block
            if start_x <= x < end_x or start_y <= y < end_y:
                if (start_x, start_y) in self.reservation_grid:
                    if vehicle_id in self.reservation_grid[(start_x, start_y)]:
                        # Block already reserved by the same vehicle
                        return True
                    else:
                        # Block already reserved by other vehicles
                        return False
                # Reserve the block for the vehicle
                if (start_x, start_y) not in self.reservation_grid:
                    self.reservation_grid[(start_x, start_y)] = set()
                self.reservation_grid[(start_x, start_y)].add(vehicle_id)
                return True

        return False

    
    def get_predicted_position(position, velocity, deltat, start_t, end_t):
        """
        Returns a list of the future positions of a car given the time interval and velocity
        """
        positions = dict()
    
        for deltat in range(0, int(end_t - start_t), deltat):
            positions[deltat] = pg.math.Vector2(position + ((start_t + deltat) * velocity))
        return positions
    
    
    # def unreserve_vehicle(self, vehicle_id: int):
    #     """
    #     Remove the reservation for the specified vehicle.
    #     """
    #     if vehicle_id in self.timeouts:
    #         del self.timeouts[vehicle_id]

    #     # Remove vehicle from reservation_grid
    #     for position, vehicles in list(self.reservation_grid.items()):
    #         if vehicle_id in vehicles:
    #             vehicles.remove(vehicle_id)
    #             if not vehicles:
    #                 del self.reservation_grid[position]
    #             break
    
    def unreserve_vehicle(self, vehicle_id: int):
        """
        Remove the reservation for the specified vehicle.
        """
        if vehicle_id in self.timeouts:
            del self.timeouts[vehicle_id]

        # Remove vehicle from reservation_grid
        for position, vehicles in list(self.reservation_grid.items()):
            if vehicle_id in vehicles:
                vehicles.remove(vehicle_id)
                if not vehicles:
                    del self.reservation_grid[position]
                break

