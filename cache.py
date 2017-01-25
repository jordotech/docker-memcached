# Import python-memcache and sys for arguments
import memcache
import sys

# Set address to access the Memcached instance
addr = '138.197.67.236'

# Get number of arguments
# Expected format: python cache.py [memcached port] [key] [value]
len_argv = len(sys.argv)

# At least the port number and a key must be supplied
if len_argv < 3:
    sys.exit("Not enough arguments.")

# Port is supplied and a key is supplied - let's connect!
port  = sys.argv[1]
test = "{0}:{1}".format(addr, port)
print test
cache = memcache.Client(["138.197.67.236:45001"])
print cache
# Get the key
key   = str(sys.argv[2])

# If a value is also supplied, set the key-value pair
if len_argv == 4:

    value = str(sys.argv[3])
    cache.set(key, value)

    print "Value for {0} set!".format(key)

# If a value is not supplied, return the value for the key
else:

    value = cache.get(key)

    print "Value for {0} is {1}.".format(key, value)