# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 10:14:43 2023

@author: LuizH
"""
import matplotlib.pyplot as plt
import math

def colision(ball_1, ball_2):
    newBall_1Velocity = (((ball_1.mass - ball_2.mass) / (ball_1.mass + ball_2.mass)) * ball_1.velocity) + (((2*ball_2.mass)/(ball_1.mass + ball_2.mass)) * ball_2.velocity)
    newBall_2Velocity = ((2*ball_1.mass) / (ball_1.mass + ball_2.mass)*ball_1.velocity) - (((ball_1.mass - ball_2.mass) / (ball_1.mass + ball_2.mass)) * ball_2.velocity)
    ball_1.velocity = newBall_1Velocity
    ball_2.velocity = newBall_2Velocity
    
class Ball:
    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        
def checkColisions(ball_1, ball_2):
    colisions = 0
    time = [0]
    time_temp = 0
    velocity_1 = [ball_1.velocity]
    velocity_2 = [ball_2.velocity]
    kinetic_energy_1 = [(ball_1.mass*math.pow(ball_1.velocity, 2))/2]
    kinetic_energy_2 = [(ball_2.mass*math.pow(ball_2.velocity, 2))/2]
    
    
    while (ball_1.velocity < 0 or ball_2.velocity < 0 or ball_2.velocity < ball_1.velocity):
        timeToBallColision = (ball_1.position - ball_2.position) / (ball_2.velocity - ball_1.velocity)

        timeToWall = -ball_1.position / ball_1.velocity if ball_1.velocity != 0 else float('inf')
        
        if(ball_1.velocity < 0 and timeToBallColision < timeToWall):
            block2PositionOnWallColision = ball_2.position + (ball_2.velocity * timeToWall)
            ball_1.position = 0
            ball_2.position = block2PositionOnWallColision
            ball_1.velocity = ball_1.velocity * -1
            time_temp += timeToWall
            time.append(time_temp)
        # will colide with block
        else:
            blocksPositionOnColide = ball_1.position + (ball_1.velocity * timeToBallColision)
            ball_2.position = blocksPositionOnColide
            ball_1.position = blocksPositionOnColide
            colision(ball_1, ball_2)
            time_temp += timeToBallColision
            time.append(time_temp)
        colisions += 1
        velocity_1.append(ball_1.velocity)
        velocity_2.append(ball_2.velocity)
        kinetic_energy_1.append((ball_1.mass*math.pow(ball_1.velocity, 2))/2)
        kinetic_energy_2.append((ball_2.mass*math.pow(ball_2.velocity, 2))/2)
    print("Total Collisions: %d" %(colisions))
    
    plt.plot(velocity_1, velocity_2)
    plt.title("Phase diagram")
    plt.ylabel("Ball 2 Velocity")
    plt.xlabel("Ball 1 Velocity")
    #plt.plot(time, kinetic_energy_2)
    #plt.plot(time, kinetic_energy_1)
    #plt.yscale("log", base=0.1)
    plt.show()
    

digits = 3
for i in range(digits):
    ball_2mass = math.pow(100, i)
    ball_1 = Ball(7, 0, 1)
    ball_2 = Ball(10, -1, ball_2mass)
    checkColisions(ball_1, ball_2)