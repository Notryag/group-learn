console.log(process.env.NODE_ENV)

console.log(process.env)
// 前2个参数是node.exe和当前文件的路径,后面的参数是命令行传递的参数
console.log("argv:", process.argv)
console.log("argv[0]:", process.argv[0])

console.log("process.execArgv", process.execArgv)
