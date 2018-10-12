import dataset
import missing_patterns

if __name__ == "__main__":
    # execute only if run as a script
    d = dataset.Dataset()
    mp = missing_patterns.MissingPatterns(d).mp

    
