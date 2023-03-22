

console.log(process.env.NODE_ENV)

// 前2个参数是node.exe和当前文件的路径,后面的参数是命令行传递的参数
console.log("argv:", process.argv)
console.log("argv[0]:", process.argv[0])

console.log("process.execArgv", process.execArgv)

console.log("process cwd", process.cwd())

// console.log('process.config', process.config)

console.log("process.pid", process.pid)

process.title = "主进程"
console.log("process.title", process.title)

console.log("process.uptime", process.uptime())

console.log("process.version", process.version)

console.log("process.arch", process.arch)

process.nextTick(() => {
  console.log("process nextTick")
})

process.stdin.setEncoding("utf-8")

process.stdin.on("readable", () => {
    let chunk = process.stdin.read()
    if(chunk !== null) {
        process.stdout.write(`data: ${chunk}`)
    }
})

process.stdin.on("end", () => {
    process.stdout.write("stdin end")
})