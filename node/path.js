const path = require("path")

// 文件目录
console.log("__dirname: ", __dirname)
// 文件完整路径
console.log("__filename:", __filename)
// 父文件夹路径
console.log(path.dirname(__filename))
// 获取文件或文件夹名
console.log(path.basename(__filename))
console.log(path.basename(__filename, ".js"))
console.log(path.basename(__dirname))
// 指定文件扩展名
console.log(path.extname(__filename))
console.log(path.extname("index.html"))
// 当前系统分隔符 \为windows /为linux
console.log(path.sep)

// 格式化路径
console.log(path.normalize("C:\\temp\\\\foo\\bar\\..\\"))
console.log("---------------join----------------------")
console.log(path.join("C:\\temp", "foo", "bar", "baz\\asf", "quux", "..")) // C:\temp\foo\bar\baz\asf
console.log(path.join("/foo", "bar", "baz/asf", "quux", "..")) // \foo\bar\baz\asf
console.log(path.join("/foo", "bar", "..", "baz")) // \foo\baz
console.log(path.join("/foo", "bar")) // \foo\baz
console.log("------------resolve--------------------")
console.log(path.resolve("foo", "bar")) // D:\Code Space\project\group-learn\node\foo\bar
console.log(path.resolve("/foo", "bar")) // D:\foo\bar

console.log(path.isAbsolute("foo")) // false
console.log(path.isAbsolute(path.resolve(__filename))) // true
// 第二个参数相对于第一个参数的所在路径
console.log(path.relative("c:/a/b/c", "c:/houdunren/her")) // ..\..\..\houdunren\her

// 路径格式化
console.log(
  path.format({
    dir: "a/b/c",
    name: "path.js",
  })
)

console.log(path.parse(__filename))
console.log(path.parse(__dirname))

