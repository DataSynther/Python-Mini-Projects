# filters out list of items that are duplicates
def return_duplicates(items):
    duplicates = [i for i in items if items.count(i) > 1]
    return list(set(duplicates))

#example usage
if __name__ == "__main__":
    items = input("Enter a list of items separated by commas: ").split(',')
    items = [item.strip() for item in items]  # Clean up whitespace
    print("Original list:", items)
    print("Duplicates:", return_duplicates(items))
