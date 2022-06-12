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
    - `hello2` uses arrow syntax, which is the same as `hello1` for the most part (difference revealed in chapter 6: [arrow functions do not bind `this`, but see `this` of the surrounding scope](https://eloquentjavascript.net/06_object.html#p_C4AqzW0fAV))
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

* `forEach`, `filter`, `map` and `reduce` are built-in. [`reduce` is clever with the start element](https://eloquentjavascript.net/05_higher_order.html#p_r9cFmJJTar)
* `some` tests whether at least one element satisfies the given predicate
* `every` tests whether all elements in an array satisfy the given predicate
* `findIndex` returns the index of the first element satisfying the given predicate
* [JS strings use UTF-16 encoding](https://eloquentjavascript.net/05_higher_order.html#p_UsDhhqR3EH)
* [Some problems when using string `length` and index access. `charCodeAt` and `codePointAt` are tricky, too](https://eloquentjavascript.net/05_higher_order.html#p_iQl/Gok4Mf)

### 6. The Secret Life of Objects

`this`:

* `this` points to the object a method was called on
* [This works even for functions assigned to objects later](https://eloquentjavascript.net/06_object.html#p_N+6e0UGvFo). [Using the `call` method on a function, the `this` context can be set explicitly](https://eloquentjavascript.net/06_object.html#p_llBwR5t6LB)
* [Arrow functions do not bind `this`, but see the `this` of the surrounding scope](https://eloquentjavascript.net/06_object.html#p_C4AqzW0fAV)

[Prototypes](https://eloquentjavascript.net/06_object.html#h_SumMlRB7yn):

* Unknown properties are requested from an object's prototype and from the prototype's prototype etc.
* The root prototype is `Object.prototype`
* `Object.getPrototypeOf` gets the prototype of the passed object. The prototype of the root prototype is `null`
* [Functions derive from `Function.prototype` and arrays from `Array.prototype`](https://eloquentjavascript.net/06_object.html#p_j+MLWf3JXr)
* [`Object.create` is used to create an object of a given prototype](https://eloquentjavascript.net/06_object.html#p_H2XhzSHHJP)
* [Shorthand for defining a method in an object (notice `speak`)](https://eloquentjavascript.net/06_object.html#c_gSGrvGTpkW):

    ```js
    let protoRabbit = {
      speak(line) {
        console.log(`The ${this.type} rabbit says '${line}'`);
      }
    };
    ```

* `new` is used to invoke a constructor function
* By convention, private property names start with `_`
* [A constructor function can be seen as a type/class from other languages. Its prototype defines the set of methods](https://eloquentjavascript.net/06_object.html#p_j8irpNziDb)
* [Capitalize constructor function names (again, matching other languages' class feature)](https://eloquentjavascript.net/06_object.html#p_DJG7BO1oTU)
* [Same can be achieved with the `class` notation and defining the special `constructor` method inside a class](https://eloquentjavascript.net/06_object.html#h_hPv1gHC33s)
* [Class name is optional for class expressions](https://eloquentjavascript.net/06_object.html#p_pp17mMu8If). Q: what's the use-case for class expressions?
* Overriding of properties can be done on prototype- and object-level (instance-level)

Maps:

* [Using normal objects as maps is dangerous](https://eloquentjavascript.net/06_object.html#h_gAcc11EHzV), e.g. because they contain additional "keys" due to inheriting properties from `Object.prototype`
* [One solution is to create objects with `null` prototype and use them as maps](https://eloquentjavascript.net/06_object.html#p_enf1/9ItBM):

    ```js
    let map = Object.create(null);
    ```

* Object property names must be strings. So when using an object as a map, only string keys are allowed
* [JS has a `Map` class](https://eloquentjavascript.net/06_object.html#p_nIsq9E5wmZ) with `set`, `get` and `has` operations
* [`Object.keys` returns only an object's own properties, not the ones from its prototype](https://eloquentjavascript.net/06_object.html#p_tx3xnowcEp)
* The `in` operator checks for the property both in the object and its prototype
* The `hasOwnProperty` method checks only for the object's properties, not those from the prototype

Polymorphism and Symbols:

* JS supports polymorphism. Objects fulfill an interface, if they have properties with matching names (or matching symbols)
* [Each `Symbol` is unique, even when created with the same name](https://eloquentjavascript.net/06_object.html#p_7p+O+Qr4bN)

Iterators:

* Objects fulfill the iterator interface when they [have a method labeled with the `Symbol.iterator` symbol](https://eloquentjavascript.net/06_object.html#h_z2tOOXM8qO)
* [String iterator example](https://eloquentjavascript.net/06_object.html#p_wSWGcm7dId), [custom matrix iterator example](https://eloquentjavascript.net/06_object.html#p_rqXAzunzIi)

Getters, setters, static:

* [`get`, `set` keywords define opaque getter/setter functions that look like regular field properties](https://eloquentjavascript.net/06_object.html#h_3vwredi8nD)
* [`static` functions are bound to the constructor (class name), not to the prototype](https://eloquentjavascript.net/06_object.html#p_MwIs1kR0mD)

Inheritance:

* [`extend` keyword extends a class from another prototype than the default `Object.prototype`](https://eloquentjavascript.net/06_object.html#p_a3GMshNFYT)
* Use `super` to call superclass constructor and `super.propertyName` to use superclass property `propertyName`
* Use `instanceof` operator to check whether an object has some class (constructor) somewhere in its inheritance hierarchy

### 7. Project: A Robot

* [`Object.freeze` makes an object immutable, all write operations are ignored](https://eloquentjavascript.net/07_robot.html#h_BgRu2ZQp4Z)

### 8. Bugs and Errors

* Enable strict mode by writing the following line at the beginning of a file or function body:

    ```js
    "use strict";
    ```

* Strict mode reports:

    - Usage of undefined bindings (normally, they'd be created implicitly in global scope)
    - `this` will be `undefined` in function scope when the function is not used as a method (normally, `this` would then refer to global scope)
    - Defining function parameters with the same name
    - Removes `with` statement and other problematic language features

* [Calling constructors defined with `class` keyword without `new` will always result in an error](https://eloquentjavascript.net/08_error.html#p_WGJIyAOZ/i)
* Use [TypeScript](https://www.typescriptlang.org/)

Debugging:

* Inserting `debugger` statement will pause program execution when browser developer tools are open

Exceptions:

* Raising an exception:

    ```js
    throw new Error("message");
    ```

* Handling an exception:

    ```js
    try {
        throwsException();
    } catch (error) {
    } finally { // Is always run
    }
    ```

* [`Error` objects have `message` and `stack` properties](https://eloquentjavascript.net/08_error.html#p_lP6PP0CCrB)
* [JS doesn't differentiate exception types (it's all just `Error`)](https://eloquentjavascript.net/08_error.html#p_3umLtBJgPo)
* [However, defining own error types by extending `Error` and checking with `instanceof` is recommended](https://eloquentjavascript.net/08_error.html#p_qurSIk3pjE)

### 9. Regular Expressions ([Summary](https://eloquentjavascript.net/09_regexp.html#h_ErccPg/l98))

* [Two ways to define RegEx patterns](https://eloquentjavascript.net/09_regexp.html#h_5w4yGFJRYl):

    ```js
    let regExConstructor = new RegExp("abc");
    let regExLiteral = /abc/;

    let caseInsensitiveFlag = /abc/i;
    let constructorFlags = new RegExp("abc", "giuy");
    ```

* [Escaping rules vary by which definition style is used](https://eloquentjavascript.net/09_regexp.html#p_0mNIcPpslS), e.g. in RegEx literals `/` needs to be escaped, backslashes don't must not be escaped. In RegEx strings passed to `RegExp` constructor, backslashes need to be escaped.
* `test` method checks whether a passed string matches the RegEx
* [`exec` method returns a match with `index` property or `null` if no match is found](https://eloquentjavascript.net/09_regexp.html#h_CV5XL/TADP). A match object looks like the matched string
* String objects have a `match` method accepting a RegEx parameter that behaves like RegEx `match`
* [Common built-in character groups](https://eloquentjavascript.net/09_regexp.html#p_1qtYlDfA/1)
* [Group matching rules](https://eloquentjavascript.net/09_regexp.html#p_/9rdcJO9zZ)
* `^` matches start of string, `$` matches end of string, `\b` matches word boundary
* `.` matches any non-newline character, [if any character incl. newline needs to be matched, `[^]` can be used](https://eloquentjavascript.net/09_regexp.html#p_DkzBCJQQdu)
* Repetition operators are greedy (match as much as possible) by default, [non-greedy (match as little as possible) ones are followed by a `?`](https://eloquentjavascript.net/09_regexp.html#p_eNtLSVH65f)
* [Sanitize input before constructing RegExp objects from user input](https://eloquentjavascript.net/09_regexp.html#p_UPAgEiKHfS)
* [Looping over matches is possible](https://eloquentjavascript.net/09_regexp.html#i_m0fs21dHEg)
* [Use `u` (unicode) flag to properly match non-ASCII characters](https://eloquentjavascript.net/09_regexp.html#h_+y54//b0l+)

[Date](https://eloquentjavascript.net/09_regexp.html#h_8U7L7LCU27):

* Month numbers start at 0, day numbers at 1

String `replace`:

* Accepts RegEx as first argument and [even matched groups in the second argument](https://eloquentjavascript.net/09_regexp.html#p_/5YU/Qo2Np). [By default, just replaces the first occurence](https://eloquentjavascript.net/09_regexp.html#p_jjBKX9l81o)
* To replace all occurences, end RegEx with `g` flag (similar to `i` flag above and other RegEx implementations)
* [The second argument may also be a function applied for every replacement](https://eloquentjavascript.net/09_regexp.html#p_BpgnqwKFHn)

String `search`:

* Like `indexOf`, but searching for first position matching pattern
* [Searching for `lastIndex` is tricky](https://eloquentjavascript.net/09_regexp.html#h_duFTd2hqd0), `y` is "sticky" flag (= RegEx must be found starting at lastIndex, by default: from beginning of string)

[Example: parse INI file](https://eloquentjavascript.net/09_regexp.html#h_RGsf6ah1EY)

### 10. Modules

* [Use `Function` as a safe alternative to `eval` if data needs to be executed as code](https://eloquentjavascript.net/10_modules.html#p_wzjzmC3uLa)
* [`require` and `exports` come from CommonJS and is used by Node.js](https://eloquentjavascript.net/10_modules.html#h_N33QHgUxbG)
* [Modern JS has `import` and `export` built-in](https://eloquentjavascript.net/10_modules.html#p_fGE1JkAJHH)
* `export default` specifies the module's main export which may not even have a name

`ini` and `dijkstrajs` packages from NPM are mentioned.

### 11. Asynchronous Programming

* `setTimeout(callback, delayInMs)`

Promises:

* [`Promise`: object which is executed may produce a value at some time in the future](https://eloquentjavascript.net/11_async.html#p_c7IGxt0qcZ)
* `Promise.resolve` wraps a value in a Promise
* `then` method gets the value produced by the Promise, applies the passed callback function and produces another Promise. This way, `then` and callbacks can be chained (without confusing callback nesting)
* [`Promise` constructor accepts a function which is immediately called with a resolve function as an argument](https://eloquentjavascript.net/11_async.html#p_sPGdi+3o75)
* [`Promise.reject` creates a Promise failure](https://eloquentjavascript.net/11_async.html#p_/Duy2d2EJl)
* `catch` gets the reason why the Promise failed and returns a Promise, similar to `then` for the non-erroneous case
* The `catch` handler may also be registered as the second optional argument to `then`, for convenience

paused at https://eloquentjavascript.net/11_async.html#h_o8Vlf60I8f


### [12. Project: A Programming Language](https://eloquentjavascript.net/12_language.html)

### [13. JavaScript and the Browser](https://eloquentjavascript.net/13_browser.html)

* Basics on TCP, client-server, URL structure, HTTP, HTML, how to include JS in HTML

### [14. The Document Object Model](https://eloquentjavascript.net/14_dom.html)

* DOM, Trees
* [`document` is the DOM root, `document.documentElement` the enclosing `<html>` tag](https://eloquentjavascript.net/14_dom.html#p_ltiXfOMPcl)
* [Each DOM node has a `nodeType` property](https://eloquentjavascript.net/14_dom.html#p_f2BdWNSlpJ)
* [`childNodes` property is of `NodeList` type stemming from DOM standardization](https://eloquentjavascript.net/14_dom.html#p_feaMhbBocX)
* [childNodes, firstChild, lastChild, previousSibling, nextSibling, parentNode visualized](https://eloquentjavascript.net/14_dom.html#h_ShZPVipWw/)
* [`children` property contains only element child nodes](https://eloquentjavascript.net/14_dom.html#p_EXYoCGtRP4)
* `nodeValue` of a text node contains its text

[Finding elements:](https://eloquentjavascript.net/14_dom.html#h_jS5BEpmLY0)

* All element nodes have `getElementsByTagName`, e.g. `document.body`
* `document.getElementById`
* `getElementsByClassName`

[Changing the document:](https://eloquentjavascript.net/14_dom.html#h_npiFAJENvT)

* `remove`, `appendChild`, `insertBefore`
* Inserting/appending an existing node will first remove it and then insert it at the new position
* [`replaceChild`](https://eloquentjavascript.net/14_dom.html#p_PHkpqBpgHX)
* [`document.createTextNode`](https://eloquentjavascript.net/14_dom.html#p_zMqlQBb7H1)
* [`Array.from`](https://eloquentjavascript.net/14_dom.html#p_H+4G9MqWPh)
* [`document.createElement`](https://eloquentjavascript.net/14_dom.html#p_2LO1OJVEk3)
* Use `getAttribute` and `setAttribute` in combination with custom attributes (e.g. `data-something`), standard attributes may directly be accessed as properties
* The `class` attribute is accessed with `className` property or `getAttribute("class")`
* [`offsetWidth`, `offsetHeight`, `clientWidth`, `clientHeight` and `getBoundingClientRect`, `pageXOffset`, `pageYOffset` for position/size of HTML elements](https://eloquentjavascript.net/14_dom.html#h_lyrY2KUDl7)

Styling/CSS:

* [Accessing an element's `style` property](https://eloquentjavascript.net/14_dom.html#p_HcAoKCgOCF)
* [Rule precedence and specificity](https://eloquentjavascript.net/14_dom.html#p_7kmWmOHAMA)
* [Query selectors and `document.querySelectorAll` (returning a NodeList) and `document.querySelector` (returning just the first match)](https://eloquentjavascript.net/14_dom.html#h_5ooQzToxht)
* [`static`, `relative` and `absolute` position explained](https://eloquentjavascript.net/14_dom.html#h_MAsyozbjjZ)
* [Animation using `requestAnimationFrame`](https://eloquentjavascript.net/14_dom.html#p_TEJWNXCk6K)

### [15. Handling Events](https://eloquentjavascript.net/15_event.html)




## Further Reads

* [WTF JS: List of tricky JavaScript examples](https://github.com/denysdovhan/wtfjs)
* [Installing nvm and node.js](https://phoenixnap.com/kb/install-latest-node-js-and-nmp-on-ubuntu)
* [Web App Manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest)
