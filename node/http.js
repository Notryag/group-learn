const http = require("http")
const url = require("url")


// const serve = http.createServer((req, res) => {
//   res.writeHead(200, { "Content-Type": "text/plain" })
//   console.log("1、客户端请求url：" + req.url)
//   console.log("2、http版本：" + req.httpVersion)
//   console.log("3、http请求方法：" + req.method)
//   // 这里使用JSON.stringify是为了方便在控制台查看，实际上是一个对象可以直接使用
//   console.log("4、http请求头部" + JSON.stringify(req.headers))
//   const params = url.parse(req.url, true).query
//   console.log("5、url参数：" + JSON.stringify(params))

//   res.write("hello")
//   res.end("world")
// })

const server = http.createServer((req, res) => {
    let body = ''
    req.on('data', (thunk) => {
        console.log('thunk:', thunk, (typeof thunk), Object.prototype.toString.call(thunk))
        body += thunk
    })

    req.on('end', () => {
        console.log('body:', body)
        res.end('ok')
    })
})


server.listen(3000, () => {
  console.log("server is running at http://localhost:3000")
})

server.on("close", () => {
  console.log("server is closed")
})

server.on("error", (err) => console.log(err))
