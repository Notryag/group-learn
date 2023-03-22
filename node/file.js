const fs = require("fs")
// 读取文件
// 同步
const data = fs.readFileSync("./path.js", "utf-8")
console.log("data: ", data)
// 异步
fs.readFile("./path.js", "utf-8", (err, data) => {
  if (err) {
    console.log("err: ", err)
    return
  }
//   console.log("data: ", data)
})

// 文件流
const readStream = fs.createReadStream("./path.js", "utf-8")
readStream
  .on("data", (chunk) => {
    console.log("chunk: ", chunk)
  })
  .on("error", (error) => {
    console.log("error: ", error)
  })
  .on("end", () => {
    console.log("end")
  })
  .on("close", () => {
    console.log("close")
  })

// 写入文件
// 同步写入
fs.writeFileSync('./fstest.js', 'console.log("hello world")')
// 异步写入
fs.writeFile('./fstest.js', 'console.log("hello me")', (err) => {
    if (err) {
        console.log("err: ", err)
        return
    }
    console.log("success")
})

// 文件流写入
const writeStream = fs.createWriteStream('./fstest.js', 'utf-8')
writeStream.on("close", () => {
    console.log("write close")
})
writeStream.write("console.log('write by stream')\n")
writeStream.write("console.log('write by stream2')")
writeStream.end()

文件追加写入
fs.appendFileSync('./fstest.js', "console.log('append by sync')\n")

fs.appendFile('./fstest.js', 'console.log("append")', (err) => {
    if(err) throw err
    console.log("append success")
})

// 文件拷贝
fs.copyFileSync('./fstest.js', './fstest2.js')
// del file, can not del dir
fs.unlinkSync('./fstest2.js')
// 监听文件改动 返回的内容不通
// 新旧内容对比
fs.watchFile('./fstest.js', {interval: 2000}, (curr,prev) => {
    console.log('watchFiel', curr, prev)
})
// 事件名 文件名
fs.watch('./fstest.js', (eventType, filename) => {
    console.log('watch', eventType, filename)
})

// 创建目录 同步和异步
fs.mkdirSync("./test")
fs.writeFileSync("./test/test.js", 'console.log("test")')
// 非空文件夹,会报错🤣
fs.rmdirSync('./test')

const files = fs.readdirSync(__dirname, "utf-8")
console.log("files: ", files)

fs.renameSync("./test", "./test2")

const stat = fs.statSync("./test/test.js")

console.log(stat.isFile(), stat.isDirectory(), stat)
