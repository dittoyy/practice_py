#coding:utf-8
class Dido(object):
        """docstring for Dido"""
        def __init__(self):
            # super(Dido, self).__init__()
            self.arg = []
        def add(self,a,p='dido',*b,**c):
            for i in b:
                self.arg.append(i)
            return "{},{},{},{}".format(a,p,b,c)

s=Dido()
print s.add(1,23,24,55,6,7,98,"55f",x=3,y=7)

class Param(object):
    """docstring for Param"""
    # def __init__(self, arg):
    #     # super(Param, self).__init__()
    #     self.arg = arg
    def printMax(self,a,b):
        if a>b:
            print a,'is ,maximum'
        elif a==b:
            print a,'=',b
        else:
            print b,'is ,maximum'
            pass
    # printMax(1,1)
    def jubu(x):
        print 'x is',x
        x=2
        print 'xxxx1',x
    x=50
    jubu(x)
    print 'xxxxxx2',x




d=Param()
print d.printMax(1,1)
# print d.printMax(1,2)
# print d.printMax(3,'1')
if __name__ == '__main__':

    s=Dido()
    # v=Dido()
    # print s==v
    t=s.add(1,2,3,4,5)
    print t
    print s.arg

    # for x in xrange(1,9):
    #     for y in xrange(1,x+1):
    #         # print ('{}*{}={}\t'.format(x,y,x*y),'')
    #         print "%d*%d=%2d" % (x,y,x*y)
    #     print '\n'
    # p=(j for j in range(1,9))#<generator object <genexpr> at 0x02486120>
    # print p
    # print p.next()
    # print p.next()

    p=[j for j in range(1,9)]#[1, 2, 3, 4, 5, 6, 7, 8]
    print p





    # print ('\n'\
    #     .join(['  '.join(['%s*%s=%-2s' % (j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)]))

    # field_names=[i for i in range(1,10)]
    # print field_names

    # mulp=[["%d*%d=%2d" %(a,b,a*b) if a>=b else "" for b in range(1,10)] for a in range(1,10)]
    # print mulp
    # # map(pt.add_row,mulp)

    # # print(pt)
    # def f(i):
    #     if i>=1:
    #         f(i-1)
    #         print(['%dx%d=%d'%(j,i,i*j) for j in range(1,i+1)])
    # f(9)



    #