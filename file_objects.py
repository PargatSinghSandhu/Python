#file = open('test.txt', 'r') #default mode is reading the file 
#print(file.name)

#context manager, it gives us a block to do anything in the block 
#and we dont have to explicitly close the file, as f.close, it automatically close
#close the file, this context manager helps in closing the file automatically
#prevents it from the resorce leaks 
#we can access the 'file' varible after the block ends, not that, 
#note that: we can not read or write file, as we are out of block
#but we can, check if the file is closed.

# with open('test.txt', 'r') as file:
#     pass

# print(file.closed)


#3

    
    # for line in file:
    #     print(line, end='')
    # file_contents = file.readlines()
    # print(file_contents, end='')
     
    # file_cont=file.read(10). #this is to print selected data 
    # print(file_cont, end ='')
    
# with open('test.txt', 'r') as file:   
    # size_to_read=2
    
    # file_contents = file.read(size_to_read)
    
    # while len(file_contents) > 0:
    #     print(file_contents, end='') #this prints the current chunk 
    #     file_contents = file.read(size_to_read) #after reading this the next 2 charactets read,
    #     #and updats with the new chuck, if there is no more content to read,
    #     #it returns an empty string
        
    
    # size_to_read = 3
    
    # file_contents = file.read(size_to_read)
    # print(file_contents, end = '')
    # file.seek(0)
    # file_contents = file.read(size_to_read) #it starts from the bgining
    # print(file_contents, end='')
    
# with open('test_sample.txt', 'w') as file:
#     file.write("write into the file") 
#     file.seek(0)
#     file.write("Open file")

#task is to copy text from one file to another

# with open('test.txt', 'r') as file1:
#     with open('test_sample.txt', 'w') as file2:
#         #now we need to go to each line so need loop
#         for line in file1:
#             file2.write(line)

#task: how to maange binary files or pictures 

# with open('/Users/pargatsingh/Desktop/Sample.png', 'rb') as file1:
#     with open('copy_image', 'wb') as file2:
#         for pixels in file1:
#             file2.write(pixels)


#if we need to do in chunks like size_to_read

with open('/Users/pargatsingh/Desktop/Sample.png', 'rb') as file1:
    with open('copy_image', 'wb') as file2:
        chunk_size = 2000
        rf_chunk = file1.read(chunk_size)
        while len(rf_chunk) >0:
            file2.write(rf_chunk)
            rf_chunk = file1.read(chunk_size)
