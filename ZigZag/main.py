class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 0:
            return ''
        if numRows == 1:
            return s
        # print(numRows)
        main_list = []
        flag = 0
        for i in range(numRows):
            main_list.append([])
        counter = 0
        for num,each in enumerate(s):
            # print(num,numRows)
            if (counter % numRows == 0 and counter!= 0) or flag == 1 :
                # print("In here da")
                counter -= 1
                print(counter)
                if counter == 0:
                    # print("ADA")
                    main_list[counter].append(each)
                    counter += 1
                    flag = 0
                    continue
                elif counter == 1:
                    main_list[counter].append(each)
                else:
                    if counter == numRows -1:
                        counter -= 1
                        main_list[counter].append(each)
                        flag = 1
                    else:
                        main_list[counter].append(each)
                # counter = 0
            else:
                # print("num",num)
                # print("counter",str(counter))
                main_list[counter].append(each)
                counter += 1
        final_str = ''
        for each in main_list:
            final_str += ''.join(each)
        print(final_str)
            
            
s = Solution()
s.convert("ABCDEF",2)