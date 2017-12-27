def rgb_hex():
  invalid_msg  = "Invalid input"
  red = int(raw_input("Gimme the red value: "))
  if red<0 or red>255:
    print "Invalid value"
    return
  
  green = int(raw_input("Gimme the green value: "))
  if green<0 or green>255:
    print "Invalid value"
    return

  blue = int(raw_input("Gimme the blue value: "))
  if blue<0 or blue>255:
    print "Invalid value"
    return
  
  val = int(red << 16) + int(green << 8) + int(blue)
  value = hex(val).upper()
  print value[2:]
  
def hex_rgb():
  hex_val = raw_input("Give me an hexadecimal value: ")
  if len(hex_val) != 6:
    print "Error. An hex must be 6 characters long"
    return
  else:
    hex_val = int(hex_val, 16)

    two_hex_digits = 2**8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits
    print red+green+blue
    
def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == '1':
      print "RGB to Hex..."
      rgb_hex()
    elif option == '2':
      print "Hex to RGB..."
      hex_rgb()
    elif option == 'x' or option == 'X':
      break
    else:
      print "Error"

      
convert()
    