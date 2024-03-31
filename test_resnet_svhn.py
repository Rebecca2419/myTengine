import os

#change the path for different data
path="./images/test_SVHN_224"

# 返回path下所有文件构成的一个list列表
filelist=os.listdir(path)

correct=0
total = 0

# 遍历输出每一个文件的名字和类型
for item in filelist:
    # 输出指定后缀类型的文件
    if(item.endswith('.png')):
        total += 1
        im_id = item.split('.p')
        class_id = im_id[0].split('_')
        image=class_id[1] #use class name as the file name
        
        os.system("touch "+ image + ".txt")
        cmd="timeout 0.9 ./build/install/bin/tm_classification -t 8 -s 0.01938492,0.01966684,0.01951029 -w 125.307,122.961,113.8575\
            -m models_convert/resnet_SVHN.tmfile -i images/test_SVHN_224/" + item + " >&" + image + ".txt"
        os.system(cmd)
        
        #p = subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #stdout,stderr = p.communicate()
        #print('stdout : ',stdout)
        #print('stderr : ',stderr)

	    #读image.txt，if 正确 correct+=1
        f = open(image + ".txt", 'r')
        lines = f.readlines()
        result = lines[9].split(", ")
        my_class = result[1]
        
        if (my_class == image+'\n'):
            correct += 1

        f.close()
        os.remove(image + ".txt")
        
        accuracy = correct/total
        print('image: ', total, f"Accuracy: {accuracy:.4f}")
        
print("End here")
