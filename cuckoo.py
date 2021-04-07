import math
import random
import tkinter as tk
from typing import Text

class nest: 
    def __init__(self,id = 0):
        self.id = id 
        self.x_value = random.random()
        self.y_value = random.random()  
        self.f_value = booth(self)


class cuckoo_algo:
    def __init__(self,discard, rad):
        self.host_nests = []
        self.frac_discard = discard
        self.n = 0
        self.radius = rad

    def update_n(self):
        self.n = len(self.host_nests)
        
    
    def make_host_nests(self,n, in_radius = False):
        print("new hosts")
        for i in range(n):
            self.host_nests.append(nest(i))
            if in_radius:
                best_x = self.host_nests[0].x_value
                best_y = self.host_nests[0].y_value 
                self.host_nests[-1].x_value = random.uniform(best_x-self.radius, best_x+self.radius)
                self.host_nests[-1].y_value = random.uniform(best_y-self.radius, best_y+self.radius)
                self.host_nests[-1].f_value = booth(self.host_nests[-1])

            print(self.host_nests[-1].f_value)
        self.update_n()
        
        print("---")

    def printing(self):
        print(self.nests[1].id)

    def run_one_iteration(self):
        self.random_cuckoo_check()
        self.discard_method()
        self.host_nests.sort(key=lambda x: x.f_value)

    def print_all_f_value(self):
        print("Current F-values")
        for each in self.host_nests:
            print(each.f_value)

    def random_cuckoo_check(self):
        cuckoo = nest()
        print("cuckoo")
        print(cuckoo.f_value)
        print("---")
        random_nest = random.randint(0, len(self.host_nests)-1)  
        print("random egg")
        print(self.host_nests[random_nest].f_value)
        print("---")
        if(cuckoo.f_value < self.host_nests[random_nest].f_value ):
            print("replaced it!")
            self.host_nests[random_nest] = cuckoo 

    def discard_method(self):
        self.host_nests.sort(key=lambda x: x.f_value)
        num_disc = int(self.n*self.frac_discard)
        for i in range(num_disc):
            self.host_nests.pop()
        self.make_host_nests(num_disc , 1)

    def print_final(self):
        best_nest = self.host_nests[0]
        print("The best nest award goes to ")
        print("x-value= ",best_nest.x_value,"\ny-value= ",best_nest.y_value,"\nf-value= ",best_nest.f_value)
        print("---")

    def final_string(self):
        pass


def cuckoo_run(num_hosts,iteration, fraction_discard = 0.5, radius = 1):
    calgo  = cuckoo_algo(fraction_discard,radius)
    calgo.make_host_nests(num_hosts)
    for i in range(iteration):
        print("Iteration no. ", i)
        calgo.run_one_iteration()
    calgo.print_all_f_value()
    calgo.print_final()
    return calgo


def booth(nest):
    x = nest.x_value
    y = nest.y_value
    f_value = (x + 2*y - 7)*(x + 2*y - 7) + (2*x + y - 5)*(2*x + y - 5)
    return f_value

class cuckoo_output:
    def __init__(self,algo):
        self.root = tk.Tk()
        self.cuck = algo

    def start(self):
        self.root.title("Cuckoo")
        box = tk.Text(self.root)
        box.grid()
        self.print_final(box)
        self.root.mainloop()

    def print_final(self,box):
        best_nest = self.cuck.host_nests[0]
        box.insert(tk.END,"The best nest award goes to \n")
        box.insert(tk.END,"x-value= ")
        box.insert(tk.END,str(best_nest.x_value))
        box.insert(tk.END,"\ny-value= ")
        box.insert(tk.END,str(best_nest.y_value))
        box.insert(tk.END,"\nf-value= ")
        box.insert(tk.END,str(best_nest.f_value))
        box.insert(tk.END,"\n---")

if __name__ == "__main__":
    print("main")
    cuckoo_algo = cuckoo_run(num_hosts = 10,iteration = 100,fraction_discard= 0.5,radius= 1)
    out = cuckoo_output(cuckoo_algo)
    out.start()

else:
    print ("Executed when imported")
    