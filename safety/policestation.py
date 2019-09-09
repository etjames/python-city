def draw_policestation(cars, officers):
    '''
        Draws a police station
        
        Args:
            cars: int that specifies how many police cars you want at the station
            officers: int that specifies how many officers you want at the station
    '''
    
     # Sanitizing Parameters
    if cars < 0:
        raise ValueError("cars is negative")
    if officers < 0:
        raise ValueError("officers is negative")
    
    #print out the building
    print("    ____________   ")
    print("   |            |  ")
    print("   |            |  ")
    print("   |    POLICE  |  ")
    print("   |            |  ")
    print("   |            |  ")
    print("   |            |  ")
    print("   |     ____   |  ")
    print("   |     |  |   |  ")
    
    
    if cars != 0:
        #print out the cars
        print(" ___ " * cars)
        print("/   \\" * cars)
        print("()-()" * cars)
    
    if officers != 0:   
        #print out the officers
        print("  _   " * officers)
        print("  0   " * officers)
        print(" -|-  " * officers)
        print(" / \  " * officers)
    
   
    
    return
