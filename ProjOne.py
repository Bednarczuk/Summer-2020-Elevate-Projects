class AerialImagery:
    
    earthRadius = 6378137
    minLat = -85.05112878
    maxLat = 85.05112878
    minLong = -180
    maxLong = 180

    def __init__(self, north_lat, south_lat, west_long, east_long):
        self.north_lat = north_lat
        self.south_lat = south_lat
        self.west_long = west_long
        self.east_long = east_long

    #Python Translation of Original C# Code
    #Link to Original Code: https://docs.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system
    def Clip(n, minValue, maxValue):
        return min(max(n, minValue), maxValue)
    
    def MapSize(levelOfDetail):
        return 256 * pow(2, levelOfDetail)
    
    def GroundResolution(latitude, levelOfDetail):
        latitude = Clip(latitude, minLat, maxLat)
        return math.cos(latitude * math.pi / 180) * 2 * math.pi * earthRadius / MapSize(levelOfDetail)
    
    def LatLongToPixelXY(latitude, longitude, levelOfDetail):
        latitude = Clip(latitude, minLat, maxLat)
        longitude = Clip(longitude, minLong, maxLong)
        
        x = (longitude + 180) / 360
        sinLatitude = math.sin(latitude * math.pi / 180)
        y = 0.5 - math.log((1 + sinLatitude) / ( 1 - sinLatitude)) / (4 * math.pi)
        
        mapSize = MapSize(levelOfDetail)
        pixelX = (int) (Clip(x * mapSize + 0.5, 0, mapSize - 1))
        pixelY = (int) (Clip(y * mapSize + 0.5, 0, mapSize - 1))
        
        return pixelX, pixelY
    
    def PixelXYToLatLong(pixelX, pixelY, levelOfDetail):
        mapSize = MapSize(levelOfDetail)
        x = (Clip(pixelX, 0, mapSize - 1) / mapSize) - 0.5
        y = 0.5 - (Clip(pixelY, 0, mapSize - 1) / mapSize)
        
        latitude = 90 - 360 * math.atan(math.exp(-y * 2 * math.pi)) / math.pi
        longitude = 360 * x
        return latitude, longitude
    
    def PixelXYToTileXY(pixelX, pixelY, levelOfDetail):
        tileX = (int) (pixelX / 256)
        tileY = (int) (pixelY / 256)
        return tileX, tileY
    
    def TileXYToPixelXY(tileX, tileY):
        pixelX = tileX * 256
        pixelY = tileY * 256
        return pixelX, pixelY
    
    def TileXYToQuadKey(tileX, tileY, levelOfDetail):
        quadKey = ''
        
        for i in range(levelOfDetail, 0, -1):
            digit = 0
            mask = 1 << (i - 1)
            if ((tileX & mask) != 0):
                digit = digit + 1
                
            if ((tileY & mask != 0)):
                digit = digit + 1
                digit = digit + 1
                
            quadKey += str(digit)
            
            return 'http://ecn.t0.tiles.virtualearth.net/tiles/a' + quadKey + '.jpeg?g=471&mkt=en'
        
    def LatLongToTileXY(latitude, longitude, levelOfDetail):
        pixelX, pixelY = LatLongToPixelXY(latitude, longitude, levelOfDetail)
        return PixelXYToTileXY(pixelX, pixelY, levelOfDetail)
