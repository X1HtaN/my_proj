class test(object):
    pass

class pretest(test):
    pass

t = pretest()

print(issubclass(test, object))
print(issubclass(pretest, object))
print(issubclass(pretest, test))
print(issubclass(t.__class__, test))