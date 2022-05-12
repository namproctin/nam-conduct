




#direction = "EAST"
#=> keep going until hit a visted element or can't go anymore
#  => switch direction to SOUTH
#    => keep going until hit a visted element or can't go anymore
#    => switch direction to WEST
#
#    => if step_count = m*n => exit


def switch_direction(current_direction):
  if current_direction == "EAST":
    return "SOUTH"
  elif current_direction == "SOUTH":
    return "WEST"
  elif current_direction == "WEST":
    return "NORTH"
  elif current_direction == "NORTH":
    return "EAST"

def move_spiral(arr):

  visited = []
  visited = {(-1,-1)}

  result=[]

  current_x = 0
  current_y = 0
  current_step = 0
  current_direction = "EAST"
  max_step = len(arr) * len(arr[0])


  while current_step < max_step:
    current_step += 1
    if ( current_y,current_x) in visited:
      current_direction = switch_direction(current_direction)
      current_step -= 1
    else:
      #print("aaa")
      #print(current_y,current_x)
      #print(arr[current_y][current_x])
      result.append(arr[current_y][current_x])
      visited.add((current_y,current_x))

      if current_direction == "EAST":
        if current_x < len(arr[0]) -1 :
          current_x += 1
          if (current_y,current_x) in visited:
            current_x += 1
            current_direction = switch_direction(current_direction)
        else:
          current_direction = switch_direction(current_direction)
          current_y += 1
      elif current_direction == "SOUTH":
        if current_y < len(arr) -1:
          current_y += 1
          if (current_y,current_x) in visited:
            current_y -= 1
            current_direction = switch_direction(current_direction)
            current_x -= 1
        else:
          current_direction = switch_direction(current_direction)
          current_x -= 1
      elif current_direction == "WEST":
        if current_x > 0:
          current_x -= 1
          if (current_y,current_x) in visited:
            current_x += 1
            current_direction = switch_direction(current_direction)
            current_y -= 1
        else:
          current_direction = switch_direction(current_direction)
          current_y -= 1
      elif current_direction == "NORTH":
        if current_y > 0:
          current_y -= 1
          if (current_y,current_x) in visited:
            current_x += 1
            current_direction = switch_direction(current_direction)
            current_y += 1
        else:
          current_direction = switch_direction(current_direction)
          current_x += 1



      #print(visited)

    #print(result)
    #break
  print(result)
  return result




matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
move_spiral(matrix)
