daum_openapi
----

Python library for Daum Open Data API. 



Features
- JSON response keys to class member variables. 
- Convert XML response to JSON and then keys to class member variables. 

```
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

Provided data api category:
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
