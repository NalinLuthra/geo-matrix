while True:
  q = raw_input("Enter option for controller")
  if q == 'q':
    print "I am starting"
    execfile("handler.py")
    print "I am ending"
