from scipy.optimize import linprog
import math
# от рукинаписанные нужные части numpy
from my_numpy import *

eps = 0.00001


# class that contain function, it's derivative and spetial combination for optimization
class Func:
    def __init__(self, func, func_der):
        self.f = func
        self.fder = func_der
        
    def J_k(self, u_k, u):
        return sum(self.fder(u_k) * (u - u_k))
        
# class that contain some type frames for optimisation and minimization method for this type of frames and linear function
class Frames:
    #-----------------------------------------------
    #type 0: frames like a_i <= u_i <= b_i
    def __set_frames0(self, a, b):
        self.a = a
        self.b = b
    #type 1: frame for symplex method
    def __set_frames1(self, A, b):
        self.A = A
        self.b = b
        
    __setframesfuncs = {
        0: __set_frames0,
        1: __set_frames1
    }
    #-----------------------------------------------
    def __set_size0(self):
        if len(self.a) == len(self.b):
            return len(self.a)
        else:
            return -1
    def __set_size1(self):
        if len(self.A) == len(self.b):
            return len(self.b)
        else:
            return -1
        
    __setSize = {
        0: __set_size0,
        1: __set_size1
    }
    #------------------------------------------------
    def __init__(self, type_of_conditions, minimize_func):
        self.type = type_of_conditions
        self.minimize = minimize_func
        self.setframes = self.__setframesfuncs.get(type_of_conditions)
        self.size = self.__setSize.get(type_of_conditions)
        
    def get_size(self):
        return self.size(self)    

# class of task contains function, frames and some help functions and parameters
class Job:
    def __init__(self, func, frames, u_0, alpha):
        self.f = func
        self.frames = frames
        self.u_0 = u_0  # start point
        self.u_k = u_0 # the point got last time
        self.__alpha = alpha # rule(function) for alpha calculation
        self.k = 0 # step number
     
    # сheck task by
    # compare dimension of function, derivative, frames and x 
    def check_errors(self):
        a = type(self.f.f(self.u_0))
        b = len(self.f.fder(self.u_0))
        c = self.frames.get_size()
        print("func:",a,"\nframes:",c,"\nder:",b,"\nu_0:", len(self.u_0), "\n")
    
    # calculate new point using previus
    def get_next_u(self, u1_k):
        self.k+=1
        return self.u_k + (u1_k - self.u_k)*self.__alpha(self, u1_k)
    
    # find abutting poin
    def find_u1_k(self):
        return self.frames.minimize(self.f, self.frames, self.u_k)


# one variable function minimisation methods
class One_variable_function_minimisation_methods:    
    #---------------------------------------------------
    @staticmethod
    def golden_ratio_method(func, a, b, eps=0.000001):
        __MAGIC_CONSTANT_1 = (3 - math.sqrt(5))/2
        __MAGIC_CONSTANT_2 = (math.sqrt(5) - 1)/2
        while True:
            if b-a < eps:
                return (a+b)/2
            u1 = a + __MAGIC_CONSTANT_1*(b-a)
            u2 = a + __MAGIC_CONSTANT_2*(b-a)
            if func(u1)<=func(u2):
                b = u2
            else:
                a = u1
        return -1
    #---------------------------------------------------
    @staticmethod
    def broken_line_method(func, a, b, L, eps=0.000001):
        def go(f, u, u0):
            return f(u0)-L*abs(u-u0)
        u0 = (a+b)/2
        p = []
        while True:
            u0 = max()
        return -1
    #---------------------------------------------------
    @staticmethod
    def tangent_method(func, a, b, eps=0.000001):
        while True:
            if func.fder(a)>=0:
                return a
            if func.fder(b)<=0:
                return b
            if abs(a-b)<eps:
                return (a+b)/2
            un = (func.f(a)-func.f(b)+b*func.fder(b)-a*func.fder(a))/(func.fder(b)-func.fder(a))
            if func.fder(un)<0:
                a = un
            else:
                b = un


#testng of one variable function minimisation methods
#print(One_variable_function_minimisation_methods.bisection_method((lambda x: x*x*x-x*x), -5, 1))
#print(One_variable_function_minimisation_methods.golden_ratio_method((lambda x: x*x*x-x*x), -5, 1))
#print(One_variable_function_minimisation_methods.tangent_method(Func((lambda x: x*x), (lambda x: 2.0*x)), -1, 2))

# alpha calculate rule 1
def alpha_1(J, u1_k):
    return 1.0/(J.k+1)

# alpha calculate rule 2
def alpha_2(J, u1_k):
    alpha = 1.0
    while True:
        u_k1 = J.u_k + alpha*(u1_k - J.u_k)
        if J.f.f(u_k1) < J.f.f(J.u_k):
            return alpha
        if alpha < eps:
            break
        alpha/=2.0
    return 0.0

# alpha calculate rule 3 (safety)
def alpha_3(J, u1_k):
    def f_k(alpha):
        return J.f.f(J.u_k+alpha*(u1_k-J.u_k))
    def f_k_der(alpha):
        return np.dot((u1_k-J.u_k),J.f.fder(J.u_k+alpha*(u1_k-J.u_k)))
    return One_variable_function_minimisation_methods.tangent_method(Func(f_k, f_k_der), 0, 1)


# minimazation function for spetial frames type (a<x<b)
def frames_minnimize_function(func, frames, u_k):
    ans = []
    der = func.fder(u_k)
    for i in range(0, len(der)):
        if der[i]>0:
            ans.append(frames.a[i])
        elif der[i]<0:
            ans.append(frames.b[i])
        else:
            ans.append((frames.a[i]+frames.b[i])/2)
    return np.array(ans)

# minimisation function(symplex method) for spetioal(linear) type of frames
def symplex_meyhod_minimize_function(func, frames, u_k):
    return np.array(linprog(func.fder(u_k), frames.A, frames.b).x)


#test func
# x^2+xy+y^2
def f0(u):
    return u[0]*u[0]+u[0]*u[1]+u[1]*u[1]+0.0
def f0der(u):
    return np.array([2*u[0]+u[1], 2*u[1]+u[0]])
func0 = Func(f0, f0der)

#0<=x<=1, -1<=y<=0
frames0 = Frames(0, frames_minnimize_function)
frames0.setframes(frames0, np.array([0.0, -1.0]), np.array([1.0,0.0]))
#0x+y<=0  0x-y<=1 x+0y<=1 -x+0y<=0
frames1 = Frames(1, symplex_meyhod_minimize_function)
frames1.setframes(frames1, np.array([[0,1],[0,-1],[1,0],[-1,0]]), np.array([0,1,1,0]))



job0 = Job(func0, frames0, np.array([1,-1]), alpha_1) #u0=(1,-1)
#job0.check_errors()
job1 = Job(func0, frames0, np.array([-1,0]), alpha_1) #u0=(-1,0)
#job1.check_errors()
job2 = Job(func0, frames1, np.array([1, 0]), alpha_1) #u0=(1, 0)
#job2.check_errors()
job3 = Job(func0, frames0, np.array([0, 0]), alpha_1) #u0=(0, 0)
#job3.check_errors()



# method for different stop rules
def calculate_m(job, eps, steps):
    def method_full(J, eps, steps):
        f_sequ = []
        u_k_sequ = []
        k = 0
        f_sequ.append(J.f.f(J.u_k))
        u_k_sequ.append(J.u_k)
        u_k = 0
        while True:
            u1_k = J.find_u1_k()
            u_k = J.u_k
            J.u_k = J.get_next_u(u1_k)
            f_sequ.append(J.f.f(J.u_k))
            u_k_sequ.append(J.u_k)
            if k>steps or np.all(J.u_k == u_k) or abs(J.f.f(J.u_k) - J.f.f(u_k)) <= eps:
                break
            k+=1
        return J.f.f(J.u_k), J.u_k, f_sequ, u_k_sequ, k, abs(J.f.f(J.u_k) - J.f.f(u_k))
    def method_eps(J, eps):
        f_sequ = []
        u_k_sequ = []
        k = 0
        f_sequ.append(J.f.f(J.u_k))
        u_k_sequ.append(J.u_k)
        u_k = 0
        while True:
            u1_k = J.find_u1_k()
            u_k = J.u_k
            J.u_k = J.get_next_u(u1_k)
            f_sequ.append(J.f.f(J.u_k))
            u_k_sequ.append(J.u_k)
            if k>100000000 or np.all(J.u_k == u_k) or abs(J.f.f(J.u_k) - J.f.f(u_k)) <= eps:
                break
            k+=1
        return J.f.f(J.u_k), J.u_k, f_sequ, u_k_sequ, k, abs(J.f.f(J.u_k) - J.f.f(u_k))
    def method_steps(J, steps):
        f_sequ = []
        u_k_sequ = []
        k = 0
        f_sequ.append(J.f.f(J.u_k))
        u_k_sequ.append(J.u_k)
        u_k = 0
#       print("u_k:{}, f:{}".format(J.u_k, J.f.f(J.u_k)))
        while True:
            u1_k = J.find_u1_k()
            u_k = J.u_k
            J.u_k = J.get_next_u(u1_k)
 #           print("u_k:{}, f:{}, u1_k:{}".format(J.u_k, J.f.f(J.u_k), u1_k))
            f_sequ.append(J.f.f(J.u_k))
            u_k_sequ.append(J.u_k)
            if k>steps or np.all(J.u_k == u_k):
                break
            k+=1
        return J.f.f(J.u_k), J.u_k, f_sequ, u_k_sequ, k+1, abs(J.f.f(J.u_k) - J.f.f(u_k))

    if steps == -1:
        return method_eps(job, eps)
    elif eps == -1:
        return method_steps(job, steps)
    return method_full(job, eps, steps)

calculate_m(job1, -1, 100)