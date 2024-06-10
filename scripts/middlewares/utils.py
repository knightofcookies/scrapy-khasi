def remove_indentation(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    dedented_lines = [line[4:] for line in lines]
    
    with open(filename, 'w') as file:
        file.writelines(dedented_lines)

# Usage example:
remove_indentation('updated_scrapy_selenium_middleware.py')
