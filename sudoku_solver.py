#author: Kaustubh Wankhede

def possible(y,x,n):
    """return bool of possiblity of n in (x,y)"""
    global sud
    x0,y0=(x//3)*3,(y//3)*3
    for i in range(9):
        if sud[y][i] == n:
            return False
        if sud[i][x] == n:
            return False
    for i in range(3):
        for j in range(3):
            if(sud[y0+i][x0+j] == n):
                return False
    return True

def solve(sud):
    """brute solves sudoku sud and appends all possible solutions in result"""
    global placeholder,result
    for y in range(9):
        for x in range(9):
            if(sud[y][x]==placeholder):
                for n in range(1,10):
                    if(possible(y,x,n)):
                        sud[y][x] = n
                        solve(sud)
                        sud[y][x] = placeholder
                return
    result.append(np.array(sud))


def convert(stri):
    """convert blank spaces in raw input to placeholder defined"""
    global placeholder
    if(type(stri)==int):
        return stri
    else:
        stri=stri.get()
        if(stri!=''):
            return int(stri)
        else:
            return placeholder
    
    
    
def mainsolv():
    """button called function to connect gui with solving code"""
    global sud
    sud=list(map(lambda x:list(map(lambda y:convert(y),x)),sud))
    solve(sud)
    root.destroy()
    res=tk.Tk()
    res.title("Result")
    i0,j0=0,1
    e=tk.Label(res,text="Solutions: ").grid(row=0,column=0)
    for c in result:
        for i in range(9):
            for j in range(9):
                
                e=tk.Label(res,text="------------------").grid(row=1+12*i0,column=0)
                e=tk.Label(res,text=str(c[i][j]),font="Times").grid(row=i+1+j0+i0*11+i//3,column=j+j//3+1)
        i0+=1
        j0+=1
    res.mainloop()
    
#libraries used: numpy(for sudoku managing) and tkinter(for gui)
import numpy as np
import tkinter as tk
placeholder,sud,result=0,[],[]
root=tk.Tk()
root.title("Sudoku")
for i in range(0,9):
    row=[]
    for j in range(0,9):
        e = tk.Entry(root)
        e.grid(row=i,column=j)
        row.append(e)
    sud.append(row)

b = tk.Button(root,text="submit",command=mainsolv)
b.grid(row=10,column=4)
root.mainloop()



