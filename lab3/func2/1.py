movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]



#task 1
def movie(list):
    imdb2=float(list.get("imdb"))
    if imdb2>5.5:
        return True


#task 2
def sublist(list):
    sub=[]
    for x in list:
        if x["imdb"]>5.5:
            sub.insert(-1,x["name"])
        else: continue
    return sub


#task 3  
def category(list):
    name=str(input())
    films=[]
    for x in list:
        if x["category"]==name:
            films.insert(-1,x["name"])
        else: continue
    return films

#task 4
def average(list):
    sum=0
    for x in list:
        sum=sum+x["imdb"]
    return float(sum/15)
print(average(movie))

#task 5
def Category(name):
    lis1 = list()
    for x in movies:
        if x["category"] == name:
            lis1.append(x)
    total = 0
    i = 0
    while i < len(lis1):
        total += float(lis1[i]["imdb"])
        i += 1
    print(total / len(lis1)) 