f = open('record.txt')

boy = []
girl = []
count = 1
for each_line in f:
    if each_line[:6] != '======':
        (role, line_spoken) = each_line.split(':', 1)
        if role == 'dudu':
            boy.append(line_spoken)
        if role == 'mama':
            girl.append(line_spoken)
        #我们这里进行字符串分割操作
    else:
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()

        boy = []
        girl = []
        count += 1

f.close()


        #文件的分别保存操作
            
