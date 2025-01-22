# for循环，语法如下
# for 变量 in 串行
# do
#    执行命令
# done

# 串行有多重表示方法，但是不能用数组，串行其实就是空格或者换行隔开的内容
for num in 122 "2" 3 4 5
do
    echo $num
done

# seq a b可以生成从a到b的串行
for num in `seq 1 10`
do echo $num
done

# 可以用{1..100}表示从1到100，{}表示扩展命令，a{1,2}b 相当于a1b a2b，扩展命令可以用..来表示从哪到哪，比方说{1..9}和{a..z}，如果无法解析则直接返回{x..x}
# 注意shell里不要乱用空格！！！
for num in a{a..c}b
do echo $num
done

# while循环，语法如下
# while 条件测试，和流程控制中，if条件一样，（（））和[[]]
# do
#   执行命令
# done

# 注意定义数字要用declare
declare -i num=1
while [[ $num -le 100 ]]
do
    echo $num
    num=$num+1
done

# until循环，和whild一样，只不过条件测试正好相反
# until 条件测试
# do
#   执行命令
# done
