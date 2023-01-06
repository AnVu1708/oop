#class, contrusctor, abilities 
class animal:
    def __init__(self, height,heavy,sex,move): 
        self.height = height
        self.heavy = heavy
        self.move = move 
        self.sex = sex
    
Lion = animal("3ft","700kg","female"," are running")
Lion.type = "Lion"
Bird = animal("25cm","10kg","male"," are flying")
Bird.type = "Bird"
print(Lion.sex + " " +Lion.type + Lion.move) 

#Instance method
class animal:
    name = "Bird"
    def color(self):
        print ("Red")
pinkbird = animal()
pinkbird.name = pinkbird
pinkbird.color()
Carolasparotia = animal()
Carolasparotia.name = "Carolasparotia"
Carolasparotia.color()
class animal:
    color = ""
pinkbird = animal()
pinkbird.color= "pink"
Carolasparotia = animal ()
Carolasparotia.color ="red"

class Animal():
    sound = ""
    def __init__(self,name):
        self.name = name
    def roar(self):
       print("{sound}! I am {name}. {sound}".format(sound=self.sound, name=self.name))
        
class Lion(Animal):
    sound = "GRRR"
Shiba = Lion("Shiba")
Shiba.roar()

#Assessment
#begin portion 1
import random
class Server:
    def __init__(self):
        self.connections={}
    def add_connection(self, connection_id):
        connection_load =random.random()*10+1
        #Add the connection to the dictionary with the calculated load
    def close_connection(self, connection_id):
        """Closes the connection from the dictionary""" 
    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        return total
    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
server = Server()
server.add_connection("192.168.1.1")

print(server.load())
server.close_connection("192.168.1.1")
print(server.load())
#begin portion 2
class LoadBalance:
    def__init__(self):
        self.connections = {}
        self.servers = [Server()]
    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it"""
        server = random.choice(self.servers)
        #add the connection to the dictionary with the selected server
        #add the connection to the server
    def close_connection(self, connection_id):
        """Closes the connection on the server corresponding to connection id"""
        #findout the right server
        #close the connection on the server
        #remove the connection from the load balancer
        
    def avg_load(self):
        """Calculates the average load of all server"""
        #Sum the load of each server and divide by the amount of server
        return 0
    def ensure_availability(self):
        """if the average load is higher than 50, spin up a new server"""
        pass
    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#end protion 2
l = LoadBalance
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())
l.servers.append(Server())
print(l.avg_load())
l.close_connection("fdca:83d2::f20d")
print(l.avg_load())
for connection in range(20):
    l.add_connection(connection)
print(l)
print(l.avg_load())

             
