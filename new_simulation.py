from car import Directions, AssetManager, Car
import pygame as pg
import random
import time
from intersection_manager import IntersectionPolicy
import threading

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 800
SPAWN_RATE = 5 #cars per second

# BACKGROUND = pg.image.load('./res/Intersection.png')
BACKGROUND = pg.image.load('./res/ExpandedIntersection.png')

def quitGame(): #Quits Pygame and Python
    pg.quit()
    quit()

def backgroundInputCheck(eventList): # Constantly checks for quits and enters
    for event in eventList:
            if event.type == pg.QUIT:
                quitGame()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quitGame()
                    

# def car_thread_func(car, intersection, center_x, center_y):
#     while True:
#         current_time = time.perf_counter()
#         # for car in current_cars:
#         success = car.request_reservation(intersection, center_x, center_y, current_time)
#         print(success)
#         if car.out_of_intersection():
#             intersection.unreserve_vehicle(car.id)
#         # if success:
#         #     car.set_accel(0.001)
#         # else:
#         #     car.set_accel(-0.001)
#         time.sleep(1)

# def main():
#     CENTER = pg.math.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
#     BACKGROUND.convert()
#     start = time.perf_counter()
#     current_cars = []  # Maintains a list of current cars in the scene
    
#     intersection = IntersectionPolicy()  # Initialize the intersection object
#     arrival_time = 0  # Initial arrival time
#      # Initial current time

#     while len(current_cars) < 100:  # Loop until there is a possible traffic jam
#         deltaTime = clock.get_time()
#         backgroundInputCheck(pg.event.get())

#         if (time.perf_counter() - start) > (1 / SPAWN_RATE):
#             initial_velocity = (random.randrange(3) * 0.1) + 0.2
#             lane = random.randrange(2)
#             new_car = Car(len(current_cars),screen ,lane, initial_velocity=initial_velocity)
#             current_cars.append(new_car)
#             current_time = time.perf_counter() 
#             # success = new_car.request_reservation(intersection, CENTER.x,CENTER.y, current_time)
#             # print(success)
#             # Start a new thread for the car
#             car_thread = threading.Thread(target=car_thread_func, args=(new_car, intersection, CENTER.x, CENTER.y))
#             car_thread.start()
            
#             # if not success:
#             #     new_car.set_accel(-0.001)
#             # else:
#             #     new_car.set_accel(0.001)

#             start = time.perf_counter()
#         # print(current_cars)
#         screen.blit(BACKGROUND, (0, 0))
#         for car in current_cars:
#             if car.completion_check():
#                 intersection.unreserve_vehicle(car.id)
#                 current_cars.remove(car)
#             elif car.out_of_intersection():
#                 car.set_accel(0.001)
#                 car.update(deltaTime)
#                 car.draw(screen)
#                 intersection.unreserve_vehicle(car.id)
#             else:
#                 # car.request_reservation(intersection, CENTER.x,CENTER.y, current_time)
#                 car.update(deltaTime)
#                 car.draw(screen)

#         clock.tick(60)
#         pg.display.flip()


import threading
from concurrent.futures import ThreadPoolExecutor
import asyncio

# def car_thread_func(car, intersection, center_x, center_y):
#     while True:
#         current_time = time.perf_counter()
#         success = car.request_reservation(intersection, center_x, center_y, current_time)
#         print(success)
#         if car.out_of_intersection():
#             intersection.unreserve_vehicle(car.id)
#             break
        
#         if not success:
#             car.set_accel(-0.001)  # Decelerate
#             time.sleep(1)  # Wait for a short time
#             continue  # Retry the reservation request

# total_collisions = 0
# collision_lock = threading.Lock()
# def car_thread_func(car, intersection, center_x, center_y, current_cars):
#     global total_collisions
#     retries = 100  # Maximum number of reservation request retries
#     while True:
#         current_time = time.perf_counter()
#         success = car.request_reservation(intersection, center_x, center_y, current_time)
#         print(success)
#         if car.out_of_intersection():
#             intersection.unreserve_vehicle(car.id)
#             break

#         if not success:
#             retries -= 1
#             if retries == 0:
#                 break  # Exit the loop if maximum retries reached
#             car.set_accel(-0.1)  # Decelerate
#             time.sleep(1)  # Wait for a short time
#             continue  # Retry the reservation request

#         car.set_accel(0.0001)  # Accelerate once out of the intersection
#         car.update()
        
#         # Check for collisions with other cars
#         for other_car in current_cars:
#             if car != other_car and car.check_collision(other_car):
#                 with collision_lock:
#                     total_collisions += 1
#                 car.collisions += 1
#                 other_car.collisions += 1
#         time.sleep(3)
# def main():
#     CENTER = pg.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#     BACKGROUND.convert()
#     start = time.perf_counter()
#     current_cars = []  # Maintains a list of current cars in the scene

#     intersection = IntersectionPolicy()  # Initialize the intersection object
#     arrival_time = 0  # Initial arrival time
#     # Initial current time

#     executor = ThreadPoolExecutor(max_workers=10)  # Use a ThreadPoolExecutor with 10 threads

#     while len(current_cars) < 100:  # Loop until there is a possible traffic jam
#         deltaTime = clock.get_time()
#         backgroundInputCheck(pg.event.get())

#         if (time.perf_counter() - start) > (1 / SPAWN_RATE):
#             initial_velocity = (random.randrange(3) * 0.1) + 0.2
#             lane = random.randrange(2)
#             new_car = Car(len(current_cars), screen, lane, initial_velocity=initial_velocity)
#             current_cars.append(new_car)
#             current_time = time.perf_counter()
#             # Start a new thread for the car
#             executor.submit(car_thread_func, new_car, intersection, CENTER.x, CENTER.y, current_cars)

#             start = time.perf_counter()

#         screen.blit(BACKGROUND, (0, 0))
#         for car in current_cars:
#             if car.completion_check():
#                 intersection.unreserve_vehicle(car.id)
#                 current_cars.remove(car)
#             # elif car.out_of_intersection():
#             #     car.set_accel(0.001)
#             #     car.update(deltaTime)
#             #     car.draw(screen)
#             #     intersection.unreserve_vehicle(car.id)
#             else:
#                 car.update(deltaTime)
#                 car.draw(screen)

#         # total_collisions = sum(car.collisions for car in current_cars)
#         global total_collisions
#         print(f"Total collisions: {total_collisions}")
#         clock.tick(60)
#         pg.display.flip()


# def main():
#     CENTER = pg.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#     BACKGROUND.convert()
#     start = time.perf_counter()
#     current_cars = []  # Maintains a list of current cars in the scene

#     intersection = IntersectionPolicy()  # Initialize the intersection object
#     arrival_time = 0  # Initial arrival time
#     # Initial current time

#     while len(current_cars) < 100:  # Loop until there is a possible traffic jam
#         deltaTime = clock.get_time()
#         backgroundInputCheck(pg.event.get())

#         if (time.perf_counter() - start) > (1 / SPAWN_RATE):
#             initial_velocity = (random.randrange(3) * 0.1) + 0.2
#             lane = random.randrange(2)
#             new_car = Car(len(current_cars), screen, lane, initial_velocity=initial_velocity)
#             current_cars.append(new_car)
#             current_time = time.perf_counter()

#             success = new_car.request_reservation(intersection, CENTER.x, CENTER.y, current_time)
#             if not success:
#                 intersection.unreserve_vehicle(new_car.id)
#                 current_cars.remove(new_car)
#                 continue

#             start = time.perf_counter()

#         screen.blit(BACKGROUND, (0, 0))
#         for car in current_cars:
#             if car.completion_check():
#                 intersection.unreserve_vehicle(car.id)
#                 current_cars.remove(car)
#             elif car.out_of_intersection():
#                 car.set_accel(0.001)
#                 car.update(deltaTime)
#                 car.draw(screen)
#                 intersection.unreserve_vehicle(car.id)
#             else:
#                 car.update(deltaTime)
#                 car.draw(screen)

#         total_collisions = 0
#         for car in current_cars:
#             for other_car in current_cars:
#                 if car != other_car and car.check_collision(other_car):
#                     total_collisions += 1
#         print(f"Total collisions: {total_collisions}")

#         clock.tick(60)
#         pg.display.flip()
# current_cars = []
# def main():
#     CENTER = pg.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#     BACKGROUND.convert()
#     start = time.perf_counter()
#     # global current_cars
#     # current__cars = [] # Maintains a list of current cars in the scene

#     intersection = IntersectionPolicy()  # Initialize the intersection object

#     while True:  # Loop until there is a possible traffic jam
#         deltaTime = clock.get_time()
#         backgroundInputCheck(pg.event.get())
#         global current_cars
#         if len(current_cars) < 10:
#             # 
#             # if (time.perf_counter() - start) > (1 / SPAWN_RATE):
#             #     print("hi")
#                 initial_velocity = (random.randrange(3) * 0.1) + 0.2
#                 lane = random.randrange(2)
#                 new_car = Car(len(current_cars), screen, lane, initial_velocity=initial_velocity)
#                 current_cars.append(new_car)
#                 # start = time.perf_counter() 
                
#                 current_time = time.perf_counter()
#         screen.blit(BACKGROUND, (0, 0))

#         for car in current_cars:
#             success = car.request_reservation(intersection, CENTER.x, CENTER.y, current_time)
#             print(success)
#             if success == True:
#                 while not car.completion_check():
#                     print("hi")
#                     for new_car in current_cars.copy():  # Use a copy of the list to avoid modifying it during iteration
#                         if new_car.completion_check():
#                             intersection.unreserve_vehicle(new_car.id)
#                             current_cars.remove(new_car)
#                         elif new_car.out_of_intersection():
#                             intersection.unreserve_vehicle(new_car.id)
#                         else:
#                             new_car.update(deltaTime)
#                             new_car.draw(screen)
                            
#         clock.tick(60)
#         pg.display.flip()
#         # if not success:
#         #     # current_cars.remove(new_car)  # Remove the car if reservation failed
#         #     for i in range(10):
#         #         success = new_car.request_reservation(intersection, CENTER.x, CENTER.y, current_time)
#         #             if success == True:
#         #                 break
#         #         continue

#         start = time.perf_counter()

        # screen.blit(BACKGROUND, (0, 0))
        # for car in current_cars.copy():  # Use a copy of the list to avoid modifying it during iteration
        #     if car.completion_check():
        #         intersection.unreserve_vehicle(car.id)
        #         current_cars.remove(car)
        #     elif car.out_of_intersection():
        #         intersection.unreserve_vehicle(car.id)
        #     else:
        #         car.update(deltaTime)
        #         car.draw(screen)

        # total_collisions = sum(1 for car1 in current_cars for car2 in current_cars if car1 != car2 and car1.check_collision(car2))
        # print(f"Total collisions: {total_collisions}")

        
        


# if __name__ == "__main__":
#     main()


current_cars = []

def main():
    CENTER = pg.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    BACKGROUND.convert()
    start = time.perf_counter()
    intersection = IntersectionPolicy()  # Initialize the intersection object
    update_interval = 0.1
    # removal_times = []
    while True:  # Loop until there is a possible traffic jam
        deltaTime = clock.get_time()
        backgroundInputCheck(pg.event.get())
        global current_cars
        if len(current_cars) < 20:
            if (time.perf_counter() - start) > (1 / SPAWN_RATE):
                initial_velocity = (random.randrange(3) * 0.1) + 0.2
                lane = random.randrange(2)
                new_car = Car(len(current_cars), screen, lane, initial_velocity=initial_velocity)
                current_cars.append(new_car)
                start = time.perf_counter()  # Update the start time
                current_time = time.perf_counter()
                # new_car.creation_time = time.perf_counter()

          # Draw the background

        # for car in current_cars:
        #     current_time = time.perf_counter()
        #     success = car.request_reservation(intersection, CENTER.x, CENTER.y, current_time)
        #     print(success)
        #     if success:
        #         while not car.completion_check():
        #             elapsed_time = time.perf_counter() - current_time
        #             if elapsed_time > 0.1:  # Update the car's position every 100 milliseconds
        #                 # print(car.acceleration)
        #                 # print(car.acceleration)
        #                 # exit()
        #                 print(car.position)
        #                 for new_car in current_cars.copy():
        #                     if new_car.completion_check():
        #                         intersection.unreserve_vehicle(new_car.id)
        #                         current_cars.remove(new_car)
        #                     # elif new_car.out_of_intersection():
        #                     #     intersection.unreserve_vehicle(new_car.id)
        #                     else:
        #                         # print("hi")
        #                         new_car.update(deltaTime)
        #                         new_car.draw(screen)
        #                 current_time = time.perf_counter()  
        # 
        # Update the current time
        screen.blit(BACKGROUND, (0, 0))
        for car in current_cars:
            current_time = time.perf_counter()
            success = car.request_reservation(intersection, CENTER.x, CENTER.y, current_time)
            print(success)
            if success:
                # Calculate the distance to move based on the elapsed time
                # elapsed_seconds = deltaTime / 1000.0  # Convert milliseconds to seconds
                # distance_to_move = car.velocity.magnitude() * elapsed_seconds
                # while not car.completion_check():
                for i in range(10):
                    # print(car.acceleration)
                    # print(car.acceleration)
                    # exit()
                    # print(car.position)
                    
                    for new_car in current_cars.copy():
                        if new_car.completion_check():
                            intersection.unreserve_vehicle(new_car.id)
                            current_cars.remove(new_car)
                            # new_car.removal_times = time.perf_counter()
                        # elif new_car.out_of_intersection():
                        #     intersection.unreserve_vehicle(new_car.id)
                        else:
                            # print("hi")
                            if (time.perf_counter() - car.last_update_time) > update_interval:
                                new_car.update(deltaTime)
                                new_car.last_update_time = time.perf_counter()
                            new_car.draw(screen)
                            # new_car.update(deltaTime)
                            # new_car.draw(screen)
                            # time.sleep(0.01)
        
        # for car in current_cars:
        #     car.draw(screen)

            # for car in current_cars:
                # print(car.removal_times - car.creation_time)
        clock.tick(60)
        pg.display.flip()  # Update the display
        




# def main():
#     CENTER = pg.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#     BACKGROUND.convert()
#     start = time.perf_counter()
#     current_cars = []  # Maintains a list of current cars in the scene
#     intersection = IntersectionPolicy()  # Initialize the intersection object

#     while True:
#         deltaTime = clock.get_time()
#         backgroundInputCheck(pg.event.get())

#         if (time.perf_counter() - start) > (1 / SPAWN_RATE):
#             initial_velocity = (random.randrange(3) * 0.1) + 0.2
#             lane = random.randrange(2)
#             new_car = Car(len(current_cars), screen, lane, initial_velocity=initial_velocity)
#             current_cars.append(new_car)
#             start = time.perf_counter()

#         screen.blit(BACKGROUND, (0, 0))
#         for car in current_cars:
#             current_time = time.perf_counter()
#             success = car.request_reservation(intersection, CENTER.x, CENTER.y, current_time)
#             # success = True
#             if car.completion_check(): 
#                 current_cars.remove(car)
#             # elif car.out_of_intersection():
#                 # intersection.unreserve_vehicle(car.id)
#             else:
#                 car.update(deltaTime)
#                 car.draw(screen)

#         clock.tick(60)
#         pg.display.flip()


# def main():
#     CENTER = pg.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#     BACKGROUND.convert()
#     start = time.perf_counter()
#     current_cars = []  # Maintains a list of current cars in the scene
#     intersection = IntersectionPolicy()  # Initialize the intersection object

#     # Create a single car
#     initial_velocity = (random.randrange(3) * 0.1) + 0.2
#     lane = random.randrange(2)
#     new_car = Car(len(current_cars), screen, lane, initial_velocity=initial_velocity)
#     current_cars.append(new_car)

#     while True:
#         deltaTime = clock.get_time()
#         backgroundInputCheck(pg.event.get())

#         screen.blit(BACKGROUND, (0, 0))
#         for car in current_cars:
#             current_time = time.perf_counter()
#             # success = car.request_reservation(intersection, CENTER.x, CENTER.y, current_time)
#             # Start a new thread for the car
#             car_thread = threading.Thread(target=car_thread_func, args=(current_cars, intersection, CENTER.x, CENTER.y))
#             car_thread.start()
#             # print(success)
#             if car.completion_check(): 
#                 current_cars.remove(car)
#             else:
#                 car.update(deltaTime)
#                 car.draw(screen)

#         clock.tick(60)
#         pg.display.flip()




    # pg.quit()
# def main():
#     CENTER = pg.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
#     BACKGROUND.convert()
#     start = time.perf_counter()
#     current_cars = []  # Maintains a list of current cars in the scene
#     intersection = IntersectionPolicy()  # Initialize the intersection object
#     arrival_time = 0  # Initial arrival time
#     current_time = time.perf_counter()  # Initial current time
#     failed_attempts = 0  # Counter for consecutive failed reservation attempts
#     max_failed_attempts = 5  # Maximum number of consecutive failed attempts before resetting acceleration

#     while len(current_cars) < 2:  # Loop until there is a possible traffic jam
#         deltaTime = clock.get_time()
#         backgroundInputCheck(pg.event.get())

#         if (time.perf_counter() - start) > (1 / SPAWN_RATE):
#             initial_velocity = (random.randrange(3) * 0.1) + 0.2
#             lane = random.randrange(2)
#             new_car = Car(screen, len(current_cars), lane, initial_velocity=initial_velocity)
#             current_cars.append(new_car)
#             current_time = time.perf_counter()

#             success = new_car.request_reservation(intersection, CENTER.x, CENTER.y, current_time)
#             print(success)
#             if not success:
#                 failed_attempts += 1
#                 if failed_attempts >= max_failed_attempts:
#                     new_car.decelerate()
#                     failed_attempts = 0  # Reset the counter
#             else:
#                 failed_attempts = 0  # Reset the counter if reservation is successful

#             start = time.perf_counter()

#         screen.blit(BACKGROUND, (0, 0))
#         for car in current_cars:
#             if car.completion_check():
#                 current_cars.remove(car)
#             else:
#                 car.update(deltaTime)
#                 car.draw(screen)

#         clock.tick(60)
#         pg.display.flip()
    
if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Autonomous Intersection Management Software")
    clock = pg.time.Clock()
    main()
