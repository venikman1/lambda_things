# import sys
# sys.setrecursionlimit(1000000000)

null = lambda n: lambda x: x
inc = lambda a: lambda n: lambda x: n(a(n)(x))
dec = lambda a: lambda n: lambda x: a(lambda u: lambda h: h(u(n)))(lambda u: x)(lambda x: x)


add = lambda a: lambda b: a(inc)(b)
sub = lambda a: lambda b: b(dec)(a)

mul = lambda a: lambda b: a(add(b))(null)


true = lambda a: lambda b: a
false = lambda a: lambda b: b
if_then_else = lambda cond: lambda x: lambda y: cond(x)(y)

logic_and = lambda a: lambda b: a(b)(false)
logic_or = lambda a: lambda b: a(true)(b)
logic_not = lambda a: a(false)(true)

iszero = lambda a: a(lambda x: false)(true)
leq = lambda a: lambda b: iszero(sub(a)(b))
eq = lambda a: lambda b: logic_and(leq(a)(b))(leq(b)(a))

rec = lambda u: u(u)
fact = rec(lambda f: lambda n: if_then_else(iszero(n))(lambda _: inc(null))(lambda _: mul(n)(f(f)(dec(n))))(f))
# do_while = rec(lambda f: lambda do: lambda cond_f: if_then_else(cond_f(do(do)))(lambda _: f(f)(do)(cond_f))(lambda _: _)(f))

minimum = lambda a: lambda b: if_then_else(leq(a)(b))(a)(b)

pair = lambda a: lambda b: lambda getter: getter(a)(b)
first = lambda pr: pr(true)
second = lambda pr: pr(false)

stack = pair(pair(null)(null))(null)
top = lambda st: first(first(st))
pop = lambda st: second(first(st))
size = lambda st: second(st)
push = lambda st: lambda a: pair(pair(a)(st))(inc(size(st)))
isempty = lambda st: iszero(size(st))
for_in_stack = rec(lambda f: lambda st: lambda callback: if_then_else(isempty(st))(lambda _: _)(lambda _: ((lambda _: f(f)(pop(st))(callback))(callback(top(st)))))(f))
for_in_stack_forward = rec(lambda f: lambda st: lambda callback: if_then_else(isempty(st))(lambda _: _)(lambda _: ((lambda _: callback(top(st)))(f(f)(pop(st))(callback))))(f))
get = lambda st: lambda i: top(sub(size(st))(inc(i))(pop)(st))
set = rec(lambda f: lambda st: lambda i: lambda num: if_then_else(eq(size(st))(inc(i)))(lambda _: push(pop(st))(num))(lambda _: push(f(f)(pop(st))(i)(num))(top(st)))(f))
swap = lambda st: lambda i: lambda j: set(set(st)(i)(get(st)(j)))(j)(get(st)(i))

# def get_const(n):
#     if n == 0:
#         return null
#     return inc(get_const(n - 1))



# kek
get_const = rec(lambda f: lambda n: null if n == 0 else inc(f(f)(n - 1)))
read_num = lambda: get_const(int(input()))
to_int = lambda a: a(lambda x: x + 1)(0)
print_num = lambda n: print(to_int(n), end=" ")

# def read_num():
#     return get_const(int(input()))

# def to_int(a):
#     return a(lambda x: x + 1)(0)


swap_if_greater = lambda st: lambda i: lambda j: if_then_else(leq(get(st)(j))(get(st)(i)))(lambda _: swap(st)(i)(j))(lambda _: st)(null)
do_bubble = rec(lambda f: lambda st: lambda i: lambda n: if_then_else(eq(inc(i))(n))(lambda _: st)(lambda _: f(f)(swap_if_greater(st)(i)(inc(i)))(inc(i))(n))(f))
sort_rec = rec(lambda f: lambda st: lambda i: lambda n: if_then_else(eq(i)(n))(lambda _: st)(lambda _: f(f)(do_bubble(st)(null)(n))(inc(i))(n))(f))
sort = lambda st: sort_rec(st)(null)(size(st))


read_stack = rec(lambda f: lambda st: lambda inp: if_then_else(iszero(inp))(lambda _: st)(lambda _: f(f)(push(st)(inp))(read_num()))(f))
st1 = read_stack(stack)(read_num())

st2 = sort(st1)
for_in_stack_forward(st2)(print_num)
# print(to_int(fact(read_num())))
# print(to_int(fact)(read_num()))
# print(to_int(add(read_num())(read_num())))
# print(to_int(minimum(read_num())(read_num())))