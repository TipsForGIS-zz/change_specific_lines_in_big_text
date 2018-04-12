# open a distnation file for saving the updated text
# if output.txt does not exist, python will create one
# if it exists, it will overwrite it
f_dist = open('./output.txt','w')

# open the source file in read mode, sample.txt should exist
# using the with statement is better for memory management
# because it reads one line at a time in memory instead of the whole file
with open('./sample.txt', 'r') as f_source:
    for idx,line in enumerate(f_source):
        if idx in (4,21,200001,70,555,6632,10023,700):
            f_dist.write('>>> *** ^^^ some updated text ^^^ *** <<<\n')
        else:
            f_dist.write(line)


# close the distination file to release lock and memory
f_dist.close()

print('Successful!')