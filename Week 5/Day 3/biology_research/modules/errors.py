import random
read_failure_probability = 0 # Initial failure probability
write_failure_probability = 0 

class Errors:
    def generate_read_error():
        global read_failure_probability
        try:
            if random.random() < read_failure_probability:
            # Raise a random exception
                random_exception = random.choice([
                FileNotFoundError,
                PermissionError,
                IsADirectoryError,
                FileExistsError,
                NotADirectoryError
                ])
                raise random_exception("Random exception raised")
            else:
                ### READ/WRITE CODE HERE ###
                if read_failure_probability < 1.0: # Cap the failure probability at 100%
                
                    read_failure_probability += 0.05 # Increase failure probability
            
                print('failure_probability after: ', read_failure_probability)
        except Exception as e:
            read_failure_probability = 0 # Reset failure probability upon failure
            raise e

    def generate_write_error():
        global write_failure_probability
        try:
            if random.random() < write_failure_probability:
            # Raise a random exception
                random_exception = random.choice([
                PermissionError,
                IsADirectoryError,
                IOError
                ])
                raise random_exception("Random exception raised")
            else:
                ### READ/WRITE CODE HERE ###
                if write_failure_probability < 1.0: # Cap the failure probability at 100%
                
                    write_failure_probability += 0.05 # Increase failure probability
            
                print('failure_probability after: ', write_failure_probability)
        except Exception as e:
            write_failure_probability = 0 # Reset failure probability upon failure
            raise e