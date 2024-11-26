from kanren import run, var, fact
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative
addition = &#39;add&#39;
multiplication = &#39;mul&#39;
fact(commutative, multiplication)
fact(commutative, addition)
fact(associative, multiplication)
fact(associative, addition)
x, y,z = var(&#39;a&#39;), var(&#39;b&#39;), var(&#39;c&#39;)
originalPattern = (multiplication, (addition,z,x),y)
ex1 = (multiplication, 9, (addition, 5, 1))
ex2 = (addition,5,(multiplication,8,1))
ex3 = (multiplication, 59, (addition,234, 34))
print(run(0, (x,y,z), eq(originalPattern, ex1)))
print(run(0, (x,y,z), eq(originalPattern, ex2)))

print(run(0, (x,y,z), eq(originalPattern, ex3)))
