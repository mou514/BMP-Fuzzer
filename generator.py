class Generator:
	'Generator for Malformed Data'
	 
	MalformedValues = [
	('RepeatedAx1','A'), ('RepeatedNULLx1','\x00'),
	('Numeric -1','-1'), ('Numeric -2','-2'), ('Numeric 0','0'),
	('Binary -1 (BYTE)','\xFF'), ('Binary -2 (BYTE)','\xFE'),
	('Binary -2 (2 BYTES)','\xFF\xFE'), ('Binary -2 (2 BYTES Reverse)','\xFE\xFF'),
	('Format String %sx1','%s'), ('Format String %xx1','%x')]
 
	def __init__(self):
		print 'Generator Created'
	def returnCount(self):
		return len(self.MalformedValues)
	 
	def returnValueAt(self, value):
		return self.MalformedValues[value][1]
	 
	def returnNameAt(self, value):
		return self.MalformedValues[value][0]
