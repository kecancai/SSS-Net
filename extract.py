# 提取 包含关键字 Accuracy 的行 到另一个文件 
# f = open('/home/ckc/workspaces/remote_36/result/s_128/128_s_delate_p1_p2/2021-12-21 16--57 cifar10_0.9_s_acc.txt','r',encoding='utf-8')
# list1 = []
# lines = f.readlines()
# for lines in lines:
#     if "Accuracy" in lines:
#         #print(lines)
#         list1.append(lines)
# with open('/home/ckc/workspaces/remote_36/result/s_128/128_s_delate_p1_p2_0.9.txt', 'a') as month_file:  # 提取后的数据文件
#     for line in list1:
#         s = (line)
#         month_file.write(s)


# # 提取某列的数据到新的文件
f = open('/home/ckc/workspace/final_results/cifar100/cluster/checkpoint_spectral/cifar100_0.8_acc.txt','r',encoding='utf-8')
list1 = []
lines = f.readlines() 
for lines in lines:
    list1.append(lines)
with open('/home/ckc/workspace/final_results/cifar100/cluster/checkpoint_spectral/mini_0.8_acc.txt', 'a') as file:  # 提取后的数据文件
    for line in list1:
        s = (line[-6:-1]+'\n')
        file.write(s)
file.close()


# 提取偶数列数据文件
# with open('/home/ckc/workspace/final_results/cifar100/checkpoint_s_T_h_ac_0.1/cifar100_0.8_AUC.txt', 'r') as file:  
#     list2=[]
#     lines = file.readlines()
#     i=0
# with open('/home/ckc/workspace/final_results/cifar100/checkpoint_s_T_h_ac_0.1/cifar100_0.8_AUC.txt', 'w') as file:  # 提取偶数列数据文件
#     for line in lines:
#         i +=1
#         if i%2 ==0:
#             file.write(line)

