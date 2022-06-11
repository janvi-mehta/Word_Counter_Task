import re
class Task(object):

    # Static list
    final_lst = []

    def read_pages(self,filename):

        # Read page
        with open(filename,'r',encoding="mbcs") as file:
            data = file.readlines()

            my_data=[]
            for line in data:
                word = line.split()
                my_data.append(word)
       
        # convert all sub list to one list and remove the special characters also convert each word in lower case
        my_list = [re.sub(r'[^a-zA-Z0-9]','',(item.lower())) for sublist in my_data for item in sublist]

        # Remove duplicates value from list
        self.words_set = set(my_list)

    @staticmethod
    def write_file(filename,data):
        with open(filename,'w',encoding="mbcs") as file:
            file.write("Word : Page Numbers\n")
            file.write("-------------------\n")
            for i in data:
                file.write(f'{i}\n')
            print("Done!")
        
    @staticmethod
    def static_method(obj1,obj2,obj3,exclude):
        
        # exclude the words and also convert to set
        val1 = obj1.words_set.difference(exclude.words_set)
        val2 = obj2.words_set.difference(exclude.words_set)
        val3 = obj3.words_set.difference(exclude.words_set)

        # Find Common values from 3 sets
        page123 = val1.intersection(val2,val3)
        lst123 = [i + ' : 1,2,3' for i in page123]
        
        # Find Common values from page 1,2
        page12 = val1.intersection(val2)
        final_page12 = page12.difference(page123)
        lst12 = [i + ' : 1,2' for i in final_page12]

        # Find Common values fron page 1,3
        page13 = val1.intersection(val3)
        final_page13 = page13.difference(page123)
        lst13 = [i + ' : 1,3' for i in final_page13]

        # Find Common values from page 2,3
        page23 = val2.intersection(val3)
        final_page23 = page23.difference(page123)
        lst23 = [i + ' :2,3' for i in final_page23]
        
        # Find unique values from page 1
        page1 = val1.difference(page123,page12,page13)
        lst1 = [i + ' : 1' for i in page1]

        # Find unique values from page 2
        page2 = val2.difference(page123,page12,page23)
        lst2 = [i + ' : 2' for i in page2]

        # Find unique values from page 3
        page3 = val3.difference(page123,page13,page23)
        lst3 = [i + ' : 3' for i in page3]

        # Merge all the lists into final list and sort the final list alphabetically.
        lst = lst1+lst2+lst3+lst12+lst23+lst13+lst123
        Task.final_lst = sorted(lst)
        return Task.final_lst

        
if __name__ == '__main__':
    obj1 = Task()
    obj1.read_pages(filename="Page1.txt")

    obj2 = Task()
    obj2.read_pages(filename="Page2.txt")

    obj3 = Task()
    obj3.read_pages(filename="Page3.txt")

    exclude = Task()
    exclude.read_pages(filename="exclude-words.txt")

    data = Task.static_method(obj1,obj2,obj3,exclude)
    Task.write_file(filename = 'index.txt',data=data)
