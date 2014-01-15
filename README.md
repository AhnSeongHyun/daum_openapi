daum_openapi
----
<br/>
[![Build Status](https://travis-ci.org/AhnSeongHyun/daum_openapi.png)](https://travis-ci.org/AhnSeongHyun/daum_openapi)
<br/>

Python library for Daum Open Data API. 
<br/> 
<h4>Install</h4>
```
pip install daum_openapi
```
<br/> 
<h4>Features</h4>
- JSON response keys to class member variables. 
- Convert XML response to JSON and then keys to class member variables. 

```
from daum_openapi.search import search
sc = search(API_KEY)
result =  sc.blog(u'coldplay', 10, 1, 'date', 'xml');
      
{
  "channel":
  {
    "result":"10",
    "pageCount":"800",
    "title":"Search Daum Open API"
    "item": [
              {"title":"Coldplay - viva la vida", "description":"viva la vida new song"},
              {"title":"YELLOW", "description":"Yellow lyrics"}
            ]
            
  }
}

=> result.channel.result               //"10"
=> result.channel.pageCount            //"800"
=> result.channel.title                //"Search Daum Open API"
=> result.channel.item[0].title        //"Coldplay - viva la vida"
=> result.channel.item[1].description  //"Yellow lyrics"
```
<br/> 
<h4>Provided data api category:</h4>
- contents
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/movie">movie</a>
- search
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/blog">blog</a>
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/cafe">cafe</a>
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/board">board</a>
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/web">web</a>
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/knowledge">knowledge</a>
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/image">image</a>
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/vclip">vclip</a>
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/book">book</a>
- socialpick
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/Socialpick-search">search</a>
- shopping
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/Shopping-search">search</a>
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/Shopping-detail">detail</a> 
- local
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/addr2coord">addr to coord</a>
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/coord2addr">coord to addr</a>
  - <a href="https://github.com/AhnSeongHyun/daum_openapi/wiki/transcoord">trans coord</a>


<h4>License</h4> 

Released under the MIT license.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.