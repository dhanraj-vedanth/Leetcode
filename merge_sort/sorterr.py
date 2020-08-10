from random import randint

class Mergesort:
    def __init__(self):
        pass
    def mergesort(self, input_array):
        """
        Breakdown the array into left and right halves
        - call mergesort recursively
        - if the length of the array is less than 1 -> return array
        - Finally call the sort function on the the left and right subarray
        """
        if len(input_array) > 1:
            mid = len(input_array)//2
            left = self.mergesort(input_array[:mid])
            right = self.mergesort(input_array[mid:])
            val = self.sort(left,right)
            return val
        return input_array

    def sort(self, left_arr, right_arr):
        """
        merge two sorted arrays and return the sorted array
        """
        sorted_array = []
        left_ind, right_ind = 0,0
        while left_ind < len(left_arr) and right_ind < len(right_arr):
            if left_arr[left_ind] < right_arr[right_ind]:
                sorted_array.append(left_arr[left_ind])
                left_ind += 1
            else: 
                sorted_array.append(right_arr[right_ind])
                right_ind += 1
        if left_ind == len(left_arr):
            sorted_array.extend(right_arr[right_ind:])
        else:
            sorted_array.extend(left_arr[left_ind:])
        return sorted_array

    def random_array_generator(self, size, lower_bound, higher_bound):
        """
        Generate an array of length 'size' with the lower and upper bounds
        """
        return [randint(lower_bound,higher_bound) for each in range(size)]

merge_obj = Mergesort()
rand_array = merge_obj.random_array_generator(10,0,100)
print(f"Input array -> {rand_array}")
print(f" Returned sorted array -> {merge_obj.mergesort(rand_array)}")
print(f"Tried making this change to see if repo is adjusted")
