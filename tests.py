from task import *

# push tests here


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



#job0 = Job(func0, frames0, np.array([1,-1]), alpha_1) #u0=(1,-1)
#job0.check_errors()
#job1 = Job(func0, frames0, np.array([-1,0]), alpha_1) #u0=(-1,0)
#job1.check_errors()
#job2 = Job(func0, frames1, np.array([1, 0]), alpha_1) #u0=(1, 0)
#job2.check_errors()
#job3 = Job(func0, frames0, np.array([0, 0]), alpha_1) #u0=(0, 0)
#job3.check_errors()

