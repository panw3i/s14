with open("1.txt","r+") as f:
    for line in f:
        print(line)

# The with statement handles opening and closing the file, including if an exception is raised in the inner block.The for line in f treats the file object f as an iterable, which automatically uses buffered IO and memory management so you don't have to worry about large files.
#
# There
# should
# be
# one - - and preferably
# only
# one - - obvious
# way
# to
# do
# it.