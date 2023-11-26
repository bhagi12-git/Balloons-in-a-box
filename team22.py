
#objective:  ballons should be placed in such a manner that after infalting each of them they should have maximum volume
#find:volume of the cuboid left uncovered with ballons(total volume of cuboid-volume occupied by ballons considered) 

#intake of number of balloons
import math

def distance_between_points(point1,point2):
  sum=0
  for i in range(0,3):
    sum=sum+pow(point1[i]-point2[i],2)
  return round(math.sqrt(sum),4)

def volume_of_balloon(r):
  return round(((4/3)*math.pi*(r**3)))

def first_balloon(list1):
    x=min((right_top_coordinates[0]-list1[0][0]),(list1[0][0]-left_bottom_coordinates[0]))
    y = min((right_top_coordinates[1] - list1[0][1]), (list1[0][1] - left_bottom_coordinates[1]))
    z = min((right_top_coordinates[2] - list1[0][2]), (list1[0][2] - left_bottom_coordinates[2]))
    return round(((4/3)*math.pi*((min(x,y,z))**3)))
    
def other_balloon(list2):
  lst2=[]
  for i in list2:
      x=min((right_top_coordinates[0]-i[0]),(i[0]-left_bottom_coordinates[0]))
      y=min((right_top_coordinates[1]-i[1]),(i[1]-left_bottom_coordinates[1]))
      z=min((right_top_coordinates[2]-i[2]),(i[2]-left_bottom_coordinates[2]))
      lst2.append(min(x,y,z))
  distance=distance_between_points(list2[0],list2[1])
  lst_volumes=[]
  for i in lst2:
      lst_volumes.append(volume_of_balloon(i))
      b2=0
      b1=volume_of_balloon(i)
      re=distance-i
      if re>0:
        s=1
        if i == 1:
          s=0
        b2=volume_of_balloon(min(lst2[s],re))
        lst_volumes.append(b1 + b2)
  return max(lst_volumes) 
  
def get_input():
    global n,left_bottom_coordinates,total_volume,right_top_coordinates,balloon_coordinates
    n = int(input())
    left_bottom_coordinates = list(map(int,input().split()))
    right_top_coordinates = list(map(int,input().split()))
    total_volume = 1
    for i in range(3):
        total_volume*=abs(left_bottom_coordinates[i]-right_top_coordinates[i])
    balloon_coordinates =[]
    for i in range(n):
        balloon_coordinates.append(list(map(int,input().split())))
    non_zero = int(input())
    
get_input()
if n==1:
    print("Box1:",total_volume-first_balloon(balloon_coordinates))
elif n>1:
    print("Box1:",total_volume-other_balloon(balloon_coordinates))
    
