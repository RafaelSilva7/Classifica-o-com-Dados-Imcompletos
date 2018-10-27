import dataset
from missingPatterns import MissingPatterns

if __name__ == "__main__":
    # execute only if run as a script
    d = dataset.Dataset()
    mp = MissingPatterns(d).missing_patterns

    for i in mp:
    	print(set(i))

    
