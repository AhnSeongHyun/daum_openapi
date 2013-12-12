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
  - movie
- search
  - blog
  - cafe
  - board
  - web
  - knowledge
  - image
  - vclip
  - book
- socialpick
  - search
- shopping
  - search
  - detail 
- local
  - addr to coord
  - coord to addr
  - trans coord
