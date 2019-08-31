'''
Kindly Check the following Link:
https://en.wikipedia.org/wiki/BMP_file_format
'''
class Structure:
	'Structure for BMP Image File'
	 #Bitmap File Header
	BMPStructure = [{'Name': 'bfType' , 'Type': 'C', 'Default': 'BM', 'Size': -1},                  #Bitmap Type, C=Constant, DefaultValue=BM
	{'Name': 'bfSize' , 'Type': 'L', 'Default': '\x33\x33\x33\x33', 'Size': 4, 'Order': 'Reverse'}, #Bitmap Size, L=Length 
	{'Name': 'bfReserved1' , 'Type': 'C', 'Default': '\x00\x00', 'Size': -1},                       #Reserved1
	{'Name': 'bfReserved2' , 'Type': 'C', 'Default': '\x00\x00', 'Size': -1},                       #Reserved2
	{'Name': 'bfOffBits' , 'Type': 'C', 'Default': '\x36\x00\x00\x00', 'Size': -1},                 #OffsetBits=Offset where the pixel array (bitmap data) can be found
	 #Bitmap Info Header
	{'Name': 'biSize' , 'Type': 'C', 'Default': '\x28\x00\x00\x00', 'Size': -1},                    #Size=Number of bytes in the DIB header (from this point)
	{'Name': 'biWidth' , 'Type': 'B', 'Default': '\x02\x00\x00\x00', 'Size': 4},                    #Width, B=Buffer
	{'Name': 'biHeight' , 'Type': 'B', 'Default': '\x02\x00\x00\x00', 'Size': 4},                   #Height
	{'Name': 'biPlanes' , 'Type': 'B', 'Default': '\x01\x00', 'Size': 2},                           #Number of Planes
	{'Name': 'biBitCount' , 'Type': 'B', 'Default': '\x18\x00', 'Size': 2},                         #Number of Bits per Pixels
	{'Name': 'biCompression' , 'Type': 'C', 'Default': '\x00\x00\x00\x00', 'Size': -1},             #Compression
	{'Name': 'biSizeImage' , 'Type': 'B', 'Default': '\x10\x00\x00\x00', 'Size': 4},                #Size of raw bitmap data
	{'Name': 'biXPelsPerMeter' , 'Type': 'B', 'Default': '\x13\x0B\x00\x00', 'Size': 4},            #Print resolution of image X
	{'Name': 'biYPelsPerMeter' , 'Type': 'B', 'Default': '\x13\x0B\x00\x00', 'Size': 4},            #Print resolution of image Y
	{'Name': 'biClrUsed' , 'Type': 'B', 'Default': '\x00\x00\x00\x00', 'Size': 4},                  #Number of colors in palette
	{'Name': 'biClrImportant' , 'Type': 'B', 'Default': '\x00\x00\x00\x00', 'Size': 4},             #Color Important 
	 
	{'Name': 'aColors', 'Type': 'B', 'Default': '\xFF\x20', 'Size': 64},                            #Colors
	 
	{'Name': 'aBitmapBits', 'Type': 'B', 'Size': 64,                                                #Bitmap Image Bits (R,G,B)
	'Default': '\x00\x00\xFF\xFF\xFF\xFF\x00\x00\xFF\x00\x00\x00\xFF\x00\x00\x00'}]
 
	def __init__(self):
		print 'Structure Instance Created'
	def returnStructure(self):
		return self.BMPStructure