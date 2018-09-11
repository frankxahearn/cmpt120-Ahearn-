#Frank Ahearn
#9/11/2018
#rover.py
#
#This program calculates how long it takes a photo from Curosity
#to reach NASA when Mars is at its closet orbit to earth

#Speed of light is 186,000 miles per second
#Distance is 34 million miles
#
def main():
    speed_of_light = 186000
    distance = 34000000
    time  = distance/speed_of_light
    
    print("The time for a picture to reach Earth is ", time, " seconds")
    

    
main()
