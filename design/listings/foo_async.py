@inlineCallbacks
def foo(x):
	y = x + 1
	z = yield bar(y)
	self.variable = z
