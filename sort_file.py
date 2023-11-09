
""" C = [('e', 4, 'B'), ('a', 2, 'A'), ('c', 5, 'D'), ('b', 3, 'C'), ('d', 1, 'E')]
C.sort(key=lambda y: y[0])
print(C)

#输出[('a', 2, 1), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5), ('e', 4, 2)]
print(sorted(C, key=lambda x: x[0]))
#[('a', 2, 1), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5), ('e', 4, 2)]
print(sorted(C, key=lambda x: x[2]))
[('a', 2, 1), ('e', 4, 2), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5)]
 
 
  """

filenames = ['frame_0.png', 'frame_1.png', 'frame_10.png', 'frame_11.png']
# 关键在于如何取出文件中的数字字符，然后对数字进行排序
filenames.sort(key=lambda x: int(x.split(".")[0].split("_")[1]))  
print(filenames)
# 输出['frame_0.png', 'frame_1.png', 'frame_2.png', 'frame_3.png', 'frame_4.png', ...]