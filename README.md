# imagerecognition.ml
An Image recognition service based on Flask and Tensorflow. The dependencies include `flask`, `flask_restful`, `numpy`, `tensorflow`

https://github.com/rjmasikome/imagerecognition.ml/

## Installation
1. Run `setup.py`
2. Run `api.py`

## Usage
### `/api`
* Query: `url` - The url of Image that you want to classify
* Example call: 
```
https://imagerecognition.ml/api?url=https://www.petfinder.com/wp-content/uploads/2012/11/91615172-find-a-lump-on-cats-skin-632x475.jpg`
```
* On Success: 
```js
{
  url: "https://www.petfinder.com/wp-content/uploads/2012/11/91615172-find-a-lump-on-cats-skin-632x475.jpg",
  res: [
    {
      class: [
        "Egyptian cat"
      ],
      score: 0.60871
    },
    {
      class: [
        "tabby",
        "tabby cat"
      ],
      score: 0.12714
    },
    {
      class: [
        "lynx",
        "catamount"
      ],
      score: 0.07766
    },
    {
      class: [
        "tiger cat"
      ],
      score: 0.07641
    },
    {
      class: [
        "cougar",
        "puma",
        "catamount",
        "mountain lion",
        "painter",
        "panther",
        "Felis concolor"
      ],
      score: 0.00148
    }
  ]
}
```
* On Error:
```js
{
  description: "Image not found on the url",
  status: 404,
  message: "You have requested this URI [/api] but did you mean /api ?"
}
```

## Disclaimer
* `classify.py` is modified from https://github.com/tensorflow/models
* The example url is based on the first result of google with keyword `cat`
