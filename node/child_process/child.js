process.on("message", (message) => {
  console.log(`message from parent: ${message}`)
})

process.send("hello from child")
