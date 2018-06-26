import math
import copy
def ball_in_box(m,blockers):
    x=[]
    y=[]
    circles=[]
    already=[]
    for blocker in blockers:
        if blocker[0] not in x:
            x.append(blocker[0])
        if blocker[1] not in y:
            y.append(blocker[1])
    x.append(-1)
    x.append(1)
    y.append(-1)
    y.append(1)
    x.sort()
    y.sort()
    print(x)
    print(y)
    for j in range(len(y)-1):
        for i in range(len(x)-1):
            running=True
            for box in already:
                if box[0][0]<=x[i] and x[i]<box[-1][0] and box[0][1]<=y[j] and y[j]<box[-1][1]:
                    running=False
                    break
            if running:
                c0=((x[i+1]+x[i])/2.0,(y[j+1]+y[j])/2.0,min(x[i+1]-x[i],y[j+1]-y[j])/2.0)
                lim=[(x[i],y[j]),(x[i+1],y[j+1])]
                print('add1 circles',c0,circles)
                circles.append(c0)
                print('add2 already',lim,already)
                limx=lim.copy()
                already.append(limx)
                while running:
                    add=False
                    if  (lim[-1][0]-lim[0][0])>(lim[-1][1]-lim[0][1]):
                        for j0 in range(len(y)):
                            if y[j0]>lim[-1][1]:
                                add=True
                                lim[-1]=(lim[-1][0],y[j0])
                                c1=((lim[0][0]+lim[-1][0])/2.0,(lim[0][1]+lim[-1][1])/2.0,min(lim[-1][0]-lim[0][0],lim[-1][1]-lim[0][1])/2.0)
                                for blocker in blockers:
                                    if (blocker[0]-c1[0])**2+(blocker[1]-c1[1])**2<c1[2]**2:
                                        add=False
                                        break
                                break
                    else:
                        for i0 in range(len(x)):
                            if x[i0]>lim[-1][0]:
                                add=True
                                lim[-1]=(x[i0],lim[-1][1])
                                c1=((lim[0][0]+lim[-1][0])/2.0,(lim[0][1]+lim[-1][1])/2.0,min(lim[-1][0]-lim[0][0],lim[-1][1]-lim[0][1])/2.0)
                                for blocker in blockers:
                                    if (blocker[0]-c1[0])**2+(blocker[1]-c1[1])**2<c1[2]**2:
                                        add=False
                                        break
                                break
                    if add:
                        print('del3 circles',circles[-1],circles)
                        del circles[-1]
                        print('add4 circles',c1,circles)
                        circles.append(c1)
                        print('del5 already',already[-1],already)
                        del already[-1]
                        print('add6 already',lim,already)
                        limx=lim.copy()
                        already.append(limx)
                    else:
                        running=False
    print('already:',already)
    circles0=[]
    print(circles)
    for k in range(m):
        biggest=circles[0]
        biggestindex=0
        for k in range(1,len(circles)):
            if circles[k][2]>biggest[2]:
                biggestindex=k
                biggest=circles[k]
        circles0.append(circles[biggestindex])
        del circles[biggestindex]
    return circles0
ex=[(0.5,0.5),(0.5,-0.5),(0.5,0.3)]
print(ex)
os=ball_in_box(5,ex)
print(os)
mul=0
for circles in os:
    mul=math.pi*circles[2]**2+mul
print(mul)
print(mul/4)
