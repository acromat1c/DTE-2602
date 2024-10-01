from random import choice

class Robot:

    def __init__(self):
        # sets up map
        w = 4
        m = 2
        g = 1
        self.map = [[w,w,m,m,m,g],[m,w,g,g,g,w],[m,g,g,g,m,w],[g,m,m,g,g,w],[g,g,g,g,m,w],[w,g,m,g,g,w]]

        # determins number of iterations for monte carlo and q learn
        self.Episodes = 1000

        # sets up new q learn Table
        self.Table = [ [1000 for j in self.map[0]] for i in self.map]

        # sets the goal coordinates
        self.finishX = 0
        self.finishY = 5



    def reset_random(self):
        # moves robot back to start
        self.x = 3
        self.y = 0
        #resets list of visited squeres
        self.visited = []
    


    def has_reached_goal(self):
        # checks if robot is on goal squere
        if self.x==self.finishX and self.y==self.finishY: return True 



    def get_x(self):
        # returns x
        return self.x
        
    def get_y(self):
        # returns y
        return self.y



    def get_avalible(self):
        # returns all avalible squeres. makes sure robot does not travel outside map.
        avalible = []
        if self.x!=0:avalible.append([self.x-1,self.y])
        if self.x!=len(self.map)-1:avalible.append([self.x+1,self.y])
        if self.y!=0:avalible.append([self.x,self.y-1])
        if self.y!=len(self.map[self.x])-1:avalible.append([self.x,self.y+1])
        
        # makes so that the robot does not travel on the same squere twice in the same jurney
        avalible = [i for i in avalible if i not in self.visited]

        # puts robot back at start if stuck
        if avalible == []:
            self.reset_random()
            return self.get_avalible()

        return avalible



    def adjustTable(self):
        # calculates the score for the path the robot has taken
        score = sum([self.map[i[0]][i[1]] for i in self.visited])
        # assign squeres a value based on how good of an option moving to them is
        for i in self.visited:
            l = len(self.visited)
            if score < self.Table[i[0]][i[1]]:
                self.Table[i[0]][i[1]] = score



    def monte_carlo_exploration(self):
        # each loop in the for loop is equivelent to one trip from start to finish for the robot
        for _ in range(self.Episodes):
            # moves everythin to start
            self.reset_random()
            #robot traveles until it reaches the goal
            while True:
                # choses random avalible direction
                self.x,self.y = choice(self.get_avalible())
                # adds the current squere to visited squeres
                self.visited.append([self.x,self.y])
                # ends loop if robot reaches goal
                if self.has_reached_goal(): break
            self.adjustTable()
        # returnes that table
        return self.Table



    def get_next_state_eg(self,explore = True):
        # Return the next state based on Epsilon-greedy.
        options = self.get_avalible()
        # checks what direction is best to move in. if multiple are equaly good it adds all of them to the list of potential options
        opt = [ i for i in options if self.Table[i[0]][i[1]] == min([self.Table[j[0]][j[1]] for j in options])]
        # if exploration is enabled it will ad a random direction that may or may not be selected
        if explore == True:
            opt.append(choice(options))
        # returns one of the possible options
        return choice(opt)    



    def q_learning(self):
        # each loop in the for loop is equivelent to one trip from start to finish for the robot. it uses this to create the table for the q learn
        for _ in range(self.Episodes):
            # puts everything back to start
            self.reset_random()
            # lets the robot run around untill it reaches goal
            while True:
                # gets next move from "get_next_state_eg" 
                self.x,self.y = self.get_next_state_eg()
                # adds current squere to list of visited squeres
                self.visited.append([self.x,self.y])
                # checks if goal has been reached
                if self.has_reached_goal(): break
            # calculates the score for the path the robot has taken
            score = sum([self.map[i[0]][i[1]] for i in self.visited])
            # assign squeres a value based on how good of an option moving to them is
            self.adjustTable()
        # run one last loop without any random variation and returns the best path that has been found
        while True:
            self.x,self.y = self.get_next_state_eg(explore=False)
            self.visited.append([self.x,self.y])
            if self.has_reached_goal():
                return self.visited


    # q learn used with pygame to create a visual demo.
    def one_step_q_learning(self):
        # gets next move from "get_next_state_eg" 
        self.x,self.y = self.get_next_state_eg()
        # adds current squere to list of visited squeres 
        self.visited.append([self.x,self.y])
        # checks if goal has been reached
        if self.has_reached_goal():
            self.adjustTable()

if __name__ == "__main__":
    R = Robot()
    print(R.monte_carlo_exploration())
    print(R.q_learning)
