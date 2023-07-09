# Use variable number of parameters

# First positional arguments, then named arguments
def f(*args, **kwargs):
    # Positiional args
    #print("Positional:", args)

    #Named arguments
    print("Named", kwargs)


#f(100, 25, 89)

f(galleons=100, sickels=50, knuts=25)