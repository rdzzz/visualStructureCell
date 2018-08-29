# -*- coding: utf-8 -*-
#重要提醒:本程序需要安装numpy库,文件名为numpy-1.8.0-win32-superpack-python2.7,exe,请从官方网站下载.
import numpy as np
import math
from Tkinter import *
import ttk

class Draw:
    def __init__(self,root):
        """ maininfo=(lattice_type=self.v.get(), crystal_constant=self.a, mode=[self.mode1,self.mode2],
        rotate_angle=self.rotate_angle,rotate_direction=self.direction,rotate_mode=self.rotate_mode,
        r_circle=self.r_circle)
        """
        self.root=root               #根窗口
        self.cv=None
        self.latticetype=None     
        self.a=None                  
        self.r=None
        self.r2=None
        self.axis=None             
        self.angle=None             
        self.circles=None
        self.lines=None
        self.r_circle=None         
        self.circle_color1=None
        self.circle_color2=None
        self.color2=None
        self.color3=None
        self.color4=None
        self.color5=None

        self.kkkk_s1=[]   #遮住的点的序号
        self.kkkk_s2=[]
        self.kdict={0:[8,9,10],1:[8,9,13],2:[8,12,13],3:[8,10,12],
                        4:[9,10,11],5:[9,11,13],6:[11,12,13],7:[10,11,12]}
        self.kdict2={0:[0,3,8],1:[0,1,9],2:[1,2,10],3:[2,3,11],
                     4:[4,7,8],5:[4,5,9],6:[5,6,10],7:[6,7,11]}
        self.kkk_vector=np.array((4,math.sqrt(2),math.sqrt(2)),dtype=np.float)
        self.kdict3={(8,9,10):0,(8,9,13):1,(8,12,13):2,(8,12,10):3,
                     (11,9,10):4,(11,9,13):5,(11,12,13):6,(11,12,10):7}
    def run(self,cv,m):
        self.cv=cv                   #画布(GUI中已经建立好了)
        self.latticetype=m['lattice_type']        #点阵类型(共14种)
        self.a=m['crystal_constant']                  #晶胞边长
        self.r=np.array([0,200])   #三维坐标轴(或二维投影坐标轴)原点0在画布上面的坐标
        self.r2=np.array([0,450])
        self.axis=m['rotate_direction']             #旋转轴
        self.angle=m['rotate_angle']*math.pi/180                #旋转角度
        self.circles=m['circles']
        self.lines=m['lines']
        self.r_circle=m['r_circle']          #点阵上面点的半径
        rx=self.r[0]                                          #建立并画出三维坐标系
        ry=self.r[1]
        self.circle_color1=m['circle_color1']
        self.circle_color2=m['circle_color2']

        color1=m['color1']
        self.color2=m['color2']
        self.color3=m['color3']
        self.color4=m['color4']
        self.color5=m['color5']
        
        self.cv.create_line(rx,ry,rx+150,ry,arrow=LAST,fill=color1)  
        self.cv.create_line(rx,ry,rx-53,ry+53,arrow=LAST,fill=color1)
        self.cv.create_line(rx,ry,rx,ry-150,arrow=LAST,fill=color1)
        rx2=self.r2[0]                                          #建立并画出三维坐标系
        ry2=self.r2[1]
        self.cv.create_line(rx2,ry2,rx2+150,ry2,arrow=LAST,fill=color1)  
        self.cv.create_line(rx2,ry2,rx2-53,ry2+53,arrow=LAST,fill=color1)
        self.cv.create_line(rx2,ry2,rx2,ry2-150,arrow=LAST,fill=color1)

    def rotation(self):
        a=self.angle
        if self.axis=='z':
            C=np.array([[math.cos(a),-math.sin(a),0],[math.sin(a),math.cos(a),0],[0,0,1]],dtype=np.float)
            #yaw 角，和右手螺旋的方向相反,见wikipedia旋转矩阵(http://zh.wikipedia.org/wiki/%E6%97%8B%E8%BD%AC%E7%9F%A9%E9%98%B5)        
        elif self.axis=='x':
            C=np.array([[1,0,0],[0,math.cos(a),-math.sin(a)],[0,math.sin(a),math.cos(a)]],dtype=np.float)
            #roll 角，和右手螺旋的方向一致
        elif self.axis=='y':
            C=np.array([[math.cos(a),0,math.sin(a)],[0,1,0],[-math.sin(a),0,math.cos(a)]],dtype=np.float)
            #pitch 角，和右手螺旋的方向相反
        else:
            C=np.array([[1,0,0],[0,1,0],[0,0,1]],dtype=np.float)
        self.clean(self.circles,self.lines)
        return C
            #坐标变换矩阵C


    def LatticeType(self):
        root=self.root
        s=self.latticetype
        
        top=Toplevel()
        top.title(u'请输入数据')
        v1=StringVar()
        v1.set(1)
        v2=StringVar()
        v2.set(1)
        v3=StringVar()
        v3.set(1)
        v4=StringVar()
        v4.set(90)
        v5=StringVar()
        v5.set(90)
        v6=StringVar()
        v6.set(90)
        l1=Label(top,text='')
        e1=Entry(top,textvariable=v1)
        l2=Label(top,text='')
        e2=Entry(top,textvariable=v2)
        l3=Label(top,text='')
        e3=Entry(top,textvariable=v3)
        l4=Label(top,text='')
        e4=Entry(top,textvariable=v4)
        l5=Label(top,text='')
        e5=Entry(top,textvariable=v5)
        l6=Label(top,text='')
        e6=Entry(top,textvariable=v6)
        Button(top,text=u'完成',command=top.quit).grid(row=7,column=2)
    
        if s=='simpleCubic' or s=='bcc' or s=='fcc':
            l1.config(text=u'请输入立方晶系三边的边长')
            l1.grid(row=1,column=1)
            e1.grid(row=1,column=2)
            top.mainloop()
            top.destroy()
            a=v1.get()
            a=eval(a)
            lattices=self.cubic(a)
        elif s=='primitiveTetragonal' or s=='body-centeredTetragonal':
            l1.config(text=u'请输入四方晶系的高,底面边长为1')
            l1.grid(row=1,column=1)
            e1.grid(row=1,column=2)
            top.mainloop()
            top.destroy()
            c=v1.get()
            c=eval(c)
            #c=input('请输入四方晶系的高,底面边长为1')
            lattices=self.tetragonal(c)
        elif s=='primitiveOrthorhombic' or s=='body-centeredOrthorhombic' or s=='base-centeredOrthorhombic' or s=='face-centeredOrthorhombic':
            l1.config(text=u'输入正交晶系的长')
            l2.config(text=u'输入正交晶系的宽')
            l3.config(text=u'输入正交晶系的高')
            l1.grid(row=1,column=1)
            e1.grid(row=1,column=2)
            l2.grid(row=2,column=1)
            e2.grid(row=2,column=2)
            l3.grid(row=3,column=1)
            e3.grid(row=3,column=2)
            top.mainloop()
            top.destroy()
            a=v1.get()
            b=v2.get()
            c=v3.get()
            a=eval(a)
            b=eval(b)
            c=eval(c)
            """
            a=input('输入正交晶系的长')
            b=input('输入正交晶系的宽')
            c=input('输入正交晶系的高')
            """
            lattices=self.orthorhombic(a,b,c)
        elif s=='primitiveMonoclinic' or s=='base-centeredMonoclinic':
            l1.config(text=u'输入单斜晶系的长')
            l2.config(text=u'输入单斜晶系的宽')
            l3.config(text=u'输入单斜晶系的高')
            l4.config(text=u'请输入单斜晶系底边夹角')
            l1.grid(row=1,column=1)
            e1.grid(row=1,column=2)
            l2.grid(row=2,column=1)
            e2.grid(row=2,column=2)
            l3.grid(row=3,column=1)
            e3.grid(row=3,column=2)
            l4.grid(row=4,column=1)
            e4.grid(row=4,column=2)
            top.mainloop()
            top.destroy()
            a=v1.get()
            b=v2.get()
            c=v3.get()
            beta=v4.get()
            a=eval(a)
            b=eval(b)
            c=eval(c)
            beta=eval(beta)
            """
            a=input('输入单斜晶系的长')
            b=input('输入单斜晶系的宽')
            c=input('输入单斜晶系的高')
            beta=input('请输入单斜晶系底边夹角')
            """
            beta=beta*math.pi/180
            lattices=self.monoclinic(a,b,c,beta)
        elif s=='triclinic':
            l1.config(text=u'输入三斜晶系的长')
            l2.config(text=u'输入三斜晶系的宽')
            l3.config(text=u'输入三斜晶系的高')
            l4.config(text=u'输入三斜晶系长和高的夹角')
            l5.config(text=u'输入三斜晶系宽和高的夹角')
            l6.config(text=u'输入三斜晶系长和宽的夹角')
            l1.grid(row=1,column=1)
            e1.grid(row=1,column=2)
            l2.grid(row=2,column=1)
            e2.grid(row=2,column=2)
            l3.grid(row=3,column=1)
            e3.grid(row=3,column=2)
            l4.grid(row=4,column=1)
            e4.grid(row=4,column=2)
            l5.grid(row=5,column=1)
            e5.grid(row=5,column=2)
            l6.grid(row=6,column=1)
            e6.grid(row=6,column=2)
        
            top.mainloop()
            top.destroy()
            a=v1.get()
            b=v2.get()
            c=v3.get()
            alpha=v4.get()
            beta=v5.get()
            gamma=v6.get()
            a=eval(a)
            b=eval(b)
            c=eval(c)
            alpha=eval(alpha)
            beta=eval(beta) 
            gamma=eval(gamma)
            """
            a=input('输入三斜晶系的长')
            b=input('输入三斜晶系的宽')
            c=input('输入三斜晶系的高')
            alpha=input('输入三斜晶系长和高的夹角')
            beta=input('输入三斜晶系宽和高的夹角')
            gamma=input('输入三斜晶系长和宽的夹角')
            """
            alpha=alpha*math.pi/180
            beta=beta*math.pi/180
            gamma=gamma*math.pi/180
            lattices=self.triclinic(a,b,c,alpha,beta,gamma)
        elif s=='rhombohedral':
            l1.config(text=u'输入棱方晶系的长')
            l2.config(text=u'输入棱方晶系的宽')
            l3.config(text=u'输入棱方晶系的高')
            l4.config(text=u'请输入棱方晶系底边夹角')
            l1.grid(row=1,column=1)
            e1.grid(row=1,column=2)
            l2.grid(row=2,column=1)
            e2.grid(row=2,column=2)
            l3.grid(row=3,column=1)
            e3.grid(row=3,column=2)
            l4.grid(row=4,column=1)
            e4.grid(row=4,column=2)
            top.mainloop()
            top.destroy()
            a=v1.get()
            b=v2.get()
            c=v3.get()
            alpha=v4.get()
            a=eval(a)
            b=eval(b)
            c=eval(c)
            alpha=eval(alpha) 
            
            #a=input('输入棱方晶系的长')
            #b=input('输入棱方晶系的宽')
            #c=input('输入棱方晶系的高')
            #alpha=input(u'输入棱方晶系边的夹角')
            alpha=alpha*math.pi/180
        
            lattices=self.triclinic(a,b,c,alpha,alpha,alpha)
        elif s=='hexagonal':
            top.destroy()
            lattices=self.hexagonal()
            
        self.clean(self.circles,self.lines)
        self.kkkk_s1=self.kkk(lattices)
        return lattices

    def cubic(self,a):
        A1=a*np.array((0,0,0),dtype=np.float) #简单立方八个点的坐标
        A2=a*np.array((1,0,0),dtype=np.float)
        A3=a*np.array((1,1,0),dtype=np.float)
        A4=a*np.array((0,1,0),dtype=np.float)
        A5=a*np.array((0,0,1),dtype=np.float)
        A6=a*np.array((1,0,1),dtype=np.float)
        A7=a*np.array((1,1,1),dtype=np.float)
        A8=a*np.array((0,1,1),dtype=np.float)
        if self.latticetype=='simpleCubic':
            lattices0=[A1,A2,A3,A4,A5,A6,A7,A8]
            return lattices0

        A15=a*np.array((0.5,0.5,0.5)) #体心立方体心
        if self.latticetype=='bcc':
            lattices0=[A1,A2,A3,A4,A5,A6,A7,A8,A15]
            return lattices0

        A9=a*np.array((0.5,0.5,0)) #面心立方面心
        A12=a*np.array((0.5,0.5,1))
        A10=a*np.array((0.5,0,0.5))
        A13=a*np.array((0.5,1,0.5))
        A11=a*np.array((0,0.5,0.5))
        A14=a*np.array((1,0.5,0.5))
        if self.latticetype=='fcc':
            lattices0=[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14]
            return lattices0
    def tetragonal(self,c):
        A1=np.array((0,0,0),dtype=np.float) #四方晶系
        A2=np.array((1,0,0),dtype=np.float)
        A3=np.array((1,1,0),dtype=np.float)
        A4=np.array((0,1,0),dtype=np.float)
        A5=np.array((0,0,c),dtype=np.float)
        A6=np.array((1,0,c),dtype=np.float)
        A7=np.array((1,1,c),dtype=np.float)
        A8=np.array((0,1,c),dtype=np.float)
        if self.latticetype=='primitiveTetragonal':
            lattices0=[A1,A2,A3,A4,A5,A6,A7,A8]
            return lattices0
        A15=np.array((0.5,0.5,0.5*c)) #体心四方
        if self.latticetype=='body-centeredTetragonal':
            lattices0=[A1,A2,A3,A4,A5,A6,A7,A8,A15]
            return lattices0

    def orthorhombic(self,a,b,c):
        A1=np.array((0,0,0),dtype=np.float) #立方晶系
        A2=np.array((a,0,0),dtype=np.float)
        A3=np.array((a,b,0),dtype=np.float)
        A4=np.array((0,b,0),dtype=np.float)
        A5=np.array((0,0,c),dtype=np.float)
        A6=np.array((a,0,c),dtype=np.float)
        A7=np.array((a,b,c),dtype=np.float)
        A8=np.array((0,b,c),dtype=np.float)
        if self.latticetype=='primitiveOrthorhombic':
            lattices0=[A1,A2,A3,A4,A5,A6,A7,A8]
            return lattices0
        A9=np.array((0.5*a,0.5*b,0),dtype=np.float)
        A12=np.array((0.5*a,0.5*b,c),dtype=np.float)
        if self.latticetype=='base-centeredOrthorhombic':
            lattices0=[A1,A2,A3,A4,A5,A6,A7,A8,A9,A12]
            return lattices0
        A15=np.array((0.5*a,0.5*b,0.5*c),dtype=np.float)
        if self.latticetype=='body-centeredOrthorhombic':
            lattices0=[A1,A2,A3,A4,A5,A6,A7,A8,A15]
            return lattices0
        A10=np.array((0.5*a,0,0.5*c))
        A13=np.array((0.5*a,b,0.5*c))
        A11=np.array((0,0.5*b,0.5*c))
        A14=np.array((a,0.5*b,0.5*c))
        if self.latticetype=='face-centeredOrthorhombic':
            lattices0=[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14]
            return lattices0
    def monoclinic(self,a,b,c,d):
        bx=b*math.cos(d)
        by=b*math.sin(d)
        A1=np.array((0,0,0),dtype=np.float) #单斜晶系
        A2=np.array((a,0,0),dtype=np.float)
        A3=np.array((a+bx,by,0),dtype=np.float)
        A4=np.array((bx,by,0),dtype=np.float)
        A5=np.array((0,0,c),dtype=np.float)
        A6=np.array((a,0,c),dtype=np.float)
        A7=np.array((a+bx,by,c),dtype=np.float)
        A8=np.array((bx,by,c),dtype=np.float)
        if self.latticetype=='primitiveMonoclinic':
            lattices0=[A1,A2,A3,A4,A5,A6,A7,A8] 
            return lattices0
        A9=np.array((0.5*(a+bx),0.5*by,0))
        A12=np.array((0.5*(a+bx),0.5*by,c))
        if self.latticetype=='base-centeredMonoclinic':
            lattices0=[A1,A2,A3,A4,A5,A6,A7,A8,A9,A12]
            return lattices0
    def triclinic(self,a,b,c,d,e,f):
        bx=b*math.cos(f)
        by=b*math.sin(f)
        cx=c*math.cos(e)
        cy=c*(math.cos(d)-math.cos(e)*math.cos(f)/math.sin(f))
        cz=c*math.sqrt(1-math.cos(d)*math.cos(d)-math.cos(e)*math.cos(e)-math.cos(f)*math.cos(f)+2*math.cos(d)*math.cos(e)*math.cos(f))/math.sin(f)
        A1=np.array((0,0,0),dtype=np.float) #三斜晶系以及棱方晶系
        A2=np.array((a,0,0),dtype=np.float)
        A3=np.array((a+bx,by,0),dtype=np.float)
        A4=np.array((bx,by,0),dtype=np.float)
        A5=np.array((cx,cy,cz),dtype=np.float)
        A6=np.array((a+cx,cy,cz),dtype=np.float)
        A7=np.array((a+bx+cx,by+cy,cz),dtype=np.float)
        A8=np.array((bx+cx,by+cy,cz),dtype=np.float)
        lattices0=[A1,A2,A3,A4,A5,A6,A7,A8]    
        return lattices0
    def hexagonal(self):    #六方晶系
        by=math.sqrt(3)/2
        A1=np.array((0,0,0),dtype=np.float) 
        A2=np.array((1,0,0),dtype=np.float)
        A3=np.array((0.5,by,0),dtype=np.float)
        A4=np.array((-0.5,by,0),dtype=np.float)
        A5=np.array((0,0,1.633),dtype=np.float)
        A6=np.array((1,0,1.633),dtype=np.float)
        A7=np.array((0.5,by,1.633),dtype=np.float)
        A8=np.array((-0.5,by,1.633),dtype=np.float)
        lattices0=[A1,A2,A3,A4,A5,A6,A7,A8]    
        return lattices0
    def lattice(self,lattices0,deltaR):
        lattices=[]
        for i in range(len(lattices0)):
            lattices=lattices+[np.dot(deltaR,lattices0[i])]#获得旋转后立方体的坐标

        self.kkkk_s1=self.kkk(lattices)
        
        return lattices
    def lattice2(self,lattices0,deltaR):
        lattices=[]
        for i in range(len(lattices0)):
            lattices=lattices+[np.dot(deltaR,lattices0[i])]#获得旋转后立方体的坐标

        self.kkkk_s2=self.kkk2(lattices)
        
        return lattices
    def project(self,lattices,r):
        Z=np.array([-math.sqrt(2)/4,-math.sqrt(2)/4])#正等轴画法,x方向坐标变成(-0.35,-0.35)的倍数
        points=[]
        k=np.array([[1,0],[0,-1]]) #画布中，纵坐标异号
        for i in range(len(lattices)):
            m=lattices[i]*self.a
            s=m[[1,2]]+m[0]*Z
            s=np.dot(k,s)
            s=s+r
            points=points+[s]
        return points      #points中含有正等轴画法画出来的点的坐标
    def reciprocalLattice(self,p): #倒易空间
        s=self.latticetype
        result=[]
        if (s=='simpleCubic' or s=='primitiveTetragonal' or s=='primitiveOrthorhombic' or s=='primitiveMonoclinic'
           or s=='triclinic' or s=='rhombohedral' or s=='hexagonal'):
            a1=p[1]
            a3=p[3]
            a4=p[4]
            V=np.array([a1,a3,a4])
            v=np.linalg.det(V)
            b0=np.array((0,0,0),dtype=np.float)
            b1=1.0*np.cross(a3,a4)/v
            b3=1.0*np.cross(a4,a1)/v
            b4=1.0*np.cross(a1,a3)/v
            b2=b1+b3
            b5=b1+b4
            b7=b3+b4
            b6=b1+b3+b4
            result=[b0,b1,b2,b3,b4,b5,b6,b7]
        elif s=='bcc' or s=='body-centeredTetragonal' or s=='body-centeredOrthorhombic': #体心立方的倒易点阵是面心立方
            a=p[8]
            A1=a-p[1]
            A2=a-p[3]
            A3=a-p[4]
            V=np.array([A1,A2,A3])
            v=np.linalg.det(V)
            b10=1.0*np.cross(A2,A3)/v
            b9=1.0*np.cross(A3,A1)/v
            b8=1.0*np.cross(A1,A2)/v
            b0=np.array((0,0,0),dtype=np.float)
            b1=b8+b9-b10
            b3=b8+b10-b9
            b4=b9+b10-b8
            b2=b1+b3
            b5=b1+b4
            b7=b3+b4
            b6=b1+b3+b4
            b11=b9+b10
            b12=b8+b10
            b13=b8+b9
            result=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13]
            
        elif s=='fcc' or s=='face-centeredOrthorhombic': #面心立方的倒易点阵是体心立方，所以只需要求出一个体心的坐标即可
            A1=p[10]
            A2=p[9]
            A3=p[8]
            V=np.array([A1,A2,A3])
            v=np.linalg.det(V)
            b=1.0*np.cross(A2,A3)/v
            k=np.array([[-1,0,0],[0,1,0],[0,0,1]],dtype=np.float)
            b15=np.dot(b,k)
            b1=np.array((2*b15[0],0,0))
            b3=np.array((0,2*b15[1],0))
            b4=np.array((0,0,2*b15[2]))
            b2=b1+b3
            b5=b1+b4
            b7=b3+b4
            b6=2*b15
            b0=np.array((0,0,0),dtype=np.float)
            result=[b0,b1,b2,b3,b4,b5,b6,b7,b15]       
            
        elif s=='base-centeredOrthorhombic' or s=='base-centeredMonoclinic':
            A1=p[8]
            A3=p[4]
            A2=A1-p[3]
            V=np.array([A1,A2,A3])
            v=np.linalg.det(V)
            b8=1.0*np.cross(A2,A3)/v
            b=1.0*np.cross(A3,A1)/v
            b4=1.0*np.cross(A1,A2)/v
            b1=b8+b
            b3=b8-b
            b2=b1+b3
            b5=b1+b4
            b7=b3+b4
            b0=np.array((0,0,0),dtype=np.float)
            b6=b1+b4+b3
            b11=b8+b4
            result=[b0,b1,b2,b3,b4,b5,b6,b7,b8,b11]
            
        self.kkkk_s2=self.kkk2(result)
        
        return result
    def kkk(self,m):
        s=self.latticetype
        self.kkk_vector
        a1=m[1]
        a3=m[3]
        a4=m[4]
        mk=[]
        m8=np.cross(a3,a1)
        m9=np.cross(a1,a4)
        m10=np.cross(a4,a3)
        if np.dot(self.kkk_vector,m8)<0:
            mk+=[8]
        else:
            mk+=[11]
        if np.dot(self.kkk_vector,m9)<0:
            mk+=[9]
        else:
            mk+=[12]
        if np.dot(self.kkk_vector,m10)<0:
            mk+=[10]
        else:
            mk+=[13]
        mk=tuple(mk)
        kkkk_s=[self.kdict3[mk]]
        if s=='bcc' or s=='body-centeredTetragonal' or s=='body-centeredOrthorhombic':
            kkkk_s+=[8]
        elif s=='base-centeredOrthorhombic' or s=='base-centeredMonoclinic':
            if 8 in mk:
                kkkk_s+=[8]
            else:
                kkkk_s+=[9]       
        elif s=='fcc' or s=='face-centeredOrthorhombic':
            kkkk_s+=self.kdict[kkkk_s[0]]
        return kkkk_s
    def kkk2(self,m):
        s=self.latticetype
        self.kkk_vector
        a1=m[1]
        a3=m[3]
        a4=m[4]
        mk=[]
        m8=np.cross(a3,a1)
        m9=np.cross(a1,a4)
        m10=np.cross(a4,a3)
        if np.dot(self.kkk_vector,m8)<0:
            mk+=[8]
        else:
            mk+=[11]
        if np.dot(self.kkk_vector,m9)<0:
            mk+=[9]
        else:
            mk+=[12]
        if np.dot(self.kkk_vector,m10)<0:
            mk+=[10]
        else:
            mk+=[13]
        mk=tuple(mk)
        kkkk_s=[self.kdict3[mk]]
        if s=='fcc' or s=='face-centeredOrthorhombic':
            kkkk_s+=[8]
        elif s=='base-centeredOrthorhombic' or s=='base-centeredMonoclinic':
            if 8 in mk:
                kkkk_s+=[8]
            else:
                kkkk_s+=[9]     
        elif s=='bcc' or s=='body-centeredTetragonal' or s=='body-centeredOrthorhombic':
            kkkk_s+=self.kdict[kkkk_s[0]]
        return kkkk_s
        
    def main(self,points):
        r_circle=self.r_circle
        
        root=self.root
        cv=self.cv
        if True :
            p=[]
            for i in range(len(points)): #将矩阵提取到列表p中,p中元素为元组(坐标)
                point=points[i]
                p=p+[(point[0],point[1])]
            r1=cv.create_line(p[0],p[1])
            r2=cv.create_line(p[1],p[2])
            r3=cv.create_line(p[2],p[3])
            r4=cv.create_line(p[3],p[0])
            r5=cv.create_line(p[4],p[5])
            r6=cv.create_line(p[5],p[6])
            r7=cv.create_line(p[6],p[7])
            r8=cv.create_line(p[7],p[4])
            r9=cv.create_line(p[0],p[4])
            r10=cv.create_line(p[1],p[5])
            r11=cv.create_line(p[2],p[6])
            r12=cv.create_line(p[3],p[7])
            lines=[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12]
            for i in self.kdict2[self.kkkk_s1[0]]:
                cv.itemconfig(lines[i],fill=self.color4,dash=(4,4))
                cv.lower(lines[i])
            circles=[]
            for i in p:
                m=cv.create_oval(i[0]-r_circle,i[1]-r_circle,i[0]+r_circle,i[1]+r_circle,fill=self.circle_color1)
                circles=circles+[m]
            for i in self.kkkk_s1:
                cv.itemconfig(circles[i],fill=self.color4)
                cv.lower(circles[i])
            cv.lower(circles[self.kkkk_s1[0]])
        
            if self.latticetype=='bcc' or self.latticetype=='body-centeredTetragonal' or self.latticetype=='body-centeredOrthorhombic':
                cv.create_line(p[0],p[6],dash=(2,4),tags="#1",fill=self.color2)
                cv.create_line(p[3],p[5],dash=(2,4),tags="#1",fill=self.color2)
                cv.create_line(p[7],p[1],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[4],p[2],dash=(2,4),tags='#1',fill=self.color2)
                lines=lines+['#1']
                #cv.itemconfig(circles[8],fill='blue')
            elif self.latticetype=='fcc' or self.latticetype=='face-centeredOrthorhombic':
                cv.create_line(p[0],p[2],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[1],p[3],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[4],p[6],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[5],p[7],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[2],p[7],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[3],p[6],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[1],p[4],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[0],p[5],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[1],p[6],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[2],p[5],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[3],p[4],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[0],p[7],dash=(2,4),tags='#1',fill=self.color2)
                lines=lines+['#1']
            elif self.latticetype=='base-centeredOrthorhombic' or self.latticetype=='base-centeredMonoclinic':
                cv.create_line(p[0],p[2],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[1],p[3],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[4],p[6],dash=(2,4),tags='#1',fill=self.color2)
                cv.create_line(p[5],p[7],dash=(2,4),tags='#1',fill=self.color2)
                lines=lines+['#1']
            return circles,lines
    def main2(self,points):
        r_circle=self.r_circle
        
        root=self.root
        cv=self.cv
        if True :      
            p=[]
            for i in range(len(points)): #将矩阵提取到列表p中,p中元素为元组(坐标)
                point=points[i]
                p=p+[(point[0],point[1])]
            r1=cv.create_line(p[0],p[1])
            r2=cv.create_line(p[1],p[2])
            r3=cv.create_line(p[2],p[3])
            r4=cv.create_line(p[3],p[0])
            r5=cv.create_line(p[4],p[5])
            r6=cv.create_line(p[5],p[6])
            r7=cv.create_line(p[6],p[7])
            r8=cv.create_line(p[7],p[4])
            r9=cv.create_line(p[0],p[4])
            r10=cv.create_line(p[1],p[5])
            r11=cv.create_line(p[2],p[6])
            r12=cv.create_line(p[3],p[7])
            lines=[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12]
            circles=[]
            for i in p:
                m=cv.create_oval(i[0]-r_circle,i[1]-r_circle,i[0]+r_circle,i[1]+r_circle,fill=self.circle_color2)
                circles=circles+[m]
            for i in self.kkkk_s2:
                cv.itemconfig(circles[i],fill=self.color5)
                cv.lower(circles[i])
            cv.lower(circles[self.kkkk_s2[0]])
            for i in self.kdict2[self.kkkk_s2[0]]:
                cv.itemconfig(lines[i],fill=self.color5,dash=(4,4))
                cv.lower(lines[i])
        
            if self.latticetype=='fcc' or self.latticetype=='face-centeredOrthorhombic':
                cv.create_line(p[0],p[6],dash=(2,4),tags="#2",fill=self.color3)
                cv.create_line(p[3],p[5],dash=(2,4),tags="#2",fill=self.color3)
                cv.create_line(p[7],p[1],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[4],p[2],dash=(2,4),tags='#2',fill=self.color3)
                lines=lines+['#2']
            elif self.latticetype=='bcc' or self.latticetype=='body-centeredTetragonal' or self.latticetype=='body-centeredOrthorhombic':
                cv.create_line(p[0],p[2],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[1],p[3],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[4],p[6],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[5],p[7],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[2],p[7],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[3],p[6],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[1],p[4],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[0],p[5],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[1],p[6],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[2],p[5],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[3],p[4],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[0],p[7],dash=(2,4),tags='#2',fill=self.color3)
                lines=lines+['#2']
            elif self.latticetype=='base-centeredOrthorhombic' or self.latticetype=='base-centeredMonoclinic':
                cv.create_line(p[0],p[2],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[1],p[3],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[4],p[6],dash=(2,4),tags='#2',fill=self.color3)
                cv.create_line(p[5],p[7],dash=(2,4),tags='#2',fill=self.color3)
                lines=lines+['#2']
            return circles,lines
    def clean(self,circles,lines):
        for i in lines:
            self.cv.delete(i)
        for i in circles:
            self.cv.delete(i)
class GUI:
    def __init__(self,root):
        self.root=root

        self.k1=StringVar()
        self.k1.set('80')
        self.a=eval(self.k1.get())
        
        self.gFlag=False
        self.mode1=True    #普通作图
        
        self.menu()
        self.title()
        
        self.mode2=False   #旋转

        self.k3=StringVar()
        self.k3.set('5')
        self.rotate_angle0=eval(self.k3.get())#旋转角度大小(°)
        self.rotate_angle=self.rotate_angle0
        self.direction=None  #旋转方向(轴)
        self.rotate_mode=None
        self.mainifo={}
        
        self.k2=StringVar()
        self.k2.set('8')
        self.r_circle=eval(self.k2.get())
        self.settingc=None

        self.k4=StringVar()
        self.k4.set(u'red')
        self.color1=self.k4.get()
        
        self.k5=StringVar()
        self.k5.set('black')
        self.circle_color1=self.k5.get()

        self.k6=StringVar()
        self.k6.set('black')
        self.circle_color2=self.k6.get()

        self.k7=StringVar()
        self.k7.set('black')
        self.color2=self.k7.get()

        self.k8=StringVar()
        self.k8.set('black')
        self.color3=self.k8.get()

        self.k9=StringVar()
        self.k9.set('blue')
        self.color4=self.k9.get()

        self.k10=StringVar()
        self.k10.set('blue')
        self.color5=self.k10.get()
        
        Label(self.root,text=u'实际空间').grid(row=30,column=11,columnspan=8)
        Label(self.root,text=u'按"WASD"和"QE"键有惊喜哦!').grid(row=31,column=11,columnspan=8)
        self.f9=Frame(self.root,bd=4,relief='groove')
        self.f9.grid(row=31,column=11,rowspan=8,columnspan=8)
        Label(self.root,text=u'倒易空间').grid(row=40,column=11,columnspan=8)
        Label(self.root,text=u'按方向键和"ZX"键有惊喜哦').grid(row=41,column=11,columnspan=8)
        self.f10=Frame(self.root,bd=4,relief='groove')
        self.f10.grid(row=41,column=11,rowspan=8,columnspan=8)
        self.rotateBuild()
        
        self.v=StringVar()
        self.v.set(u'simpleCubic')
        self.getType()
        
        self.cv=Canvas(root,width=400,height=400,scrollregion=(-300,-100,300,800),bg='white')
        self.cv.grid(row=31,column=21,rowspan=20,columnspan=20)
        self.f11=Frame(self.root,bd=4,relief='groove')
        self.f11.grid(row=1,column=11)
        Label(self.f11,text=u'按F1键可以进入设置').grid(row=1,column=1)
        
        self.scrollX=Scrollbar(self.root,orient='horizontal',command=self.cv.xview)
        self.scrollX.grid(row=51,column=21,columnspan=20,sticky=W+E)
        self.cv['xscrollcommand']=self.scrollX.set
        self.scrollY=Scrollbar(self.root,orient='vertical',command=self.cv.yview)
        self.scrollY.grid(row=31,rowspan=20,column=41,sticky=N+S)
        self.cv['yscrollcommand']=self.scrollY.set

        def resettingsF1(event):
            if not self.settingc:
                self.settings()
            else:
                self.settingc.destroy()
                self.settingc=None
        self.root.bind_all('<F1>',resettingsF1)
        self.root.bind('w',self.up11)
        self.root.bind('s',self.down11)
        self.root.bind('a',self.left11)
        self.root.bind('d',self.right11)
        self.root.bind('q',self.counterclockwise11)
        self.root.bind('e',self.clockwise11)
        self.root.bind('<Up>',self.up22)
        self.root.bind('<Down>',self.down22)
        self.root.bind('<Left>',self.left22)
        self.root.bind('<Right>',self.right22)
        self.root.bind('z',self.counterclockwise22)
        self.root.bind('x',self.clockwise22)
    def getType(self):
        f1=Frame(self.root,bd=4,relief='groove')
        f1.grid(row=11,column=11,rowspan=10,columnspan=30,sticky=N)
        f2=Frame(f1,bd=3,relief='groove')
        f2.grid(row=0,rowspan=8,column=2,sticky=N)
        Label(f2,text=u'立方晶系').grid(column=0,row=0)
        f3=Frame(f1,bd=3,relief='groove')
        f3.grid(row=0,rowspan=8,column=3,sticky=N)
        Label(f3,text=u'正交晶系').grid(column=0,row=0)
        f4=Frame(f1,bd=3,relief='groove')
        f4.grid(row=0,rowspan=8,column=4,sticky=N)
        Label(f4,text=u'四方晶系').grid(column=0,row=0)
        f5=Frame(f1,bd=3,relief='groove')
        f5.grid(row=0,rowspan=8,column=5,sticky=N)
        Label(f5,text=u'单斜晶系').grid(column=0,row=0)
        f6=Frame(f1,bd=3,relief='groove')
        f6.grid(row=0,rowspan=8,column=6,sticky=N)
        Label(f6,text=u'棱方晶系').grid(column=0,row=0)
        f7=Frame(f1,bd=3,relief='groove')
        f7.grid(row=0,rowspan=8,column=7,sticky=N)
        Label(f7,text=u'六方晶系').grid(column=0,row=0)
        f8=Frame(f1,bd=3,relief='groove')
        f8.grid(row=0,rowspan=8,column=8,sticky=N)
        Label(f8,text=u'三斜晶系').grid(column=0,row=0)
        Radiobutton(f2,text=u'简单立方晶胞',variable=self.v,value='simpleCubic').grid(row=1,column=0)
        Radiobutton(f2,text=u'体心立方晶胞',variable=self.v,value='bcc').grid(row=2,column=0)
        Radiobutton(f2,text=u'面心立方晶胞',variable=self.v,value='fcc').grid(row=3,column=0)
        Radiobutton(f4,text=u'简单四方晶胞',variable=self.v,value='primitiveTetragonal').grid(row=1,column=0)
        Radiobutton(f4,text=u'体心四方晶胞',variable=self.v,value='body-centeredTetragonal').grid(row=2,column=0)
        Radiobutton(f3,text=u'简单正交晶胞',variable=self.v,value='primitiveOrthorhombic' ).grid(row=1,column=0)
        Radiobutton(f3,text=u'体心正交晶胞',variable=self.v,value='body-centeredOrthorhombic').grid(row=2,column=0)
        Radiobutton(f3,text=u'底心正交晶胞',variable=self.v,value='base-centeredOrthorhombic').grid(row=3,column=0)
        Radiobutton(f3,text=u'面心正交晶胞',variable=self.v,value='face-centeredOrthorhombic').grid(row=4,column=0)
        Radiobutton(f5,text=u'简单单斜晶胞',variable=self.v,value='primitiveMonoclinic').grid(row=1,column=0)
        Radiobutton(f5,text=u'底心单斜晶胞',variable=self.v,value='base-centeredMonoclinic').grid(row=2,column=0)
        Radiobutton(f8,text=u'简单三斜晶胞',variable=self.v,value='triclinic').grid(row=1,column=0)
        Radiobutton(f6,text=u'简单棱方晶胞',variable=self.v,value='rhombohedral').grid(row=1,column=0)
        Radiobutton(f7,text=u'简单六方晶胞',variable=self.v,value='hexagonal').grid(row=1,column=0)
        Button(f1,text=u'完成',command=self.getLtype).grid(row=10,column=4)
    def rotateBuild(self):
        Button(self.f9,text=u'↑',command=self.up1).grid(row=9,column=1)
        Button(self.f9,text=u'↓',command=self.down1).grid(row=10,column=1)
        Button(self.f9,text=u'←',command=self.left1).grid(row=10,column=0)
        Button(self.f9,text=u'→',command=self.right1).grid(row=10,column=2)
        Button(self.f9,text=u'顺时针',command=self.clockwise1).grid(row=11,column=2)
        Button(self.f9,text=u'逆时针',command=self.counterclockwise1).grid(row=11,column=0)

        Button(self.f10,text=u'↑',command=self.up2).grid(row=12,column=1)
        Button(self.f10,text=u'↓',command=self.down2).grid(row=13,column=1)
        Button(self.f10,text=u'←',command=self.left2).grid(row=13,column=0)
        Button(self.f10,text=u'→',command=self.right2).grid(row=13,column=2)
        Button(self.f10,text=u'顺时针',command=self.clockwise2).grid(row=14,column=2)
        Button(self.f10,text=u'逆时针',command=self.counterclockwise2).grid(row=14,column=0)

        
        def reset():
            self.mode1=False
            self.mode2=True
            self.rotate_mode=0
            self.root.quit()

        Button(self.root,text=u'重置',command=reset).grid(row=50,column=11,columnspan=8)
    def up1(self):
        self.direction='y'
        self.rotate_mode=1
        self.rotate_angle=-self.rotate_angle0
        self.mode1=False
        self.mode2=True
        
        self.root.quit()
    def down1(self):
        self.direction='y'
        self.rotate_mode=1
        self.rotate_angle=self.rotate_angle0
        self.mode1=False
        self.mode2=True
        self.root.quit()
    def left1(self):
        self.direction='z'
        self.rotate_mode=1
        self.rotate_angle=-self.rotate_angle0
        self.mode1=False
        self.mode2=True
        self.root.quit()
    def right1(self):
        self.direction='z'
        self.rotate_mode=1
        self.rotate_angle=self.rotate_angle0
        self.mode1=False
        self.mode2=True
        self.root.quit()
    def clockwise1(self):
        self.direction='x'
        self.rotate_mode=1
        self.rotate_angle=-self.rotate_angle0
        self.mode1=False
        self.mode2=True
        self.root.quit()
    def counterclockwise1(self):
        self.direction='x'
        self.rotate_mode=1
        self.rotate_angle=self.rotate_angle0
        self.mode1=False
        self.mode2=True
        self.root.quit()
    def up2(self):
        self.up1()
        self.rotate_mode=2
    def down2(self):
        self.down1()
        self.rotate_mode=2
    def left2(self):
        self.left1()
        self.rotate_mode=2
    def right2(self):
        self.right1()
        self.rotate_mode=2
    def counterclockwise2(self):
        self.counterclockwise1()
        self.rotate_mode=2
    def clockwise2(self):
        self.clockwise1()
        self.rotate_mode=2
    def up11(self,event):
        self.up1()
    def down11(self,event):
        self.down1()
    def left11(self,event):
        self.left1()
    def right11(self,event):
        self.right1()
    def clockwise11(self,event):
        self.clockwise1()
    def counterclockwise11(self,event):
        self.counterclockwise1()
    def up22(self,event):
        self.up1()
        self.rotate_mode=2
    def down22(self,event):
        self.down1()
        self.rotate_mode=2
    def left22(self,event):
        self.left1()
        self.rotate_mode=2
    def right22(self,event):
        self.right1()
        self.rotate_mode=2
    def counterclockwise22(self,event):
        self.counterclockwise1()
        self.rotate_mode=2
    def clockwise22(self,event):
        self.clockwise1()
        self.rotate_mode=2
    
        
    def title(self):
        self.root.title(u'布拉格点阵及其倒易空间')
    def getLtype(self):
        self.mode1=True
        self.mode2=False
        self.root.quit()

    def getInfo(self):
        self.root.mainloop()
        self.cv
        maininfo=dict(lattice_type=self.v.get(), crystal_constant=self.a, mode=[self.mode1,self.mode2],
                      rotate_angle=self.rotate_angle,rotate_direction=self.direction,rotate_mode=self.rotate_mode,
                      r_circle=self.r_circle,color1=self.color1,circle_color1=self.circle_color1,
                      circle_color2=self.circle_color2,color2=self.color2,color3=self.color3,
                      color4=self.color4,color5=self.color5)
        return self.gFlag,self.cv,maininfo
    def menu(self):
        m=Menu(self.root)
        self.root.config(menu=m)
        filemenu=Menu(m)
        m.add_cascade(label=u'文件',menu=filemenu)
        filemenu.add_command(label=u'设置',command=self.settings)
        filemenu.add_separator()
        filemenu.add_command(label=u'退出',command=self.close)
        helpmenu=Menu(m)
        m.add_cascade(label=u'帮助',menu=helpmenu)
        helpmenu.add_command(label=u'程序介绍',command=self.about1)
        helpmenu.add_separator()
        helpmenu.add_command(label=u'关于',command=self.about2)
    def about1(self):
        c=Toplevel()
        c.title(u'关于')
        words=Label(c,text=u'这个程序为大家展示了14种布拉格\n点阵及其倒易空间的三维图像',justify=LEFT)
        words.grid()
        Label(c,text=u'重要提醒:本程序需要安装numpy库,文件名为numpy-1.8.0-win32-superpack-python2.7,exe,请从官方网站下载.').grid()
        b=Button(c,text=u'关闭',command=c.destroy)
        b.grid()
        c.mainloop()
    def about2(self):
        c=Toplevel()
        c.title(u'zyh')
        Label(c,text=u'本程序由:\n材料科学与工程学院\n周逸涵\n5120519133\n所编写，欢迎大家使用!',justify=LEFT).grid()
        b=Button(c,text=u'关闭',command=c.destroy)
        b.grid()
        c.mainloop()
    def settings(self):
        self.settingc=Toplevel()
        c=self.settingc
        c.title(u'设置')
        Entry(c,textvariable=self.k1).grid(row=1,column=1)
        Label(c,text=u'晶胞边长').grid(row=1,column=0)
        Entry(c,textvariable=self.k2).grid(row=2,column=1)
        Label(c,text=u'点的半径').grid(row=2,column=0)
        Entry(c,textvariable=self.k3).grid(row=3,column=1)
        Label(c,text=u'每次旋转角大小').grid(row=3,column=0)
        ttk.Combobox(c,textvariable=self.k4, values=[u"red", u"pink", u"orange",
                        u'yellow',u'purple',u'green',u'blue',u'brown',u'black']).grid(row=4,column=1)
        Label(c,text=u'坐标轴颜色').grid(row=4,column=0)
        ttk.Combobox(c,textvariable=self.k5, values=[u"red", u"pink", u"orange",
                        u'yellow',u'purple',u'green',u'blue',u'brown',u'black']).grid(row=5,column=1)
        Label(c,text=u'实际空间点的颜色').grid(row=5,column=0)
        Label(c,text=u'倒易空间点的颜色').grid(row=6,column=0)
        ttk.Combobox(c,textvariable=self.k6, values=[u"red", u"pink", u"orange",
                        u'yellow',u'purple',u'green',u'blue',u'brown',u'black']).grid(row=6,column=1)
        Label(c,text=u'实际空间虚线的颜色').grid(row=7,column=0)
        ttk.Combobox(c,textvariable=self.k7, values=[u"red", u"pink", u"orange",
                        u'yellow',u'purple',u'green',u'blue',u'brown',u'black']).grid(row=7,column=1)
        Label(c,text=u'倒易空间虚线的颜色').grid(row=8,column=0)
        ttk.Combobox(c,textvariable=self.k8, values=[u"red", u"pink", u"orange",
                        u'yellow',u'purple',u'green',u'blue',u'brown',u'black']).grid(row=8,column=1)
        Label(c,text=u'实际空间被挡住点和线的颜色').grid(row=9,column=0)
        ttk.Combobox(c,textvariable=self.k9, values=[u"red", u"pink", u"orange",
                        u'yellow',u'purple',u'green',u'blue',u'brown',u'black']).grid(row=9,column=1)
        Label(c,text=u'倒易空间被挡住点和线的颜色').grid(row=10,column=0)
        ttk.Combobox(c,textvariable=self.k10, values=[u"red", u"pink", u"orange",
                        u'yellow',u'purple',u'green',u'blue',u'brown',u'black']).grid(row=10,column=1)
        Button(c,text=u'完成',command=c.quit).grid(row=20,column=1)
        c.mainloop()
        self.color1=self.k4.get()
        self.a=eval(self.k1.get())
        self.r_circle=eval(self.k2.get())
        self.rotate_angle0=eval(self.k3.get())
        self.circle_color1=self.k5.get()
        self.circle_color2=self.k6.get()
        self.color2=self.k7.get()
        self.color3=self.k8.get()
        self.color4=self.k9.get()
        self.color5=self.k10.get()
        self.mode1=False
        self.mode2=True
        self.rotate_mode=4
        c.destroy()
        self.root.quit()
        self.settingc=None
        
    def close(self):
        self.gFlag=True
        self.root.quit()
        self.root.destroy()
        
class zyhAPP:
    def __init__(self,inter,root):
        self.root=root
        self.interface=inter
        self.lines=[]
        self.circles=[]
        self.axis='x'
        self.angle=0
        self.lattices=None
        self.lattices2=None
        self.maininfo=None

    def run(self):
        circles=[]
        lines=[]
        s=Draw(self.root)
        while True:
            
            gFlag,cv,self.maininfo = self.interface.getInfo()
            mode1=self.maininfo['mode'][0]
            mode2=self.maininfo['mode'][1]
            self.maininfo['circles']=self.circles
            self.maininfo['lines']=self.lines
            if not self.lattices:
                self.maininfo['rotate_angle']=0
            
            s.run(cv,self.maininfo)
            
            if gFlag:
                break
            else:
                if mode1: 
                    self.lattices=s.LatticeType()#提取出布拉格点阵的坐标
                    self.lattices2=s.reciprocalLattice(self.lattices) #倒易空间点的坐标
                    points=s.project(self.lattices,s.r)
                    self.circles,self.lines=s.main(points)
                    points2=s.project(self.lattices2,s.r2)
                    circles2,lines2=s.main2(points2)
                    self.maininfo['lattice_1']=self.lattices
                    self.maininfo['lattice_2']=self.lattices2
                    self.circles+=circles2
                    self.lines+=lines2
                    init_lattice1=self.lattices
                    init_lattice2=self.lattices2
                elif mode2:
                    """ maininfo=(lattice_type=self.v.get(), crystal_constant=self.a, mode=[self.mode1,self.mode2],
                    rotate_angle=self.rotate_angle,rotate_direction=self.direction,rotate_mode=self.rotate_mode,
                    r_circle=self.r_circle)
                    """
                    i=self.maininfo['rotate_mode']
                    C=s.rotation()      #C为坐标变换矩阵,axis为旋转轴,angle为旋转角
                    
                    if not self.lattices :
                        self.lattices=s.LatticeType()
                        self.lattices2=s.reciprocalLattice(self.lattices)
                        self.maininfo['lattice_1']=self.lattices
                        self.maininfo['lattice_2']=self.lattices2
                        i=0
                        init_lattice1=self.lattices
                        init_lattice2=self.lattices2
                    if i==1:
                        self.lattices=s.lattice(self.lattices,C)   #变换点的三维坐标
                        points=s.project(self.lattices,s.r)
                        self.circles,self.lines=s.main(points)
                        points2=s.project(self.lattices2,s.r2)
                        circles2,lines2=s.main2(points2)
                        self.maininfo['lattice_1']=self.lattices
                        self.maininfo['lattice_2']=self.lattices2
                        self.circles+=circles2
                        self.lines+=lines2
                        
                    if i==2:
                        self.lattices2=s.lattice2(self.lattices2,C)
                        points=s.project(self.lattices,s.r)
                        self.circles,self.lines=s.main(points)
                        points2=s.project(self.lattices2,s.r2)
                        circles2,lines2=s.main2(points2)
                        self.maininfo['lattice_1']=self.lattices
                        self.maininfo['lattice_2']=self.lattices2
                        self.circles+=circles2
                        self.lines+=lines2
                        
                    if i==0:
                        s.kkkk_s1=s.kkk(init_lattice1)
                        s.kkkk_s2=s.kkk2(init_lattice2)
                        points=s.project(init_lattice1,s.r)
                        self.circles,self.lines=s.main(points)
                        points2=s.project(init_lattice2,s.r2)
                        circles2,lines2=s.main2(points2)
                        self.lattices=init_lattice1
                        self.lattices2=init_lattice2
                        self.maininfo['lattice_1']=self.lattices
                        self.maininfo['lattice_2']=self.lattices2
                        self.circles+=circles2
                        self.lines+=lines2
                    if i==4:
                        self.circles,self.lines=s.main(points)
                        circles2,lines2=s.main2(points2)
                        self.circles+=circles2
                        self.lines+=lines2
                        
                        
            
                        
root=Tk()
windows=GUI(root)
APP=zyhAPP(windows,root)
APP.run()
