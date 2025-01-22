# shell脚本中的流程控制
# 值得特殊说明的是，在shell中 0代表true，其余值都代表false

# test命令和[]命令，可以将命令中的布尔表达式进行计算，并映射返回退出的值：0为true，其余为false；
# 注意：[ xxx ] 方括号里边左右要有空格
# 数值对比：-lt 表示小于；-le 小于等于；-gt 大于；-ge 大于等于；-eq 等于；
# 字符串对比：= 等于；!= 不等于；-n 字符串长度不为0；-z 字符串长度为0；
[ 1 = 1 ] && echo $?

# if condition 
# then body
# elif condition
# then body
# else body
# fi

if [ -z $1 ]
then echo "未输入任何的值"
elif [ $1 -eq 1 ]
then echo "输入的值是1"
elif [ $1 -ge 2 ]
then echo "输入的值大于等于2"
else echo "输出的值是其他值"
fi

# 针对条件表达式，[]的使用会有一些不稳，推荐使用[[]]来使用更为丰富的表达式，且能兼容未输入的场景
if [[ $1 = 1 ]]
then echo "success"
fi

# 同等的，还有case in，相当于switch case方法，;;相当于break
# case condition in
#   pattern1)
#   body
#   ;;
# esac

case $1 in
    100)
    echo "当前输入的值是100"
    ;;
    10[0-9])
    echo "当前输入的值处于100到200之间"
    ;;
    *)
    echo "当前输入的值是1以外的值"
    ;;
esac # 标识case结束
# pattern其实是一种正则表达式，可以使用[0~9]之类的来表示

# 参考网址：https://blog.csdn.net/oqqHuTu12345678/article/details/125662997