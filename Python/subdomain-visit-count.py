#submitted 12/27/2020
class Solution(object):
    def subdomainVisits(self, input_arr):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dictionary = {}
        i = 0
        while i < len(input_arr):
            input_arr[i] = input_arr[i].split(' ')
            input_arr[i][0] = int(input_arr[i][0])
            input_arr[i][1] = (input_arr[i][1].split('.'))
            i +=1
        i = 0
        #[[9001, [leetcode, com]]]

        while i < len(input_arr):
            if len(input_arr[i][1]) == 2:
                if str((input_arr[i][1][0] + '.' + input_arr[i][1][1])) in dictionary:
                    dictionary[str(input_arr[i][1][0] + '.' + input_arr[i][1][1])] += input_arr[i][0]
                else:
                    dictionary[str(input_arr[i][1][0] + '.' + input_arr[i][1][1])] = input_arr[i][0]

                if str(input_arr[i][1][1]) in dictionary:
                    dictionary[str(input_arr[i][1][1])] += input_arr[i][0]
                else:
                    dictionary[str(input_arr[i][1][1])] = input_arr[i][0]

            if len(input_arr[i][1]) == 3:
                if str(input_arr[i][1][0] + '.' + input_arr[i][1][1] + '.'+ input_arr[i][1][2]) in dictionary:
                    dictionary[str(input_arr[i][1][0] + '.' + input_arr[i][1][1] + '.'+ input_arr[i][1][2])] += input_arr[i][0]
                else:
                    dictionary[str(input_arr[i][1][0] + '.' + input_arr[i][1][1] + '.'+ input_arr[i][1][2])] = input_arr[i][0]

                if str(input_arr[i][1][1] + '.' + input_arr[i][1][2]) in dictionary:
                    dictionary[str(input_arr[i][1][1] + '.' + input_arr[i][1][2])] += input_arr[i][0]
                else:
                    dictionary[str(input_arr[i][1][1] + '.' + input_arr[i][1][2])] = input_arr[i][0]

                if str(input_arr[i][1][2]) in dictionary:
                    dictionary[str(input_arr[i][1][2])] += input_arr[i][0]
                else:
                    dictionary[str(input_arr[i][1][2])] = input_arr[i][0]
            i += 1
        returnme = []
        print(dictionary)
        for item in dictionary:
            returnme.append(str(dictionary[item]) + ' '+ item) 
        return returnme