# Decorator
# Wrap another functions to extend the functionality
# without change the original code

def higher_order_example(func):

    def inside():
        print("start ...")
        func()
        print("end ...")

    return inside

@higher_order_example # excution
def sample_example():
    print("I am inside")

sample_example()

# => start ... => I am inside => end ...