dt = {"From Axis -> To Axis" : 0, "From Axis -> Auxiliary Axis" : 0, "To Axis -> From Axis" : 0, "To Axis -> Auxiliary Axis" : 0, "Auxiliary Axis -> To Axis" : 0, "Auxiliary Axis -> From Axis" : 0}

def Hanoi(n,f_r,t_r,a_r,dt):
    if n == 1:
        print(f_r,"-->",t_r)
        dt[f_r+" -> "+t_r] += 1
        return
    Hanoi(n-1,f_r,a_r,t_r,dt)
    print(f_r,"-->",t_r)
    dt[f_r+" -> "+t_r] += 1
    Hanoi(n-1,a_r,t_r,f_r,dt)

def main():
    Hanoi(3,"From Axis","To Axis","Auxiliary Axis",dt)
    for i in dt:
        print("\n%s =\t\t%d times"%(i,dt[i]),end="")


if __name__ == '__main__':
    main()
