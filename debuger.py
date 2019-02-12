
import os

if __name__ == "__main__":
    for k in os.environ.keys():
        print("key={key}".format(key=k))
