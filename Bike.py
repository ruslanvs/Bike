class Bike( object ):
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
        if self.miles < 5:
            print "We only have", self.miles, "miles. Cannot reverse anymore!"
            return( self )
        print "Revesing..."
        self.miles -= 5
        print "Miles after reversing", self.miles
        return( self )

Harley = Bike( 20000, "120mph" )
Dukatti = Bike( 30000, "160mph" )
Suzuki = Bike( 25000, "200mph" )

Harley.ride().ride().ride().reverse().displayInfo()
Dukatti.ride().ride().reverse().reverse().displayInfo()
Suzuki.reverse().reverse().reverse().displayInfo()