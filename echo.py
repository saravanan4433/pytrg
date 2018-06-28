def echo(*args,**kwargs):
    print(args,kwargs)
    type(args)
echo("a","b",1,2,a=3,b=4)
echo(1,2,a=3,b=4)

