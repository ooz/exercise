# JavaScript

I recently discovered ["Eloquent JavaScript" by M. Haverbeke](https://eloquentjavascript.net) which seems to be a common introduction to both programming and JavaScript, e.g. for bootcamp students.
So far, I followed a conservative philosophy of "the least amount of JS you can get away with" and thus my JS skills are limited:

* Static page tools: [Lifetime Clock](https://oliz.io/lifetime-clock/), [Kitchen Cleaning Plan](https://github.com/ooz/kitchen-cleaning-plan) (somewhat modular, [with tests run in browser](https://oliz.io/kitchen-cleaning-plan/test.html))
* Minor accessibility features in vanilla JS used in [ggpy](https://github.com/ooz/ggpy): https://github.com/ooz/templates/blob/master/html/oz-accessibility.js
* Unoptimized, non-modular Electron app using React.js: https://github.com/ooz/flow-charter
* Unoptimized, non-modular game jam games using [Phaser](https://phaser.io/): [Ogre Forge](https://oliz.io/ogre-forge/), [home is](https://oliz.io/home-is/), [Handshake](https://oliz.io/handshake/)

Study goals:

* Level-up JS skills, understand prototypic features
* Learn and write modern JS instead of a mix of various language features/standards
* Understand JS module system, dependency management, bundling and webpack
* Get started with Node.js, learn basic API

## My Learnings

(As a person with extensive programming and CS background, ymmv.)

### 1. Values, Types, and Operators

> [Calculations with whole numbers [...] smaller than the aforementioned 9 quadrillion are guaranteed to always be precise.](https://eloquentjavascript.net/01_values.html#p_8KgYC0F1fX)

> [There is only one value in JavaScript that is not equal to itself, and that is NaN (“not a number”).](https://eloquentjavascript.net/01_values.html#p_tLooHn2QPj)
> [NaN is supposed to denote the result of a nonsensical computation, and as such, it isn’t equal to the result of any other nonsensical computations.](https://eloquentjavascript.net/01_values.html#p_rcMZUIfGYR)

### 2. Program Structure

* [For beginners, the author recommends to always terminate statements with semicolons, because omission rules are non-trivial.](https://eloquentjavascript.net/02_program_structure.html#p_z/83KOxUGo)
* [`let` defines a *binding* (aka variable)](https://eloquentjavascript.net/02_program_structure.html#p_jG4q4gLJDw)
* [There's no reason to use `var` over `let` in modern JS](https://eloquentjavascript.net/02_program_structure.html#p_IvQMyQVoj9)
* [Write JS in camelCase](https://eloquentjavascript.net/02_program_structure.html#p_GveY0yoCxZ)

### 3. Functions

* Three ways to define functions:

    ```js
    const hello1 = function(name) { return "Hello " + name; };
    const hello2 = (name) => { return "Hello " + name; };
    function hello3(name) { return "Hello " + name; }
    ```

    - `hello1` and `hello2` use binding notation (binding a function value to the respective names)
    - `hello2` uses arrow syntax, which is the same as `hello1` for the most part ([difference will be revealed in chapter 6](https://eloquentjavascript.net/03_functions.html#p_UKyLgbrDUa)
    - `hello3`-style function declarations are read before the JS program is executed, so the function can be used before it is defined. `hello1` and `hello2` need to be defined before their usage
    - Also mind the semicolon terminating `hello1` and `hello2` definitions

* [JS ignores excessive arguments passed to functions](https://eloquentjavascript.net/03_functions.html#p_JyyXKkZ6u6)
* [If too few arguments are passed, the affected parameters become `undefined`](https://eloquentjavascript.net/03_functions.html#p_kzCivbonMM)
* [Avoid recursion](https://eloquentjavascript.net/03_functions.html#p_0kxF7WAzdn), JS has no tail nor optimized recursion

### 4. Data Structures: Objects and Arrays

* Two ways to access a property:

    ```js
    name.prop;
    name[prop]; // Expression "prop" is evaluated and the property with the resulting index/name accessed
    ```

    - The second way may be used to work around invalid property names e.g. starting with numbers

* [`array.length` and `array["length"]` are the same](https://eloquentjavascript.net/04_data.html#p_Bcq+Q3kiI4)
* [Use binary `in` operator to check whether an object has a property, use unary `delete` operator to delete a property from an object](https://eloquentjavascript.net/04_data.html#c_66M3B1wG98)
* [Use `Object.keys(myObj)` to get all property names of object `myObj`](https://eloquentjavascript.net/04_data.html#p_SvMW6lxfp+)
* [Use `Object.assign(left, right)` to copy all properties from `right` to `left`](https://eloquentjavascript.net/04_data.html#p_z4/OPZzTTK)
* [`typeof []` is `"object"`](https://eloquentjavascript.net/04_data.html#p_Rl8msr9DUz)
* [`==` checks for identity (reference to same object), not (deep) equality of contents](https://eloquentjavascript.net/04_data.html#p_wD7jhXt+Tr)
* [`{some, other}` is a shorthand for `{some: some, other: other}`](https://eloquentjavascript.net/04_data.html#c_CI+dtzXW/x)

([nice phi coefficient example to measure correlation between two variables](https://eloquentjavascript.net/04_data.html#p_mq//xARuKm))

* [`array.includes(elem)` checks whether `elem` is in `array`](https://eloquentjavascript.net/04_data.html#p_1/7IsMpwdF)
* Further array methods: `shift` (pop first element), `unshift` (insert at beginning of array), `indexOf` (find first), `lastIndexOf` (find last), `slice`, `concat`
* For strings, `indexOf` can also search for substrings with length greater than 1
* [String padding with `padStart`](https://eloquentjavascript.net/04_data.html#p_pSkK9k9R0g)
* Further string methods: `trim`, `split`, `join`, `repeat`
* [Rest parameters and spread operator `...`](https://eloquentjavascript.net/04_data.html#h_hX9DkIBp9y)
* [Re-using a name for a binding defined with `let` or `const` will trigger a warning, but not for `var` or `function`!](https://eloquentjavascript.net/04_data.html#p_6OHrUF+WEc)
* [Destructuring arrays and objects](https://eloquentjavascript.net/04_data.html#h_B372u36cp6)
* [`JSON.stringify` and `JSON.parse`](https://eloquentjavascript.net/04_data.html#p_1IU60Zh2Af)

### 5. Higher-Order Functions

https://eloquentjavascript.net/05_higher_order.html


## Further Reads

* [WTF JS: List of tricky JavaScript examples](https://github.com/denysdovhan/wtfjs)
