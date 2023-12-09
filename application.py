import sqlite3
from bottle import Bottle, route, run, template, request, redirect

app = Bottle()

# Connect to SQLite database
conn = sqlite3.connect('movie_genre.db')
cursor = conn.cursor()

@app.route('/')
def index():
    search_term = request.query.get('search', '')
    query = '''
        SELECT movies.id, movies.title, movies.release_year, genre.name
        FROM movies
        INNER JOIN genre ON movies.genre_id = genre.id
        WHERE movies.title LIKE ? OR genre.name LIKE ?
    '''
    cursor.execute(query, (f'%{search_term}%', f'%{search_term}%'))
    result = cursor.fetchall()
    return template('index', movies=result)


@app.route('/add')
def add_form():
    cursor.execute('SELECT * FROM genre')
    genres = cursor.fetchall()
    return template('insert', genres=genres)


@app.route('/add', method='POST')
def add():
    title = request.forms.get('title')
    release_year = request.forms.get('release_year')
    genre_id = request.forms.get('genre_id')

    cursor.execute("INSERT INTO movies (title, release_year, genre_id) VALUES (?, ?, ?)",
                   (title, release_year, genre_id))
    conn.commit()

    redirect('/')


@app.route('/edit/<movie_id>')
def edit_form(movie_id):
    cursor.execute("SELECT * FROM movies WHERE id=?", (movie_id,))
    movie = cursor.fetchone()

    cursor.execute('SELECT * FROM genre')
    genres = cursor.fetchall()

    return template('edit', movie=movie, genres=genres)


@app.route('/edit/<movie_id>', method='POST')
def edit(movie_id):
    title = request.forms.get('title')
    release_year = request.forms.get('release_year')
    genre_id = request.forms.get('genre_id')

    cursor.execute("UPDATE movies SET title=?, release_year=?, genre_id=? WHERE id=?",
                   (title, release_year, genre_id, movie_id))
    conn.commit()

    redirect('/')


@app.route('/delete/<movie_id>')
def delete(movie_id):
    cursor.execute("DELETE FROM movies WHERE id=?", (movie_id,))
    conn.commit()

    redirect('/')


if __name__ == '__main__':
    run(app, host='localhost', port=8080)