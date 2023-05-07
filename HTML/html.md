*5/6/23* <br/>
source: https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML

### Intro to HTML
* HTML (HyperText Markup Language) is a markup language that tells web browsers how to structure the web pages you visit.
* You can use NotePad for codes and save the extension as html.

* Anatomy of an HTML element <br/>
  ```<p>My cat is very grumpy</p>```
  * `<p>` means paragraph
  * `<p>` is the opening tag
  * My cat is very grumpy is the conetnt
  * `</p>` is the closing tag
  * The whole part is the element
  Code <br/>
     ``` <em> This is my text.</em>``` <br/>
  Output <br/>
*This is my text.*
* Nesting elements <br/>
  ```<p>My cat is <strong>very</strong> grumpy.```</p>
  Output <br/>
  My cat is __very__ grumpy.
* Block versus inline elements <br/>
  `</p>` is a block-level element. Each *p* element appears on a new line, with space above and below. <br/>
  `<em>` is an inline element. Elements sit on the same line, with no space in between.
* Void elements
  * A void element is an element that doesn't have any content and doesn't have a closing tag <br/>
  <img
  src="https://raw.githubusercontent.com/mdn/beginner-html-site/gh-pages/images/firefox-icon.png" alt="Firefox icon" />
* Attributes
  * Attributes contain extra information about the element that won't appear in the content. In the below example, the `<class>` attribute is an identifying name used to target the element with style information.<br/>
  ```<p class="editor-note">My cat is very grumpy</p>```
  * single or double quotes are both okay
* Whitespace in HTML
  * No matter how much whitespace you use inside HTML element content, the HTML parser reduces each sequence of whitespace to a single space when rendering the code. The reason why using whitespace is readability.
* HTML comments - wrap it in the special markers `<!-->` and `-->` <br/>
  Code <br/>
  ```<p> I'm not inside a comment</p>``` <br/>
  ```<!-- ,p.I am!</p> -->``` <br/>
  Output <br/>
  I'm not inside a comment

