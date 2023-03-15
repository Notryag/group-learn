const url = require('url')

const str = "http://user:password@randy.com:8080/index.html?nick=%E4%B8%AD%E6%96%87#part=1";

console.log(url.parse(str, true))
// format
const obj = {
    protocol: 'http:',
    slashes: true,
    auth: 'user:password',
    host: 'randy.com:8080',
    port: '8080',
    hostname: 'randy.com',
    hash: '#part=1',
    search: '?nick=%E4%B8%AD%E6%96%87',
    query: 'nick=%E4%B8%AD%E6%96%87',
    pathname: '/index.html',
    path: '/index.html?nick=%E4%B8%AD%E6%96%87',
    href: 'http://user:password@randy.com:88/index.html?nick=%E4%B8%AD%E6%96%87#part=1',
}
console.log(url.format(obj));

// resolve
console.log(url.resolve('http://www.baidu.com', '/index.html'))



