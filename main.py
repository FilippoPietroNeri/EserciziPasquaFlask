from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/wtitze/3E/main/2010.csv", delimiter=';')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/by/titolo')
def title():
    return render_template('titles.html')
    
@app.route('/by/genere')
def genere():
    moviesGenres = df[~df['Genres'].str.contains('\|')]['Genres'].to_list()
    moviesGenres = list(set(moviesGenres))
    return render_template('genres.html', moviesGenres = moviesGenres )

@app.route('/by/tendina')
def tendina():
    moviesGenres = df[~df['Genres'].str.contains('\|')]['Genres'].to_list()
    moviesGenres = list(set(moviesGenres))
    return render_template('form3.html', moviesGenres = moviesGenres )

@app.route('/by/radio')
def radio():
    return "assgasdg"

@app.route('/by/checkbox')
def checkbox():
    moviesGenres = df[~df['Genres'].str.contains('\|')]['Genres'].to_list()
    moviesGenres = list(set(moviesGenres))
    return render_template('form4.html', moviesGenres = moviesGenres )

@app.route('/by/budget')
def budget():
    table = df[df['Budget'].isna()].to_html()
    return render_template('risultato.html', table = table)


# API

@app.route('/risultato/titolo')
def restitle():
    filmInput = request.args.get('filmInput')
    film = df[df.Title.str.contains(filmInput)]
    if len(film) == 0:
        table = 'film non trovato'
    else:
        table = film.to_html()
    return render_template('risultato.html', table = table)
    
@app.route('/risultato/genere')
def resgenere():
    filmInput = str(request.args.get('filmInput'))
    film = df[df.Genres.str.contains(filmInput)]
    if len(film) == 0:
        table = 'film non trovato'
    else:
        table = film.to_html()
    return render_template('risultato.html', table = table)

@app.route('/risultato/tendina')
def restendina():
    filmInput = str(request.args.get('filmInput'))
    film = df[df.Genres.str.contains(filmInput)]
    if len(film) == 0:
        table = 'film non trovato'
    else:
        table = film.to_html()
    return render_template('risultato.html', table = table)

@app.route('/risultato/radio')
def resradio():
    filmInput = str(request.args.get('filmInput'))
    film = df[df.Genres.str.contains(filmInput)]
    if len(film) == 0:
        table = 'film non trovato'
    else:
        table = film.to_html()
    return render_template('risultato.html', table = table)

@app.route('/risultato/checkbox')
def rescheckbox():
    filmInput = request.args.get('filmInput')
    film = pd.DataFrame()
    for i in filmInput:
       film = pd.concat([film, df[df.Genres.str.contains(i)]])
    if len(film) == 0:
        table = 'film non trovato'
    else:
        table = film.to_html()
    return render_template('risultato.html', table = table)

@app.route('/risultato/budget')
def resbudget():
    table = df[df['Budget'].isna()].to_html()
    return render_template('risultato.html', table = table)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3245,debug=True)