def mapto(x, minx, maxx, miny, maxy):
        tmaxx = maxx-minx
        tmaxy = maxy-miny
        scale = tmaxy/tmaxx   
        x = x-minx
        x *= scale
        x += miny
        return x


print(mapto(0.7,0,1,0,10))
