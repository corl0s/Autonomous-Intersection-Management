####################################
# Created by Akash Pamal, Jack Blair, and Rahel Selemon
# HackTJ 2020 12/13/20
# MIT License
####################################
import pygame as pg
import random
import threading
import time

CAR_WIDTH = 150
CAR_HEIGHT = 80

class Directions():
    """
    Stores the Matricies for each cardinal direction
    Determines if two given directions are perpendicular or opposite
    """
    
    right = (1, 0)
    left = (-1, 0)
    up = (0, -1)
    down = (0, 1)
     
    directions = [up, down, left, right]
        
    def perpendicular(dir1, dir2):
        if dir1 == Directions.up or dir == Directions.down:
            return (dir2 == Directions.left or dir2 == Directions.right)
        elif dir1 == Directions.left or dir1 == Directions.right:
            return (dir2 == Directions.up or dir2 == Directions.down)
        else:
            return False
        
    def opposite(dir1, dir2):
        if dir1 == Directions.up:
            return dir2 == Directions.down
        elif dir1 == Directions.down:
            return dir2 == Directions.up
        elif dir1 == Directions.left:
            return dir2 == Directions.right
        elif dir1 == Directions.right:
            return dir2 == Directions.left

class AssetManager():
    """
    Reads the images into Pygame from the given directories
    Maintains a list of all the colors to be chosen from randomly
    """
    
    lblue = pg.image.load('./res/BlueCar.png')
    blue = pg.image.load('./res/BlueSudan.png')
    yellow = pg.image.load('./res/YellowTruck.png')
    brown = pg.image.load('./res/BrownCar.png')
    grey = pg.image.load('./res/GreyCar.png')
    red = pg.image.load('./res/RedCar.png')
    purple = pg.image.load('./res/PurpleCar.png')
    green = pg.image.load('./res/GreenCar.png')
    cars = [lblue, blue, yellow, brown, grey, red, purple, green]
    
class Car:
    def __init__(self, id, screen, lane, initial_velocity = 0.05, initial_acceleration = 0.001):
        """
        Stores all the information about a certain vehicle in the scene
        """
        # threading.Thread.__init__(self)
        self.id = id
        # Physics
        self.direction = random.choice(Directions.directions) 
        self.position = self.gen_pos_lane(lane, self.direction) #Generates lane position from a direction and lane number)
        self.velocity = pg.math.Vector2(self.direction[0] * initial_velocity, self.direction[1] * initial_velocity)
        self.acceleration = pg.math.Vector2(self.direction[0] * initial_acceleration, self.direction[1] *initial_acceleration)
        
        # Graphics
        image = random.choice(AssetManager.cars)
        self.image = image.convert_alpha() # This gets the clear image backgrounds
        self.image = self.rotate_image(screen, self.image)
        self.length = self.image.get_size()[0]
        self.width = self.image.get_size()[1]
        self.image = pg.transform.scale(self.image, (int(self.length/2), int(self.width/2)))
        self.rect = pg.Rect(self.position.x, self.position.y, CAR_WIDTH, CAR_HEIGHT)
        # Characteristics
        self.completed_path = False
        self.completed_intersection = False
        self.lane = lane
        self.success = True
        self.collisions = 0
        
        self.last_update_time = time.perf_counter()
        self.creation_time = 0
        self.removal_times = 0
        
    def check_collision(self, other_car):
        # self.rect = pg.Rect(self.position.x, self.position.y, CAR_WIDTH, CAR_HEIGHT)
        if (self.position.x , self.position.y) == (other_car.position.x,other_car.position.y):
            return 1
        return 0
    def set_accel(self, new_accel):
        """
        This is what the AI uses to control the accleration of the vehicle
        """
        if self.direction == Directions.left or self.direction == Directions.up:
            new_accel *= -1
            
        if self.acceleration[0] == 0:
            self.acceleration = pg.math.Vector2(0, new_accel)
        else:
            self.acceleration = pg.math.Vector2(new_accel, 0)
            
    def set_velocity(self,new_vel):
        self.velocity = pg.math.Vector2(self.direction[0]*new_vel, self.direction[1] * new_vel)
    def update(self, dt):
        self.velocity += self.acceleration * dt
        
        if self.direction == Directions.right:
            if self.velocity[0] < 0:
                self.velocity.x = 0
        elif self.direction == Directions.left:
            if self.velocity[0] > 0:
                self.velocity.x = 0
        elif self.direction == Directions.up:
            if self.velocity[1] > 0:
                self.velocity.y = 0
        elif self.direction == Directions.down:
            if self.velocity[1] < 0:
                self.velocity.y = 0
                
        self.position += self.velocity * dt
        self.completed_intersection = self.in_intersection()
        
    def completion_check(self):
        if self.direction == Directions.right:
            return self.position.x > 1540
        elif self.direction == Directions.left:
            return self.position.x < -100
        elif self.direction == Directions.up:
            return self.position.y < -100
        elif self.direction == Directions.down:
            return self.position.y > 900
    
    def draw(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))
        
    def gen_pos_lane(self, lane, direction):
        #Generates X and Y given lane and direction
        if direction == Directions.up:
            if lane == 0:
                return pg.math.Vector2(775, 900)
            if lane == 1:
                return pg.math.Vector2(831, 900)
        elif direction == Directions.down:
            if lane == 0:
                return pg.math.Vector2(717, -100)
            if lane == 1:
                return pg.math.Vector2(661, -100)
        elif direction == Directions.left:
            if lane == 0:
                return pg.math.Vector2(1540, 367)
            if lane == 1:
                return pg.math.Vector2(1540, 318)
        elif direction == Directions.right:
            if lane == 0:
                return pg.math.Vector2(-100, 462)
            if lane == 1:
                return pg.math.Vector2(-100, 509)
                
        return None
    
    def rotate_image(self, screen, old_image):
        if self.direction == Directions.left:
            return old_image
        
        if self.direction == Directions.right:
            rotated = pg.transform.rotate(old_image, 180)
        elif self.direction == Directions.up:
            rotated = pg.transform.rotate(old_image, 270)
        elif self.direction == Directions.down:
            rotated = pg.transform.rotate(old_image, 90)
        rect = rotated.get_rect()
        self.position.x -= rect.width / 2        
        self.position.y -= rect.height / 2
        return rotated
    
    def in_intersection(self):
        if 820 > self.position.x > 620 and 500 > self.position.y > 300:
            return True
    
    def out_of_intersection(self):
        if self.direction == Directions.right and self.position.x > 820:
            return True
        elif self.direction == Directions.left and self.position.x < 620:
            return True
        elif self.direction == Directions.up and self.position.y < 300:
            return True
        elif self.direction == Directions.down and self.position.y > 500:
            return True
        
    # def request_reservation(self, intersection, intersection_x, intersection_y, current_time):
    # # """
    # # Requests a reservation from the intersection.
    # # Returns True if the reservation is granted, False otherwise.
    # # """
    #     acceleration = 0.0001  # Initial acceleration
    #     # while True:
    #     distance_to_intersection = self.position.distance_to(pg.math.Vector2(intersection_x, intersection_y))
    #     velocity_magnitude = self.velocity.magnitude()

    #     if velocity_magnitude != 0:  # Add this check
    #         estimated_arrival_time = current_time + distance_to_intersection / velocity_magnitude
    #         estimated_arrival_velocity = velocity_magnitude + acceleration * (estimated_arrival_time - current_time)

    #         # Request reservation from intersection
    #         # success = intersection.request_reservation(self.id, self.position.x, self.position.y, int(current_time), int(estimated_arrival_time))
    #         success = intersection.request_reservation(self.id, self.position.x, self.position.y)
    #     else:
    #         # Handle the case when velocity magnitude is zero
    #         # self.set_accel(0.0001)
    #         # success = False
    #         # print("hi")
    #         return False
    #         # Optionally, you can take some action here when the velocity is zero
    
    
    #     timeout_limit = 5  # Timeout limit in seconds
    #     start_time = time.time()
    #     while not success and (time.time() - start_time) < timeout_limit:
    #         # Retry the reservation request with a slightly reduced acceleration
    #         self.set_accel(-0.0001)
    #         time.sleep(0.1)  # Wait for a short time before retrying
    #         success = intersection.request_reservation(self.id, self.position.x, self.position.y)
    
    
    #     if success:
    #         # Reservation granted
    #         # print("True")
    #         self.set_accel(0.0001)
    #         return True
    #     else:
    #         # # Reservation not granted, adjust acceleration
    #         # if current_time + distance_to_intersection / self.velocity.magnitude() - estimated_arrival_time > 1:
    #         #     # If substantially early, attempt to change to an earlier reservation
    #         #     acceleration += 0.0001
    #         #     # print("False")
                
    #         # else:
    #         # Decelerate and request again
    #         if self.direction == Directions.left or self.direction == Directions.up:
    #             a = (self.velocity.magnitude() ** 2)/(2*(distance_to_intersection-100))
    #         else:
    #             a = (self.velocity.magnitude() ** 2)/(2*(distance_to_intersection+100))
    #         self.set_accel(-0.)
    #         acceleration = 0.0001  # Reset acceleration for next request
    #         # print("False")
    #         return False

    def request_reservation(self, intersection, intersection_x, intersection_y, current_time):
        acceleration = 0.0001  # Initial acceleration

        # Calculate distance to intersection
        distance_to_intersection = self.position.distance_to(pg.math.Vector2(intersection_x, intersection_y))

        # Calculate estimated arrival time and velocity
        velocity_magnitude = self.velocity.magnitude()
        if velocity_magnitude != 0:
            estimated_arrival_time = current_time + distance_to_intersection / velocity_magnitude
        else:
            self.set_accel(0.001)
            return False  # Cannot request reservation with zero velocity

        # Request reservation from intersection
        success = intersection.request_reservation(self.id, self.position.x, self.position.y)

        # Retry if reservation failed
        # retries = 5
        # while not success and retries > 0:
        #     # self.set_accel(-0.01) 
        #     # Decelerate slightly
        #     self.set_velocity(0)
        #     # time.sleep(0.1)  # Wait for a short time
        #     success = intersection.request_reservation(self.id, self.position.x, self.position.y)
        #     retries -= 1

        if success:
            # Reservation granted
            self.set_accel(0.001)  # Set acceleration for normal movement
            return True
        else:
            if self.out_of_intersection():
                intersection.unreserve_vehicle(self.id)
            # # Reservation not granted, adjust acceleration and retry
            # if self.direction == Directions.left or self.direction == Directions.up:
            #     a = (self.velocity.magnitude() ** 2) / (2 * (distance_to_intersection - 100))
            # else:
            #     a = (self.velocity.magnitude() ** 2) / (2 * (distance_to_intersection + 100))
            self.set_accel(-0.001)  # Decelerate further for retry
            # self.set_velocity(0)
            # time.sleep(0)  # Wait for a short time
            # self.set_accel(0.0001)  # Reset acceleration for next request
            return False


    def decelerate(self):
        """
        Decelerates the vehicle to a minimum velocity.
        """
        min_velocity = 0.1  # Minimum velocity
        if self.velocity.magnitude() > min_velocity:
            self.velocity -= 0.0001  # Deceleration rate