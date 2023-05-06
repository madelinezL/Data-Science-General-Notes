```let``` allows you to declare block-level variables. The declared variable is available from the block it is enclosed in.
```
let a;
let name = "Simon";

// myLetVariable is *not* visible out here

for (let myLetVariable = 0; myLetVariable < 5; myLetVariable++) {
  // myLetVariable is only visible in here
}

// myLetVariable is *not* visible out here
```

```const``` allows you to declare variables whose values are never intended to change. The variable is available from the block it is declared in.
```
const Pi = 3.14; // Declare variable Pi
console.log(Pi); // 3.14
```
