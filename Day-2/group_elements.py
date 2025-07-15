#Group Elements of Same Indices using Python
def group_elements(lst):
    try:
        # using list comprehension and zip() to pair index elements
        res = [list(x) for x in zip(*lst)]
        return res
    except Exception as e:
        print(e)

# Example usage
li = [[1, 4, 5], [4, 6, 8], [8, 3, 10],[25,30,80]]
print("Original list : " + str(li))

print("Index pairs list : " + str(group_elements(li)))