class Bike(object):
    def __init__( self, price, max_speed, miles = 0 ):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo( self ):
        print self.price, self.max_speed, self.miles
        return self
    def ride( self ):
        print "Miles before the ride", self.miles
        print "Riding ..."
        self.miles += 10
        print "Miles after the ride", self.miles
        return( self )
    def reverse( self ):
        print "Revesing..."
        self.miles -= 5
        print "Miles after reversing", self.miles

Harley = Bike( 20000, "160mph" )
Dukatti = Bike( 20000, "160mph" )
Suzuki = Bike( 20000, "160mph" )

Dukatti.displayInfo()
Dukatti.ride()
Dukatti.reverse()