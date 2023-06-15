# 大概介绍一下shell编程

# shell是一个命令行解释器，向用户提供了一个面向linux内核发送请求以便运行程序的界面系统程序，用户可以通过shell来启动、挂起甚至来编写一些程序；
# shell的作用是解释用户执行的命令，用户输入一条指令，shell就解释并执行一条命令，有点像python。
# 当然shell的使用可以更方便，即批处理，用户事先写好一个shell脚本（sh），其中有很多命令，shell可以运行这个脚本将命令一次性执行完；

# 由于历史原因，UNIX系统上有很多种Shell：
# sh（Bourne Shell）：由Steve Bourne开发，各种UNIX系统都配有sh。
# csh（C Shell）：由Bill Joy开发，随BSD UNIX发布，它的流程控制语句很像C语言，支持很多Bourne Shell所不支持的功能：作业控制，命令历史，命令行编辑。
# ksh（Korn Shell）：由David Korn开发，向后兼容sh的功能，并且添加了csh引入的新功能，是目前很多UNIX系统标准配置的Shell，在这些系统上/bin/sh往往是指向/bin/ksh的符号链接。
# tcsh（TENEX C Shell）：是csh的增强版本，引入了命令补全等功能，在FreeBSD、MacOS X等系统上替代了csh。
# bash（Bourne Again Shell）：由GNU开发的Shell，主要目标是与POSIX标准保持一致，同时兼顾对sh的兼容，bash从csh和ksh借鉴了很多功能，是各种Linux发行版标准配置的Shell，在Linux系统上/bin/sh往往是指向/bin/bash的符号链接。虽然如此，bash和sh还是有很多不同的，一方面，bash扩展了一些命令和参数，另一方面，bash并不完全和sh兼容，有些行为并不一致，所以bash需要模拟sh的行为：当我们通过sh这个程序名启动bash时，bash可以假装自己是sh，不认扩展的命令，并且行为与sh保持一致。

