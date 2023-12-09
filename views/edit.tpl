<!DOCTYPE html>
<html>
<head>
    <title>Edit Movie</title>
</head>
<body>
    <h1>Edit Movie</h1>
    <form action="/edit/{{ movie[0] }}" method="post">
        <label>Title:</label>
        <input type="text" name="title" value="{{ movie[1] }}" required><br>

        <label>Release Year:</label>
        <input type="number" name="release_year" value="{{ movie[2] }}" required><br>

        <label>Genre:</label>
        <select name="genre_id">
            % for genre in genres:
            % if genre[0] == movie[3]:
            <option value="{{ genre[0] }}" selected>{{ genre[1] }}</option>
            % else:
            <option value="{{ genre[0] }}">{{ genre[1] }}</option>
            % end
            % end
        </select><br>

        <input type="submit" value="Save">
    </form>
    <p><a href="/">Back to List</a></p>
</body>
</html>
