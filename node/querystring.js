// querystring
const querystring = require("querystring")
const str = "nick=randy&age=24&nick2=%E4%B8%AD%E6%96%87"
const obj = querystring.parse(str)
console.log(obj)

const str1 = "name-randy|country-cn"
const obj1 = querystring.parse(str1)
console.log(obj1) // { 'name-randy|country-cn': '' }
const obj2 = querystring.parse(str1, "|", "-")
console.log(obj2) // { name: 'randy', country: 'cn' }

const obj4 = {
  nick: "randy",
  age: 24,
}

const str4 = querystring.stringify(obj4)
console.log("stringify", str4)

console.log("escape:", querystring.escape(str4)) // nick%3Drandy%26age%3D24

console.log("unescape:", querystring.unescape("nick%3Drandy%26age%3D24")) // nick=randy&age=24
